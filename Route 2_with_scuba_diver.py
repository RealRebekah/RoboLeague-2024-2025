from hub import light_matrix, motion_sensor, port
import runloop, motor_pair, motor,math,time,runloop, color, color_sensor


async def drive(distance, speed):
    CM = round(distance * 17.5)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, CM, 0, velocity = speed, stop=motor.SMART_COAST)

async def turnLeft(angle):
    while motion_sensor.tilt_angles()[0]<(angle*10): #while the angle sensor is less than desired angle
        motor_pair.move(motor_pair.PAIR_1,-100, acceleration=600, velocity=350) #both motors will run -100 degrees
    motor_pair.stop(motor_pair.PAIR_1) #stop the motors after that while loop
    motion_sensor.reset_yaw(0) #reset yaw value
async def turnRight(angle):
    while motion_sensor.tilt_angles()[0]>(angle*-10): #getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100,acceleration=600, velocity=350) #move to right
    motor_pair.stop(motor_pair.PAIR_1) #stop the motors after that while loop
    motion_sensor.reset_yaw(0) #reset yaw value

async def whiteout(speed, port):
    while(color_sensor.color(port) == 10):
            motor_pair.move(motor_pair.PAIR_1, 0, velocity = speed) #drive robot until white is not sensed
    motor_pair.stop(motor_pair.PAIR_1)

async def moveMotor(degrees,speed, side):
    if (side == "left"):
        motor.run_for_degrees(port.A, degrees, speed, stop = motor.HOLD)
    if (side == "right"):
        motor.run_for_degrees(port.C, degrees, speed, stop = motor.HOLD)

max_speed = 1050
async def main():
    motor_pair.pair(motor_pair.PAIR_1,port.B,port.D)
    #write your code here
    await drive(-85,800)
    await turnLeft(47)
    await drive(5,800)

    await moveMotor(-200,max_speed,"left")
    time.sleep_ms(500)
    await moveMotor(150,200,"left")
    time.sleep_ms(200)
    await turnLeft(30)
    await drive(10,750)
    #await moveMotor(-70,600,"left")
    #await drive(-10,800)
    #await moveMotor(25,900,"left")
    await turnRight(78)
    await drive(-1,700)

    await moveMotor(-145,700, "left")
    time.sleep_ms(1000)
    await moveMotor(135,800,"left")
    await drive(7,700)
    await turnRight(82)
    await drive(22,700)
    await drive(-3,800)
    await turnRight(35)
    await drive(-13,900)
    await turnLeft(16)
    await drive(16,800)
    time.sleep_ms(200)
    await moveMotor(-175,400,"left")
    time.sleep_ms(200)
    await drive(-2,800)
    time.sleep_ms(100)
    await moveMotor(75,250,"left")
    time.sleep_ms(150)
    await drive(-2,800)
    await moveMotor(30,250,"left")
    await drive(-19,800)
    await drive(16,800)
    await turnLeft(60)
    await drive(65,800)


runloop.run(main())
