#!/usr/bin/env python3
from io import SEEK_CUR
from os import truncate
import re
import math
from ev3dev.core import Led, Screen
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev.ev3 import Button, ColorSensor
from time import sleep

lcd = Screen()


class Robot:
    def __init__(self):
        self.motor_right = LargeMotor(OUTPUT_B)
        self.motor_left = LargeMotor(OUTPUT_C)
        self.motor_right.position = 0
        self.motor_left.position = 0
        self.position_motor_old_right = 0
        self.position_motor_old_left = 0
        self.x = 0
        self.y = 0
        self.fi = 0
        self.R = 2.8
        self.L = 12.5
        self.v = 0
        self.omega = 0
        self.Vr = 0
        self.Vl = 0

    def position(self):
        n_r = self.motor_right.position
        n_l = self.motor_left.position
        delta_n_r = n_r - self.get_position_motor_old_right()
        delta_n_l = n_l - self.get_position_motor_old_left()
        D_r = 2 * math.pi * self.get_R() * (delta_n_r / 360)
        D_l = 2 * math.pi * self.get_R() * (delta_n_l / 360)
        Dc = (D_r + D_l) / 2
        self.x = self.get_x() + (Dc * math.cos(self.get_fi()))
        self.y = self.get_y() + (Dc * math.sin(self.get_fi()))
        self.fi = self.get_fi() + ((D_r - D_l) / self.L)
        self.position_motor_old_right = n_r
        self.position_motor_old_left = n_l

    def angle_to_goal(self, xg, yg):
        psi = math.atan2(yg - self.get_y(), xg - self.get_x())
        return psi

    def go_to_goal(self, xg, yg):
        e = self.angle_to_goal(xg, yg) - self.get_fi()
        e = math.atan2(math.sin(e), math.cos(e))
        return e

    def run(self, e, goal):
        k = 3
        if goal[1] > 0:
            k = 120
        self.motor_right.run_forever(speed_sp=140 + k * e)
        self.motor_left.run_forever(speed_sp=140 - k * e)

    def stop(self):
        self.motor_right.stop()
        self.motor_left.stop()

    def move_target(self, goal):
        drift = 3
        while not (abs(self.get_x() - goal[0]) < drift and abs(self.get_y() - goal[1]) < drift):
            lcd.clear()
            lcd.draw.text((6, 55), 'x:{},y:{}'.format(int(self.get_x()), int(self.get_y())))
            lcd.update()
            print(int(self.get_x()))
            print(int(self.get_y()))
            self.position()
            e = self.go_to_goal(goal[0], goal[1])
            self.run(e, goal)
        self.stop()

    def get_position_motor_old_right(self):
        return self.position_motor_old_right

    def get_position_motor_old_left(self):
        return self.position_motor_old_left

    def get_fi(self):
        return self.fi

    def get_R(self):
        return self.R

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_v(self):
        return self.v


wspolrzedne = [200, 0]
robot = Robot()
sleep(5)
robot.move_target(wspolrzedne)
wspolrzedne = [125, 100]
robot.move_target(wspolrzedne)
wspolrzedne = [125, 200]
robot.move_target(wspolrzedne)