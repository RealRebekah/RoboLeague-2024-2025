from hub import light_matrix, motion_sensor, port
import runloop, motor_pair, motor,math,time,runloop, color, color_sensor


async def drive(distance, speed):
    CM = round(distance * 17.5)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, CM, 0, velocity = speed, stop=motor.SMART_COAST)

async def turnLeft(angle):
    while motion_sensor.tilt_angles()[0]<(angle*10): #while the angle sensor is less than desired angle
        motor_pair.move(motor_pair.PAIR_1,-100) #both motors will run -100 degrees
    motor_pair.stop(motor_pair.PAIR_1) #stop the motors after that while loop
    motion_sensor.reset_yaw(0) #reset yaw value

async def turnRight(angle):
    while motion_sensor.tilt_angles()[0]>(angle*-10): #getting yaw value from tuple
        motor_pair.move(motor_pair.PAIR_1,100) #move to right
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
apple=1050;
async def main():
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1,port.D,port.B)


##########################. m9
    await drive(32,apple)
    await turnLeft(45)
    await drive(33,apple)
    time.sleep_ms(250)
    await drive(-23,apple)
    await turnRight(45)
    await drive(50,apple)
    await turnRight(90)
    await moveMotor(175,3000,"right")
    await drive(-25,apple)
############################# end m9

###############################.  m13#####################  
    time.sleep_ms(200)
    await drive(24.5,apple)
    # await moveMotor(-175,apple,"right")
    time.sleep_ms(300)
    await moveMotor(-175,3000,"right")
###############################.m13##############
    time.sleep_ms(300)
##############################.  m14
    await drive(10,apple)
    await turnRight(5)
    time.sleep_ms(200)
    await moveMotor(-130,3000,"left")
    time.sleep_ms(200)
    await drive(-17,apple)
    await turnRight(45)
    await drive(40,apple)
    await turnRight(45)
    await drive(30,apple)
########### end m14#################
    time.sleep_ms(300)
    await moveMotor(130,3000,"left")
    await drive(8,apple)

    

runloop.run(main())
