let strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
let redAmount = 0
let greenAmount = 0
let blueAmount = 0
basic.forever(function () {
    strip.rotate(1)
    strip.show()
})
basic.forever(function () {
    strip.showColor(neopixel.rgb(redAmount, greenAmount, blueAmount))
    if (input.buttonIsPressed(Button.B)) {
        redAmount += 1
    }
    if (input.buttonIsPressed(Button.A)) {
        greenAmount += 1
    }
    if (input.isGesture(Gesture.Shake)) {
        blueAmount += 1
    }
})
