#!/usr/bin/env python3 # <---- This runs the code

import wpilib
from wpilib import drive
import time
from networktables import NetworkTables

NetworkTables.initialize()
table = NetworkTables.getTable("SmartDashboard")


class robot(wpilib.IterativeRobot):

    def robotInit(self):
        #Motors
        self.leftMotor1 = wpilib.Talon(0) # <-- This is what links our PWM port on the CRIO to a physical ESC.
        self.leftMotor2 = wpilib.Talon(1) # <-- This is what links our PWM port on the CRIO to a physical ESC.
        self.left = wpilib.SpeedControllerGroup(self.leftMotor1, self.leftMotor2)

        self.rightMotor1 = wpilib.Talon(2)
        self.rightMotor2 = wpilib.Talon(3)
        self.right = wpilib.SpeedControllerGroup(self.rightMotor1, self.rightMotor2)

        #User Input
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers

        #Drive
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)

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
        NetworkTables.initialize()
        table = NetworkTables.getTable("SmartDashboard")

        print('ControllerY = ', table.getNumber('ctrlY', 'N/A'))
        table.putNumber('ctrlY', self.playerOne.getY(0))

        #Drive
        self.drive.curvatureDrive(self.playerOne.getY(0), self.playerOne.getX(0)*0.3, 1)



if __name__ == "__main__":
    '''
    This is the end of the code. Don't mess with this part =)
    '''
    wpilib.run(robot)
