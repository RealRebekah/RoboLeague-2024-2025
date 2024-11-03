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
    # write your code here
    # drive forward
    # await drive(90,1000)
    await drive(-85,800)
    await turnLeft(47)
    await drive(10,800)

    await moveMotor(-200,max_speed,"left")
    time.sleep_ms(500)
    await moveMotor(150,200,"left")
    time.sleep_ms(200)
    ################### MODULE 3 #########################
    await turnRight(29)
    await drive(4,700)
    await turnRight(32)
    await drive(-7,700)
    await moveMotor(250, 1000, "left")
    time.sleep_ms(100)
    await moveMotor(-200,700, "left")
    time.sleep_ms(1000)
    await moveMotor(175,1000,"left")
    await drive(7,700)
    await turnRight(72)
    await drive(18,700)
    # MIGHT NOT WORK
    await drive(-3,800)
    await turnRight(35)
    await drive(-19,900)
    await turnLeft(27)
    await drive(22,800)
    await moveMotor(-200,400,"left")
    time.sleep_ms(500)
    await drive(-8,700)
    time.sleep_ms(300)
    await moveMotor(200,300,"left")
    time.sleep_ms(500)
    await drive(-18,900)
    await drive(10,700)
    await turnRight(100)
    await drive(-50,1050)


    # ################## MODULE 6 ###########################
#    time.sleep_ms(200)
#    await moveMotor(10,1000,"left")
#    await drive(-40,max_speed)
#    await turnRight(45)
#    await drive(-5,700)
#    await drive(-2,700)
#    await moveMotor(-300,1000,"left")
#    await drive(10,max_speed)
#    await moveMotor(100,1000,"left")

runloop.run(main())
