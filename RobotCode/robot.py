#!/usr/bin/env python3 # <---- This runs the code

import wpilib
import time
from networktables import NetworkTables

NetworkTables.initialize()
sd = NetworkTables.getTable("SmartDashboard")


class robot(wpilib.IterativeRobot):

    def robotInit(self):
        #Motors
        self.leftMotor = wpilib.Talon(0) # <-- This is what links our PWM port on the CRIO to a physical ESC.
        self.rightMotor = wpilib.Talon(1)

        #User Input
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers

        #Drive
        self.robotDrive = wpilib.RobotDrive(self.leftMotor, self.rightMotor)

    def disabledInit(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        '''
        self.robotDrive.arcadeDrive(Forward/Backwards Axis, Rotation axis)
        '''
        i = 0
        #This doesn't work yet
        while True:
            print('dsTime:', sd.getNumber('dsTime', 'N/A'))
            sd.putNumber('robotTime', i)
            time.sleep(1)
            i += 1
            print(i)

        #Drive
        self.robotDrive.arcadeDrive(self.playerOne.getY(0), self.playerOne.getX(0))

if __name__ == "__main__":
    '''
    This is the end of the code. Don't mess with this part =)
    '''
    wpilib.run(robot)
