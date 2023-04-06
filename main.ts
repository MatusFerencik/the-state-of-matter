let atmos_temperature = 0
let temperature = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    temperature += 10
    basic.showIcon(IconNames.Triangle)
})
basic.forever(function on_forever() {
    
    if (temperature < atmos_temperature) {
        temperature += -7
    } else {
        temperature += -30
    }
    
    if (temperature < 0) {
        basic.showIcon(IconNames.Square)
    } else if (temperature < 100) {
        basic.showIcon(IconNames.Umbrella)
    } else {
        basic.showIcon(IconNames.Chessboard)
    }
    
    basic.clearScreen()
    basic.pause(100)
})
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    atmos_temperature = 120
    basic.showString("GAS")
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    atmos_temperature = 25
    basic.showString("LIQUID")
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    atmos_temperature = -20
    basic.showString("SOLID")
})
atmos_temperature = 40
temperature = 40
