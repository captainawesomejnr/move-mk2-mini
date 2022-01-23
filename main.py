PixelArray: neopixel.Strip = None
"""

KITRONIK :MOVE NEEDED

"""

def on_logo_long_pressed():
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 180)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def on_button_pressed_a():
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)
    control.reset()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_ab():
    for index in range(4):
        pins.servo_write_pin(AnalogPin.P1, 0)
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(5000)
        pins.servo_write_pin(AnalogPin.P1, 180)
        pins.servo_write_pin(AnalogPin.P2, 180)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    PixelArray.clear()
    basic.show_string("POLICE!")
    PixelArray.range(0, 2).show_color(neopixel.colors(NeoPixelColors.RED))
    PixelArray.set_pixel_color(2, neopixel.colors(NeoPixelColors.WHITE))
    PixelArray.range(3, 2).show_color(neopixel.colors(NeoPixelColors.BLUE))
    for index2 in range(4):
        pins.servo_write_pin(AnalogPin.P1, 0)
        pins.servo_write_pin(AnalogPin.P2, 0)
        basic.pause(5000)
        pins.servo_write_pin(AnalogPin.P1, 180)
        pins.servo_write_pin(AnalogPin.P2, 180)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    PixelArray.range(0, 2).show_color(neopixel.colors(NeoPixelColors.RED))
    PixelArray.set_pixel_color(2, neopixel.colors(NeoPixelColors.GREEN))
    PixelArray.range(3, 2).show_color(neopixel.colors(NeoPixelColors.BLUE))
    basic.show_string(":MovePixels for Micro:bit V2 & Kitronik :MOVE mini Mk2")
    basic.clear_screen()
    basic.show_string("Extension by AdaFruit")
    for index3 in range(4):
        PixelArray.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(1000)
        PixelArray.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(1000)
        PixelArray.show_color(neopixel.colors(NeoPixelColors.BLUE))
        basic.pause(1000)
    PixelArray.show_rainbow(1, 330)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    global PixelArray
    input.set_sound_threshold(SoundThreshold.LOUD, 128)
    PixelArray = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
    PixelArray.set_brightness(10)
    radio.set_group(8.456)
basic.forever(on_forever)
