# Initialize variables.
distance = 0
X = 0
seconds = 0
# Step 2.

def on_forever():
    global X
    if X == 1:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(1500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 50)
        basic.pause(500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(2000)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 50)
        basic.pause(500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(1500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 50)
        basic.pause(1000)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(2000)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_LEFT, 50)
        basic.pause(300)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(2000)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 50)
        basic.pause(1500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 50)
        basic.pause(500)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
        basic.pause(1000)
        X += 1
basic.forever(on_forever)

# Step 1. 

def on_forever2():
    global X
    if X == 0:
        basic.show_leds("""
            # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # . . .
                        # . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # . .
                        # # . . .
                        # . . . .
                        . . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # .
                        # # # . .
                        # # . . .
                        # . . . .
                        . . . . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # .
                        # # # . .
                        # # . . .
                        # . . . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # .
                        # # # . .
                        # # . . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # .
                        # # # . .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # .
        """)
        basic.show_leds("""
            # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
                        # # # # #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . #
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
        X += 1
basic.forever(on_forever2)

# Step 5. 

def on_forever3():
    global distance, X
    if X == 4:
        distance = Tinybit.Ultrasonic_Car()
        if distance < 30:
            Tinybit.RGB_Car_Big(Tinybit.enColor.RED)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RIGHT, 50)
            basic.pause(500)
            Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
            X += 1
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_STOP, 0)
basic.forever(on_forever3)

# Step 6.

def on_forever4():
    global X
    if X == 5:
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        basic.show_icon(IconNames.HAPPY)
        Tinybit.RGB_Car_Big(Tinybit.enColor.RED)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.WHITE)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.GREEN)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.BLUE)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.PINKISH)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.YELLOW)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.PINKISH)
        basic.pause(100)
        X += 1
basic.forever(on_forever4)

# Step 3. 

def on_forever5():
    global X
    if X == 2:
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_melody("F A B D B F G C5 ", 120)
        X += 1
basic.forever(on_forever5)

# Step 7.

def on_forever6():
    global seconds
    while X != 6:
        seconds += 1
        basic.pause(1000)
basic.forever(on_forever6)

# Step 4. 

def on_forever7():
    global X
    if X == 3:
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINLEFT, 100)
        basic.pause(5000)
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_SPINRIGHT, 100)
        basic.pause(5000)
        X += 1
        Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 50)
basic.forever(on_forever7)

# Step 7.

def on_forever8():
    if X == 6:
        Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
        if Tinybit.Voice_Sensor() > 160:
            basic.show_string("Seconds from Start:")
            basic.show_number(seconds)
basic.forever(on_forever8)
