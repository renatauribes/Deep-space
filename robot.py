
import wpilib
import wpilib.drive
from state import state
from oi import read_input_chasis
from oi import lift
from oi import cargo


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
       
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.cargo_motor = wpilib.Spark(2)
        self.lift_motor = wpilib.Spark(3)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)


    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        read_input_chasis()
        x = state["chasis_x_movement"]
        y = state["chasis_y_movement"]

        self.drive.arcadeDrive(y,x)

        #read_feeder()

        #if state["cargo"]:
            #self.cargo_motor.set(1)
        #elif state["cargo"] == False:
            #self.cargo_motor.set(-1)
        #else:
            #self.cargo_motor.set(0)
        cargo()
        
        if state["cargo"]:
            self.cargo_motor.set(1)
        else:
            self.cargo_motor.set(0)

        lift()
        
        if state["lift"]:
            state["timer_lift"] += 1
            if state["timer_lift"] <= 50:
                self.lift_motor.set(1)
            elif state["timer_lift"] > 50 and state["timer_lift"] < 100:
                self.lift_motor.set(0)
                self.cargo_motor.set(-1)
            elif state["timer_lift"] >= 100:
                self.lift_motor.set(-1)
                self.cargo_motor.set(0)
        else:
            state["timer_lift"] = 0
            self.lift_motor.set(0)
        
        print(state)

if __name__ == "__main__":
    wpilib.run(MyRobot)