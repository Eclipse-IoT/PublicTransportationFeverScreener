"""This example is for Raspberry Pi (Linux) only!
   It will not work on microcontrollers running CircuitPython!"""
 
import os
import math
import time
import functools
import operator
import busio
import board
import RPi.GPIO as GPIO
import numpy as np
import pygame
import paho.mqtt.client as mqtt

from scipy.interpolate import griddata
from mfrc522 import SimpleMFRC522

from colour import Color
 
import adafruit_amg88xx
 

MQTT_BROKER = "172.31.0.74" #IP Address for the Broker
# Paho-MQTT Client
client = mqtt.Client()
client.username_pw_set("raspberrypi", "raspberrypi") #Setting the password and username

reader = SimpleMFRC522() #RFID Reader
client.connect(MQTT_BROKER)
    

i2c_bus = busio.I2C(board.SCL, board.SDA)
 
#low range of the sensor (this will be blue on the screen)
MINTEMP = 18.
 
#high range of the sensor (this will be red on the screen)
MAXTEMP = 38.

REGTEMP = 27 #Normal Human temperature
FEVERTEMP= 32 #Fever temperature in human, normally 38
#how many color values we can have
COLORDEPTH = 1024
 
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

upArrow = pygame.image.load("greenarrow.png")
upArrow = pygame.transform.scale(upArrow,(700,700))
downArrow = pygame.transform.flip(upArrow, False, True)

redX = pygame.image.load("redx.png")
redX = pygame.transform.scale(redX,(700,700))

greenCheck = pygame.image.load("greencheck.png")
greenCheck = pygame.transform.scale(greenCheck,(900,700))


font = pygame.font.SysFont("Arial", 60)
black = (0,0,0)
newBalance = "0"

feverDetected = font.render("     Fever Detected! Please Exit", True, black)
moveCloser = font.render("Please Move Closer to the Sensor", True, black)
insufficientFunds = font.render("               Insufficient Funds! ", True, black)
tapBelow = font.render("      Please Tap Your Card Below", True, black)
state = 0 

#initialize the sensor
sensor = adafruit_amg88xx.AMG88XX(i2c_bus)
 
# pylint: disable=invalid-slice-index
points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]
# pylint: enable=invalid-slice-index
 
#sensor is an 8x8 grid so lets do a square
height = 360
width = 360
 
#the list of colors we can choose from
blue = Color("indigo")
colors = list(blue.range_to(Color("red"), COLORDEPTH))
 
#create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]
 
displayPixelWidth = width / 30
displayPixelHeight = height / 30
 
lcd = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
 
#lcd.fill((255, 0, 0))
 
pygame.display.update()
pygame.mouse.set_visible(False)

lcd.fill((255, 255, 255))

 
#some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))
 
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def greenCircle(x,y,r):
    pygame.draw.circle(lcd, (0,150,0), (x,y), r)
    
#let the sensor initialize
time.sleep(.1)
#greenCircle(960,400,360)
statusSymbol = upArrow
statusText = moveCloser
pygame.display.update()
while True:
    
    lcd.fill((255, 255, 255))#screen clear
    #read the pixels
    pixels = []
    for row in sensor.pixels:
        pixels = pixels + row
    pixels = [map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]
 
    #perform interpolation
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
 
    #draw everything
    for ix, row in enumerate(bicubic):
        for jx, pixel in enumerate(row):
            pygame.draw.rect(lcd, colors[constrain(int(pixel), 0, COLORDEPTH- 1)],
                             (displayPixelHeight * ix, displayPixelWidth * jx,
                              displayPixelHeight, displayPixelWidth))
            
    flatList = functools.reduce(operator.iconcat, sensor.pixels, [])   #Create a flatlist of the temperatures
    j = flatList
    
    
    if(sum(FEVERTEMP>i>REGTEMP for i in j)) >3: #if human infront of sensor?
        statusText = tapBelow
        statusSymbol = downArrow
        client.publish("Temperature", str(max(j)))
        
    else: #human not infront of sensor
        statusText = moveCloser
        statusSymbol = upArrow
            
    if (sum(i>FEVERTEMP for i in j) > 0): #If Fever?
        statusText =feverDetected
        statusSymbol = redX
        client.publish("Temperature", str(max(j)))
        client.publish("Fever")
    
    lcd.blit(statusSymbol,(610,50))
    lcd.blit(statusText, (540, 900))
    pygame.display.update()
    start = time.time()
   
    while(statusSymbol == downArrow or statusText == tapBelow):
        
        id, text = reader.read()
        GPIO.cleanup()
        if(float(text)<3.25):
            statusText = insufficientFunds
            statusSymbol = redX
        else:
            newBalance = str(float(text)-3.25)
            reader.write(newBalance)
            thankYou = font.render("Thank you, New Balance: $"+newBalance, True, black)
            client.publish("Transaction", time.time())
            statusText = thankYou
            statusSymbol = greenCheck
        
            

    while(statusSymbol == greenCheck or statusText == insufficientFunds):
        lcd.fill((255, 255, 255))#screen clear
        lcd.blit(statusSymbol,(610,50))
        lcd.blit(statusText, (540, 900))
        pygame.display.update()
        time.sleep(5)
        statusText = moveCloser
        statusSymbol = upArrow
        