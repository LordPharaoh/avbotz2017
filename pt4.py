ki = 1
kd = 1
kp = 1
bias = 0
desired = float(input("desired height:"))
accumulator = 0
past_error = 0

while True:
	error = get_height() - desired
	accumulator += error
	derivative = error - past_error
	past_error = error
	
	thrust = ki * accumulator + kp * error + kd * derivative + bias
	set_thrust(thrust)
	

