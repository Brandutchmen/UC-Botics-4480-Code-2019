from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state
from components import drive

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Forward Turn Right'
    DEFAULT = False

    def initialize(self):
        self.speed = 0.7


    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.drive.masterDrive(0, 0)
        self.drive.setAutoTurn(90)
        self.drive.autoOneEighty()

    @timed_state(duration=6, next_state='stop')
    def drive_forward(self):

        self.drive.autoTurn.enable()
        self.drive.masterDrive(0,0)


    @state()
    def stop(self):
        self.drive.masterDrive(0,0)
