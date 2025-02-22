import requests
import time
import serial
from playsound import playsound

ser = serial.Serial("/dev/cu.usbmodem1101", 9600)

station = 'DBRK'
url = 'https://api.bart.gov/api/etd.aspx?cmd=etd&orig=' + station + '&key=MW9S-E7SL-26DU-VV8V&json=y' # this key is public! go BART!

direction = 'South'

last_played = 0
ser.write(bytearray("BLANK",'ascii'))

mode = "STANDARD"
# mode = "DEMO"
# mode = "LEAVE_THE_HOUSE"

if mode == "DEMO":
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
        flag = True
        for line in incoming:
          approaching = line["estimate"][0]
          if approaching["direction"] == direction:
            if (approaching['minutes'] == 'Leaving' and mode == "STANDARD") or (approaching['minutes'] == '13' and mode == "LEAVE_THE_HOUSE"):
                print("byebye!")
                if last_played + 60 < int(time.time()):
                    last_played = int(time.time())
                    playsound('leaving.mp3')
            elif (approaching['minutes'] != 'Leaving' and int(approaching['minutes']) < 2 and mode == "STANDARD") or (approaching['minutes'] == '14' and mode == "LEAVE_THE_HOUSE"):
                print(approaching["color"])
                flag = False
                ser.write(bytearray(approaching["color"],'ascii'))
            else:
                print(approaching["color"])
                print(approaching['minutes'])
        if flag:
          ser.write(bytearray("BLANK",'ascii'))
        time.sleep(1)
    
