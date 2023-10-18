#This animations is a little thing that shows the character Hornet, from the hit game Hollow Knight, throwing her needle at a UFO in the sky, which proceeds to make the UFO crash to the ground. 

#imports
from tkinter import*
from random import *
from time import *

myInterface = Tk()
screen = Canvas( myInterface, width=800, height=600, background="orange")
screen.pack()

#sun
screen.create_arc(700, 500, 800, 600, start=0, extent=180, fill="yellow")

#clouds, they are randomized
cloud_number = randint(1, 5)
for a in range (cloud_number):
  cloudx1 = randint(1, 750)
  cloudy1 = randint(1, 250)
  screen.create_oval(cloudx1, cloudy1, cloudx1 + 180, cloudy1 + 50, fill="white", outline="white")
  screen.create_oval(cloudx1 + 40, cloudy1 - 25, cloudx1 + 110, cloudy1 + 50, fill="white", outline="white")
  screen.create_oval(cloudx1 + 70, cloudy1 - 25, cloudx1 + 140, cloudy1 + 50, fill="white", outline="white")

#ground
screen.create_rectangle(0, 550, 800, 600, fill="green")

#hornet's head
screen.create_oval(85, 450, 115, 500, fill="white")
screen.create_oval(95, 450, 105, 475, fill="orange")
#hornet's eyes
screen.create_oval(90, 480, 95, 490, fill="black")
screen.create_oval(105, 480, 110, 490, fill="black")
#hornet's body
screen.create_polygon(90, 500, 110, 500, 100, 515, fill="maroon")
screen.create_polygon(100, 510, 115, 540, 85, 540, fill="maroon")
#hornet's legs
screen.create_line(95, 540, 95, 560, width=3, fill="black")
screen.create_line(105, 540, 105, 560, width=3, fill="black")

#ufo
ufo1 = screen.create_oval(500, 100, 550, 150, fill="light blue")
ufo2 = screen.create_oval(475, 125, 575, 150, fill="grey")

#hornet's needle & throw
for x in range (190):
  speed = x * 2
  needle = screen.create_polygon(150 + speed, 500 - speed, 112 + speed, 530 - speed, 118 + speed, 540 - speed, fill="grey", outline="black")
  screen.update()
  sleep(0.02)
  screen.delete(needle)

#explosion 1
explosion = screen.create_oval(450, 50, 600, 200, fill="red")
screen.update()
sleep(1)
screen.delete(explosion)

#UFO gets hit and falls
screen.delete(ufo1, ufo2)
for x in range(32):
  ufox = 0.1 * x + 500
  ufoy = 0.5 * x ** 2 - 2 * x + 100
  ufo1 = screen.create_oval(ufox, ufoy, ufox + 50, ufoy + 50, fill="light blue")
  ufo2 = screen.create_oval(ufox - 25, ufoy + 25, ufox + 75, ufoy + 50, fill="grey")
  screen.update()
  if x != 31:
    sleep(0.02)
  screen.delete(ufo1, ufo2)

#second explosion
screen.update()
explosion = screen.create_oval(450, 475, 600, 650, fill="red")
screen.update() #all of these screen.update()s are here because the screen needs to update, the explosion needs to happen right as the UFO touches the ground
sleep(1)
screen.delete(explosion)

#SHAW!
screen.create_text(85, 400, text="SHAW!", font="Comic 25", fill="white", anchor=W)

screen.update
