import paho.mqtt.client as paho                         # mqtt library
import os
import json
import time
import random
from datetime import datetime
import MQTTSN, socket, time, MQTTSNinternal, thread, types, sys, struct

"""
/****************************************************************************

    START CLASSES : Callback, Client

*****************************************************************************/
"""
class Callback:

  def __init__(self):
    self.events = []
    self.registered = {}
    self.payload = None

  def connectionLost(self, cause):
    print "default connectionLost", cause
    self.events.append("disconnected")

  def messageArrived(self, topicName, payload, qos, retained, msgid):
    print "default publishArrived", topicName, payload, qos, retained, msgid
    self.payload = payload
    return True

  def deliveryComplete(self, msgid):
    print "default deliveryComplete"
  
  def advertise(self, address, gwid, duration):
    print "advertise", address, gwid, duration

  def register(self, topicid, topicName):
    self.registered[topicId] = topicName


class Client:

  def __init__(self, clientid, host="localhost", port=1883):
    self.clientid = clientid
    self.host = host
    self.port = port
    self.msgid = 1
    self.callback = None
    self.__receiver = None
    
  def start(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind((self.host, self.port))
    mreq = struct.pack("4sl", socket.inet_aton(self.host), socket.INADDR_ANY)

    self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    self.startReceiver()
      
  def stop(self):
    self.stopReceiver()

  def __nextMsgid(self):
    def getWrappedMsgid():
      id = self.msgid + 1
      if id == 65535:
        id = 1
      return id

    if len(self.__receiver.outMsgs) >= 65535:
      raise "No slots left!!"
    else:
      self.msgid = getWrappedMsgid()
      while self.__receiver.outMsgs.has_key(self.msgid):
        self.msgid = getWrappedMsgid()
    return self.msgid


  def registerCallback(self, callback):
    self.callback = callback


  def connect(self, cleansession=True):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #self.sock.settimeout(5.0)

    self.sock.connect((self.host, self.port))

    connect = MQTTSN.Connects()
    connect.ClientId = self.clientid
    connect.CleanSession = cleansession
    connect.KeepAliveTimer = 0
    self.sock.send(connect.pack())

    response, address = MQTTSN.unpackPacket(MQTTSN.getPacket(self.sock))
    assert response.mh.MsgType == MQTTSN.CONNACK
    
    self.startReceiver()

    
  def startReceiver(self):
    self.__receiver = MQTTSNinternal.Receivers(self.sock)
    if self.callback:
      id = thread.start_new_thread(self.__receiver, (self.callback,))


  def waitfor(self, msgType, msgId=None):
    if self.__receiver:
      msg = self.__receiver.waitfor(msgType, msgId)
    else:
      msg = self.__receiver.receive()
      while msg.mh.MsgType != msgType and (msgId == None or msgId == msg.MsgId):
        msg = self.__receiver.receive()
    return msg


  def subscribe(self, topic, qos=2):
    subscribe = MQTTSN.Subscribes()
    subscribe.MsgId = self.__nextMsgid()
    if type(topic) == types.StringType:
      subscribe.TopicName = topic
      if len(topic) > 2:
        subscribe.Flags.TopicIdType = MQTTSN.TOPIC_NORMAL
      else:
        subscribe.Flags.TopicIdType = MQTTSN.TOPIC_SHORTNAME
    else:
      subscribe.TopicId = topic # should be int
      subscribe.Flags.TopicIdType = MQTTSN.TOPIC_PREDEFINED
    subscribe.Flags.QoS = qos
    if self.__receiver:
      self.__receiver.lookfor(MQTTSN.SUBACK)
    self.sock.send(subscribe.pack())
    msg = self.waitfor(MQTTSN.SUBACK, subscribe.MsgId)
    return msg.ReturnCode, msg.TopicId


  def unsubscribe(self, topics):
    unsubscribe = MQTTSN.Unsubscribes()
    unsubscribe.MsgId = self.__nextMsgid()
    unsubscribe.data = topics
    if self.__receiver:
      self.__receiver.lookfor(MQTTSN.UNSUBACK)
    self.sock.send(unsubscribe.pack())
    msg = self.waitfor(MQTTSN.UNSUBACK, unsubscribe.MsgId)
  
  
  def register(self, topicName):
    register = MQTTSN.Registers()
    register.TopicName = topicName
    if self.__receiver:
      self.__receiver.lookfor(MQTTSN.REGACK)
    self.sock.send(register.pack())
    msg = self.waitfor(MQTTSN.REGACK, register.MsgId)
    return msg.TopicId


  def publish(self, topic, payload, qos=0, retained=False):
    publish = MQTTSN.Publishes()
    publish.Flags.QoS = qos
    publish.Flags.Retain = retained
    if type(topic) == types.StringType:
      publish.Flags.TopicIdType = MQTTSN.TOPIC_SHORTNAME
      publish.TopicName = topic
    else:
      publish.Flags.TopicIdType = MQTTSN.TOPIC_NORMAL
      publish.TopicId = topic
    if qos in [-1, 0]:
      publish.MsgId = 0
    else:
      publish.MsgId = self.__nextMsgid()
#      print "MsgId", publish.MsgId
      self.__receiver.outMsgs[publish.MsgId] = publish
    publish.Data = payload
    self.sock.send(publish.pack())
    return publish.MsgId
  

  def disconnect(self):
    disconnect = MQTTSN.Disconnects()
    if self.__receiver:
      self.__receiver.lookfor(MQTTSN.DISCONNECT)
    self.sock.send(disconnect.pack())
    msg = self.waitfor(MQTTSN.DISCONNECT)
    

  def stopReceiver(self):
    self.sock.close() # this will stop the receiver too
    assert self.__receiver.inMsgs == {}
    assert self.__receiver.outMsgs == {}
    self.__receiver = None

  def receive(self):
    return self.__receiver.receive()


def publish(topic, payload, retained=False, port=1883, host="localhost"):
  publish = MQTTSN.Publishes()
  publish.Flags.QoS = 3
  publish.Flags.Retain = retained  
  if type(topic) == types.StringType:
    if len(topic) > 2:
      publish.Flags.TopicIdType = MQTTSN.TOPIC_NORMAL
      publish.TopicId = len(topic)
      payload = topic + payload
    else:
      publish.Flags.TopicIdType = MQTTSN.TOPIC_SHORTNAME
      publish.TopicName = topic
  else:
    publish.Flags.TopicIdType = MQTTSN.TOPIC_NORMAL
    publish.TopicId = topic
  publish.MsgId = 0
#  print "payload", payload
  publish.Data = payload
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.sendto(publish.pack(), (host, port))
  sock.close()
  return 


"""
/****************************************************************************

    END CLASSES : Callback, Client

*****************************************************************************/
"""

# Communication
ACCESS_TOKEN_C = 'thP4KR1bffpe3mjgkaS5'                 # Token of device C
ACCESS_TOKEN_D = 'y4dQQRQkieiBbH1d0WBU'                 # Token of device C
broker = "demo.thingsboard.io"                          # host name
tb_topic = "v1/devices/me/telemetry"                    # Thingsboard topic
tb_port = 1883                                          # data listening port

internal_port = 1885
internal_topic_c = "devices/dev_c"                      # env station c topic
internal_topic_d = "devices/dev_d"                      # env station c topic

def on_publish(client,userdata,result):                 # create function for callback
    print("data published to thingsboard \n")
    pass

# Setting Up Client C
client_C = paho.Client("EnvStat_C")                     # create client object
client_C.on_publish = on_publish                        # assign function to callback
client_C.username_pw_set(ACCESS_TOKEN_C)                # access token from thingsboard device
client_C.connect(broker, tb_port, keepalive=60)              # establish connection

# Setting Up Client D
client_D = paho.Client("EnvStat_D")                     # create client object
client_D.on_publish = on_publish                        # assign function to callback
client_D.username_pw_set(ACCESS_TOKEN_D)                # access token from thingsboard device
client_D.connect(broker, tb_port, keepalive=60)              # establish connection

# Start loooooooooop
client_C.loop_start()
client_D.loop_start()

# RSMB STUFFS
rsmb_c = Client("dev_c", port=internal_port)
rsmb_d = Client("dev_d", port=internal_port)

# Starting up our rsmb
while (True) :
    
    # Device C data acquiring    
    rsmb_c.registerCallback(Callback())
    rsmb_c.connect()
    rc, topic1 = rsmb_c.subscribe(internal_topic_c)

    # Device D data acquiring
    rsmb_d.registerCallback(Callback())
    rsmb_d.connect()
    rd, topic2 = rsmb_d.subscribe(internal_topic_d)

    while (rsmb_c.callback.payload == None or rsmb_d.callback.payload == None ) :
        pass
    #print (rsmb_c.callback.payload)
    
    # Device C data transmission to ThingsBoard
    print("CCC ENVIRONMENTAL STATION C ")
    print ("\n")
    #payload_C = "{\"humidity\":\""+str(random.randint(0, 100)) +"\"}" # get payload from C
    ret = client_C.publish(tb_topic, rsmb_c.callback.payload)
    print(rsmb_c.callback.payload)
    print ("\n")
    
    # Device D data transmission to ThingsBoard
    print("DDD ENVIRONMENTAL STATION D ")
    print ("\n")
    ret = client_D.publish(tb_topic, rsmb_d.callback.payload)
    print(rsmb_d.callback.payload)
    print ("\n")
    
    # RSMB STUFFS
    rsmb_c.disconnect()
    rsmb_d.disconnect()
