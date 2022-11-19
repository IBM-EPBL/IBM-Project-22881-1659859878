import requests 
import json
import ibmiotf.application 
import ibmiotf.device 
import time
import random 
import sys

# watson device details

organization = "4yi0vc" 
devicType = "BIN1" 
deviceId = "BIN1ID" 
authMethod= "token" 
authToken= "123456789"

#generate random values for randomo variables (temperature&humidity)
 


def myCommandCallback(cmd): 
    global a
    print("command recieved:%s" %cmd.data['command']) 
    control=cmd.data['command']
    print(control)

try:
deviceOptions={"org": organization, "type": devicType,"id": deviceId,"auth-method":authMethod,"auth-
token":authToken}
deviceCli = ibmiotf.device.Client(deviceOptions) 
except Exception as e:
print("caught exception connecting device %s" %str(e)) sys.exit()