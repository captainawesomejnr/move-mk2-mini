/**
 * KITRONIK :MOVE NEEDED
 */
input.onLogoEvent(TouchButtonEvent.LongPressed, function () {
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 180)
})
input.onButtonPressed(Button.A, function () {
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 90)
})
input.onSound(DetectedSound.Loud, function () {
    pins.servoWritePin(AnalogPin.P1, 90)
    pins.servoWritePin(AnalogPin.P2, 90)
    control.reset()
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        pins.servoWritePin(AnalogPin.P1, 0)
        pins.servoWritePin(AnalogPin.P2, 0)
        basic.pause(5000)
        pins.servoWritePin(AnalogPin.P1, 180)
        pins.servoWritePin(AnalogPin.P2, 180)
    }
})
input.onButtonPressed(Button.B, function () {
    pins.servoWritePin(AnalogPin.P1, 180)
    pins.servoWritePin(AnalogPin.P2, 0)
})
input.onGesture(Gesture.Shake, function () {
    PixelArray.clear()
    basic.showString("POLICE!")
    PixelArray.range(0, 2).showColor(neopixel.colors(NeoPixelColors.Red))
    PixelArray.setPixelColor(2, neopixel.colors(NeoPixelColors.White))
    PixelArray.range(3, 2).showColor(neopixel.colors(NeoPixelColors.Blue))
    for (let index = 0; index < 4; index++) {
        pins.servoWritePin(AnalogPin.P1, 0)
        pins.servoWritePin(AnalogPin.P2, 0)
        basic.pause(5000)
        pins.servoWritePin(AnalogPin.P1, 180)
        pins.servoWritePin(AnalogPin.P2, 180)
    }
})
let PixelArray: neopixel.Strip = null
PixelArray = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
PixelArray.range(0, 2).showColor(neopixel.colors(NeoPixelColors.Red))
PixelArray.setPixelColor(2, neopixel.colors(NeoPixelColors.Green))
PixelArray.range(3, 2).showColor(neopixel.colors(NeoPixelColors.Blue))
basic.showString(":MovePixels for Micro:bit V2 & Kitronik :MOVE mini Mk2")
basic.clearScreen()
basic.showString("Extension by AdaFruit")
for (let index = 0; index < 4; index++) {
    PixelArray.showColor(neopixel.colors(NeoPixelColors.Red))
    basic.pause(1000)
    PixelArray.showColor(neopixel.colors(NeoPixelColors.Green))
    basic.pause(1000)
    PixelArray.showColor(neopixel.colors(NeoPixelColors.Blue))
    basic.pause(1000)
}
PixelArray.showRainbow(1, 330)
basic.forever(function () {
    input.setSoundThreshold(SoundThreshold.Loud, 128)
    PixelArray.setBrightness(10)
    radio.setGroup(8.456)
})
