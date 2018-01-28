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

current_cmd = -1

while True:
    current_cmd = getch()

    if current_cmd == 'w':
        wp.softPwmWrite(motor_1_speed,100)
        wp.softPwmWrite(motor_2_speed,100)
        wp.softPwmWrite(motor_3_speed,100)
        wp.softPwmWrite(motor_4_speed,100)
        wp.digitalWrite(motor_1_dir,1)
        wp.digitalWrite(motor_1_brake,0)
        wp.digitalWrite(motor_2_dir,1)
        wp.digitalWrite(motor_2_brake,0)
    if current_cmd == 's':
        wp.softPwmWrite(motor_1_speed,100)
        wp.softPwmWrite(motor_2_speed,100)
        wp.softPwmWrite(motor_3_speed,100)
        wp.softPwmWrite(motor_4_speed,100)

        wp.digitalWrite(motor_1_dir,0)
        wp.digitalWrite(motor_1_brake,1)
        wp.digitalWrite(motor_2_dir,0)
        wp.digitalWrite(motor_2_brake,1)
    if current_cmd == 'd':
        wp.softPwmWrite(motor_1_speed,100)
        wp.softPwmWrite(motor_2_speed,100)
        wp.softPwmWrite(motor_3_speed,100)
        wp.softPwmWrite(motor_4_speed,100)

        wp.digitalWrite(motor_3_dir,1)
        wp.digitalWrite(motor_3_brake,0)
        wp.digitalWrite(motor_4_dir,1)
        wp.digitalWrite(motor_4_brake,0)
    if current_cmd == 'a':
        wp.softPwmWrite(motor_1_speed,100)
        wp.softPwmWrite(motor_2_speed,100)
        wp.softPwmWrite(motor_3_speed,100)
        wp.softPwmWrite(motor_4_speed,100)

        wp.digitalWrite(motor_3_dir,0)
        wp.digitalWrite(motor_3_brake,1)
        wp.digitalWrite(motor_4_dir,0)
        wp.digitalWrite(motor_4_brake,1)
    if current_cmd == 'q':
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

    if current_cmd == 'e':
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


    wp.delay(40)

    


    wp.digitalWrite(motor_1_brake,1)
    wp.digitalWrite(motor_1_dir,1)
    wp.digitalWrite(motor_2_brake,1)
    wp.digitalWrite(motor_2_dir,1)
    wp.digitalWrite(motor_3_brake,1)
    wp.digitalWrite(motor_3_dir,1)
    wp.digitalWrite(motor_4_brake,1)
    wp.digitalWrite(motor_4_dir,1)
