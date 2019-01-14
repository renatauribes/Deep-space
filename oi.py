import wpilib
from state import state

def read_input_mecanum ():
	controller = wpilib.Joystick(1)


	x = controller.getX()
	state["mov_x"] = x

	y = controller.getY()
	state["mov_y"] = y

	z = controller.getZ()
	state["mov_z"] = z

	button_x = controller.getRawButton(8)
	state["button_x_active"] = button_x

	
def read_input_cargo ():
	stick = wpilib.Joystick(1)

	button_1_is_pressed = stick.getRawButton(5)
	state["cargo"] = button_1_is_pressed
	
def read_input_lift ():

	stick = wpilib.Joystick(1)
	
	button_2_is_pressed = stick.getRawButton(6)
	state["lift"] = button_2_is_pressed