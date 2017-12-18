import serial
import pygame
from pygame.locals import *

ARDUINO_PORT = 'COM3'


class RCTest(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((100,100))
        self.ser = serial.Serial(ARDUINO_PORT, 9600, timeout=1)
        self.send_inst = True
        self.steer()

    def steer(self):

        while self.send_inst:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    key_input = pygame.key.get_pressed()

                    # complex orders
                    if key_input[pygame.K_UP] and key_input[pygame.K_RIGHT]:
                        print("Forward Right")
                        self.ser.write(str("F_RIGHT").encode())

                    elif key_input[pygame.K_UP] and key_input[pygame.K_LEFT]:
                        print("Forward Left")
                        self.ser.write(str("F_LEFT").encode())

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_RIGHT]:
                        print("Reverse Right")
                        self.ser.write(str("R_RIGHT").encode())

                    elif key_input[pygame.K_DOWN] and key_input[pygame.K_LEFT]:
                        print("Reverse Left")
                        self.ser.write(str("R_LEFT").encode())

                    # simple orders
                    elif key_input[pygame.K_UP]:
                        print("Forward")
                        self.ser.write(str("FORWARD").encode())

                    elif key_input[pygame.K_DOWN]:
                        print("Reverse")
                        self.ser.write(str("BACK").encode())

                    elif key_input[pygame.K_RIGHT]:
                        print("Right")
                        self.ser.write(str("RIGHT").encode())

                    elif key_input[pygame.K_LEFT]:
                        print("Left")
                        self.ser.write(str("LEFT").encode())

                    # exit
                    elif key_input[pygame.K_x] or key_input[pygame.K_q]:
                        print('Exit')
                        self.send_inst = False
                        self.ser.write(str("STOP").encode())
                        self.ser.close()
                        break

                elif event.type == pygame.KEYUP:
                    self.ser.write(str("STOP").encode())

if __name__ == '__main__':
    RCTest()
