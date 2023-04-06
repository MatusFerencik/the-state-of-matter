atmos_temperature = 0
temperature = 0

def on_gesture_shake():
    global temperature
    temperature += 10
    basic.show_icon(IconNames.TRIANGLE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global temperature
    if temperature < atmos_temperature:
        temperature += -7
    else:
        temperature += -30
    if temperature < 0:
        basic.show_icon(IconNames.SQUARE)
    elif temperature < 100:
        basic.show_icon(IconNames.UMBRELLA)
    else:
        basic.show_icon(IconNames.CHESSBOARD)
    basic.clear_screen()
    basic.pause(100)
basic.forever(on_forever)

def on_pin_pressed_p0():
    global atmos_temperature
    atmos_temperature = 120
    basic.show_string('GAS')
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_pin_pressed_p1():
    global atmos_temperature
    atmos_temperature = 25
    basic.show_string('LIQUID')
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_pin_pressed_p2():
    global atmos_temperature
    atmos_temperature = -20
    basic.show_string('SOLID')
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

atmos_temperature = 40
temperature = 40