import tinytuya

c = tinytuya.Cloud(
        apiRegion="in", 
        apiKey="ks7drncsugvsfcanjwen", 
        apiSecret="5ae091516bd449d4bf3a74065bc949e3", 
        apiDeviceID="d79c2ecbff7321e3f9pf0j")

# Display list of devices
devices = c.getdevices()
#print("Device List: %r" % devices)

# Select a Device ID to Test
laptopPlugid = "d79c2ecbff7321e3f9pf0j"
paniGaramId = "d71e68e803d616215amq45"

# Display Properties of Device
result = c.getproperties(laptopPlugid)
#print("Properties of device:\n", result)

# Display Status of Device
result = c.getstatus(laptopPlugid)
print("Status of device:\n", result)
plug = result.get('result')
statusPlug = plug[0].get('value')


# Send Command - Turn on switch
commandsOn = {
    "commands": [
        {"code": "switch_1", "value": True},
        {"code": "countdown_1", "value": 0},
    ]
}

commandsOff = {
    "commands": [
        {"code": "switch_1", "value": False},
        {"code": "countdown_1", "value": 0},
    ]
}

print("Sending command...")
if statusPlug == True:
    result = c.sendcommand(laptopPlugid,commandsOff)
else:
    result = c.sendcommand(laptopPlugid,commandsOn)
print("Results\n:", result)