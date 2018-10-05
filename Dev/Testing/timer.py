#!/usr/bin/env python3 # <---- This runs the code
'''
This is a networktables test for a timer interface
'''
import wpilib
import time
from networktables import NetworkTables

class robot(wpilib.IterativeRobot):

    def robotInit(self):
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers

    def teleopPeriodic(self):

        NetworkTables.initialize()
        table = NetworkTables.getTable("SmartDashboard")

        print('ControllerY = ', table.getNumber('ctrlY', 'N/A'))
        table.putNumber('ctrlY', self.playerOne.getY(0))


if __name__ == "__main__":
    wpilib.run(robot)
