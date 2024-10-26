
from hub import light_matrix, motion_sensor, port
import runloop, motor_pair, motor,math,time,runloop, color, color_sensor


async def drive(distance, speed):
    motion_sensor.reset_yaw(0)
    CM = round(distance * 17.5)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, CM, 0, velocity = speed, stop=motor.SMART_COAST)
    motion_sensor.reset_yaw(0)


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
        motor.run_for_degrees(port.F, degrees, speed, stop = motor.HOLD)
    if (side == "right"):
        motor.run_for_degrees(port.B, degrees, speed, stop = motor.HOLD)
apple= 1050

async def main():
    motion_sensor.reset_yaw(0)
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.E)



    await drive(86,500)
    await turnLeft(85)
    await drive(33,400)
    time.sleep_ms(50)
    await drive(50,500)
    await drive(5, 1000)
    await turnRight(20)
    await drive(5, 1000)
    await turnLeft(20)
    await drive(60, 1000)
    await turnLeft(75)
    time.sleep_ms(200)
    await drive(90,400)


runloop.run(main())
