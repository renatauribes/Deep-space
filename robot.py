
import wpilib
import wpilib.drive
from state import state

from wpilib.drive import MecanumDrive

from oi import read_input_mecanum
from oi import read_input_lift
from oi import read_input_cargo


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		# Ismafeeder
		self.cargo_motor = wpilib.Spark(4)
		self.lift_motor = wpilib.Spark(5)
		
		# Mecanum drive
		self.frontLeftMotor = wpilib.Talon(0)
		self.rearLeftMotor = wpilib.Talon(1)
		self.frontRightMotor = wpilib.Talon(2)
		self.rearRightMotor = wpilib.Talon(3)

		self.sensor_1 = wpilib.DigitalInput(1)

		self.frontLeftMotor.setInverted(True)

		self.rearLeftMotor.setInverted(True)


		self.drive = MecanumDrive(self.frontLeftMotor,
										 self.rearLeftMotor,
										 self.frontRightMotor,
										 self.rearRightMotor)


	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""

		read_input_mecanum()
		x = state["mov_x"]
		y = state["mov_y"]
		z = state["mov_z"]

		

		if state["button_x_active"]:
			if self.sensor_1.get():
				self.drive.driveCartesian(0, 0, 0, 0)
			else:
				self.drive.driveCartesian(0, -1, 0, 0)

		else:
			self.drive.driveCartesian(x, y, z, 0)


		read_input_cargo()
		if state["cargo"]:
			self.cargo_motor.set(1)
		else:
			self.cargo_motor.set(0)

		read_input_lift()
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

print("holaaa")

if __name__ == "__main__":
	wpilib.run(MyRobot)