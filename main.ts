let X = 0
let distance = 0
let seconds = 0
// Step 2.
basic.forever(function () {
    if (X == 1) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(1500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Right, 50)
        basic.pause(500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(2000)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Left, 50)
        basic.pause(500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(1500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Left, 50)
        basic.pause(1000)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(2000)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Left, 50)
        basic.pause(300)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(2000)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Right, 50)
        basic.pause(1500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Right, 50)
        basic.pause(500)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
        basic.pause(1000)
        X += 1
    }
})
// Step 1.
basic.forever(function () {
    if (X == 0) {
        basic.showLeds(`
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # . .
            # # . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # # .
            # # # . .
            # # . . .
            # . . . .
            . . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # .
            # # # . .
            # # . . .
            # . . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # .
            # # # . .
            # # . . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # .
            # # # . .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # .
            `)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        X += 1
    }
})
// Step 6.
basic.forever(function () {
    if (X == 5) {
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        basic.showIcon(IconNames.Happy)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.White)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Green)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Blue)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Pinkish)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Yellow)
        basic.pause(100)
        Tinybit.RGB_Car_Big(Tinybit.enColor.Pinkish)
        basic.pause(100)
        X += 1
    }
})
// Step 5.
basic.forever(function () {
    if (X == 4) {
        distance = Tinybit.Ultrasonic_Car()
        if (distance < 30) {
            Tinybit.RGB_Car_Big(Tinybit.enColor.Red)
            Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Right, 50)
            basic.pause(500)
            Tinybit.RGB_Car_Big(Tinybit.enColor.OFF)
            Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
            X += 1
            Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Stop, 0)
        }
    }
})
// Step 3.
basic.forever(function () {
    if (X == 2) {
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.playMelody("F A B D B F G C5 ", 120)
        X += 1
    }
})
// Step 7.
basic.forever(function () {
    if (X == 6) {
        Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
        if (Tinybit.Voice_Sensor() > 160) {
            basic.showString("Seconds from Start:")
            basic.showNumber(seconds)
        }
    }
})
// Step 4.
basic.forever(function () {
    if (X == 3) {
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinLeft, 100)
        basic.pause(5000)
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_SpinRight, 100)
        basic.pause(5000)
        X += 1
        Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 50)
    }
})
// Step 7.
basic.forever(function () {
    while (X != 6) {
        seconds += 1
        basic.pause(1000)
    }
})
