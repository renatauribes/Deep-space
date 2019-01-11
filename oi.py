import wpilib
from state import state

def read_input_chasis ():
	stick = wpilib.Joystick(1)
	y = stick.getY()
	state["chasis_y_mov"] = y
	x = stick.getX()
	state["chasis_x_mov"] = x

#def read_feeder():
	#stick = wpilib.Joystick(1)

	#button_1_is_pressed = stick.getRawButton(1)
	#state["cargo"] = button_1_is_pressed

	#button_2_is_pressed = stick.getRawButton(2)
	
def cargo():
	stick = wpilib.Joystick(1)

	button_1_is_pressed = stick.getRawButton(1)
	state["cargo"] = button_1_is_pressed
	
def lift():

	stick = wpilib.Joystick(1)
	
	button_2_is_pressed = stick.getRawButton(2)
	state["lift"] = button_2_is_pressed