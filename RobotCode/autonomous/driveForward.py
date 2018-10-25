from robotpy_ext.autonomous import StatefulAutonomous, timed_state, state
from components import drive

class DriveForward(StatefulAutonomous):

    MODE_NAME = 'Drive Forward Short'
    DEFAULT = True

    def initialize(self):
        self.speed = 0.5

    @timed_state(duration=0.5, next_state='drive_forward', first=True)
    def drive_wait(self):
        self.drive.masterDrive(0, 0)

    @timed_state(duration=4, next_state='stop')
    def drive_forward(self):
        self.drive.masterDrive(self.speed, 0)

    @state()
    def stop(self):
        self.drive.masterDrive(0,0)
