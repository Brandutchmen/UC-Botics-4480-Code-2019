#!/usr/bin/env python3 # <---- This runs the code

import wpilib
from wpilib import drive
import time
from networktables import NetworkTables
from robotpy_ext.common_drivers import units, navx
from robotpy_ext.autonomous import AutonomousModeSelector

from components import drive

class robot(wpilib.IterativeRobot):

    def robotInit(self):

        #NetworkTables Init
        NetworkTables.initialize()
        self.table = NetworkTables.getTable("SmartDashboard")

        #Navx
        self.navx = navx.AHRS.create_spi()

        #PowerDistributionPanel
        self.power_board = wpilib.PowerDistributionPanel()

        #Motors
        self.leftMotor1 = wpilib.Spark(0) # <-- This is what links our PWM port on the CRIO to a physical ESC.
        self.leftMotor2 = wpilib.Spark(1) # <-- This is what links our PWM port on the CRIO to a physical ESC.
        self.left = wpilib.SpeedControllerGroup(self.leftMotor1, self.leftMotor2)

        self.rightMotor1 = wpilib.Spark(2)
        self.rightMotor2 = wpilib.Spark(3)
        self.right = wpilib.SpeedControllerGroup(self.rightMotor1, self.rightMotor2)

        self.liftMotor1 = wpilib.Talon(4)
        self.liftMotor2 = wpilib.Talon(5)
        self.liftMotor2.setInverted(True)
        self.lift = wpilib.SpeedControllerGroup(self.liftMotor1, self.liftMotor2)
        #User Input
        self.playerOne = wpilib.XboxController(0)# <-- This is for using Xbox controllers

        #Drive
        self.robotDrive = wpilib.drive.DifferentialDrive(self.left, self.right)

        #Drive.py init
        self.drive = drive.Drive(self.robotDrive, self.navx, self.left, self.right)

        self.components = {
            'drive': self.drive,
            'table': self.table
            }
        self.automodes = AutonomousModeSelector('autonomous', self.components)


    def disabledInit(self):
       self.table.putNumber('ctrlY', 0)
       self.table.putNumber('ctrlX', 0)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.table.putNumber('ctrlY', self.left.get())
        self.table.putNumber('ctrlX', self.right.get())
        self.automodes.run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):

        #NetworkTables Variables
        self.table.putNumber('ctrlY', self.left.get())
        self.table.putNumber('ctrlX', -1*self.right.get())

        #lift
        self.lift.set(self.playerOne.getYButton()+self.playerOne.getAButton()*-1)

        #Shoot
        #self.playerTwo.getTriggerAxis(1) + self.playerTwo.getTriggerAxis(0) * -1

        #Drive
        self.drive.masterDrive(self.playerOne.getY(0), self.playerOne.getY(1))


if __name__ == "__main__":
    wpilib.run(robot)
