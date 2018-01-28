from getch import getch
import wiringpi as wp

motor_1_speed = 29
motor_1_dir = 28
motor_1_brake = 27

motor_2_speed = 5
motor_2_dir = 26
motor_2_brake = 6

motor_3_speed = 4
motor_3_dir = 1
motor_3_brake = 25

motor_4_speed = 24
motor_4_dir = 23
motor_4_brake = 22

wp.wiringPiSetup()

wp.pinMode(motor_1_speed,1)
wp.pinMode(motor_1_dir,1)
wp.pinMode(motor_1_brake,1)

wp.pinMode(motor_2_speed,1)
wp.pinMode(motor_2_dir,1)
wp.pinMode(motor_2_brake,1)

wp.pinMode(motor_3_speed,1)
wp.pinMode(motor_3_dir,1)
wp.pinMode(motor_3_brake,1)

wp.pinMode(motor_4_speed,1)
wp.pinMode(motor_4_dir,1)
wp.pinMode(motor_4_brake,1)

wp.softPwmCreate(motor_1_speed,100,100)
wp.digitalWrite(motor_1_dir,1)
wp.digitalWrite(motor_1_brake,1)

wp.softPwmCreate(motor_2_speed,100,100)
wp.digitalWrite(motor_2_dir,1)
wp.digitalWrite(motor_2_brake,1)

wp.softPwmCreate(motor_3_speed,100,100)
wp.digitalWrite(motor_3_dir,1)
wp.digitalWrite(motor_3_brake,1)

wp.softPwmCreate(motor_4_speed,100,100)
wp.digitalWrite(motor_4_dir,1)
wp.digitalWrite(motor_4_brake,1)

def forward():
	wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_1_brake,0)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_2_brake,0)

def backward():
	wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_1_dir,0)
    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_2_dir,0)
    wp.digitalWrite(motor_2_brake,1)

def right():
	wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_3_brake,0)
    wp.digitalWrite(motor_4_dir,1)
    wp.digitalWrite(motor_4_brake,0)

def left():
	wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,0)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_4_dir,0)
    wp.digitalWrite(motor_4_brake,1)

def turn_right():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_3_brake,0)
    wp.digitalWrite(motor_4_dir,0)
    wp.digitalWrite(motor_4_brake,1)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_1_brake,0)
    wp.digitalWrite(motor_2_dir,0)
    wp.digitalWrite(motor_2_brake,1)

def turn_left():
    wp.softPwmWrite(motor_1_speed,100)
    wp.softPwmWrite(motor_2_speed,100)
    wp.softPwmWrite(motor_3_speed,100)
    wp.softPwmWrite(motor_4_speed,100)
    wp.digitalWrite(motor_3_dir,0)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_4_dir,1)
    wp.digitalWrite(motor_4_brake,0)
    wp.digitalWrite(motor_1_dir,0)
    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_2_brake,0)

def reset():
    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_2_brake,1)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_4_brake,1)
    wp.digitalWrite(motor_4_dir,1)