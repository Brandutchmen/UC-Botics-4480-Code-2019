#!/usr/bin/env python3 # <---- This runs the code
'''
This is a networktables test
'''
import wpilib
import time
from networktables import NetworkTables

class robot(wpilib.IterativeRobot):

    def robotInit(self):
        #User Input
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers

        self.i = 5
    def teleopPeriodic(self):
        NetworkTables.initialize()
        table = NetworkTables.getTable("SmartDashboard")

        print('Time? (robot) ', table.getNumber('time', 'N/A'))
        table.putNumber('time', self.i)
        time.sleep(1)
        self.i = self.i+1


if __name__ == "__main__":
    wpilib.run(robot)
