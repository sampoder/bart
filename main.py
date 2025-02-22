import requests
import time
import serial
from playsound import playsound

ser = serial.Serial("/dev/cu.usbmodem1101", 9600) # establishes serial connection, you may need to change this.

station = 'DBRK' # D-owntown B-e-RK-eley

url = 'https://api.bart.gov/api/etd.aspx?cmd=etd&orig=' + station + '&key=MW9S-E7SL-26DU-VV8V&json=y' # this key is public! go BART!

direction = 'South' # feel free to change this to North - I normally travel into Oakland / SF from Berkeley

last_played = 0 # this variable is used to only play the sound once every minute

ser.write(bytearray("BLANK",'ascii')) # this resets the Arduino and turns off any lights

# use the mode variable to configure the piece

mode = "STANDARD" 
# mode = "DEMO"
# mode = "LEAVE_THE_HOUSE"

if mode == "DEMO":
    # basic demo, light up red for 10 seconds, then play the leaving sound.
    for x in range(10):
        ser.write(bytearray("RED",'ascii'))
        time.sleep(1)
    
    ser.write(bytearray("BLANK",'ascii'))
    
    playsound('leaving.mp3')
    
    while True:
        ser.write(bytearray("BLANK",'ascii'))
else:
    while True:
        response = requests.get(url)
        incoming = response.json()["root"]["station"][0]["etd"]
        flag = True # this flag is used to keep track of whether or not the train should light up.
        for line in incoming:
          approaching = line["estimate"][0]
          if approaching["direction"] == direction:
            # see README for explanation of modes
            if (approaching['minutes'] == 'Leaving' and mode == "STANDARD") or (approaching['minutes'] == '13' and mode == "LEAVE_THE_HOUSE"):
                if last_played + 60 < int(time.time()): # only play the noise every 60 seconds
                    last_played = int(time.time())
                    playsound('leaving.mp3')
            elif (approaching['minutes'] != 'Leaving' and int(approaching['minutes']) < 2 and mode == "STANDARD") or (approaching['minutes'] == '14' and mode == "LEAVE_THE_HOUSE"):
                flag = False # don't reset the train to blank
                ser.write(bytearray(approaching["color"],'ascii')) # instructs the train to light up the line's colour
            else:
                print(approaching["color"])
                print(approaching['minutes'])
        if flag:
          ser.write(bytearray("BLANK",'ascii'))
        time.sleep(1)
    
