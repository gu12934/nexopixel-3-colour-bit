strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
redAmount = 0
greenAmount = 0
blueAmount = 0

def on_forever():
    strip.rotate(1)
    strip.show()
basic.forever(on_forever)

def on_forever2():
    global redAmount, greenAmount, blueAmount
    strip.show_color(neopixel.rgb(redAmount, greenAmount, blueAmount))
    if input.button_is_pressed(Button.B):
        redAmount += 1
    if input.button_is_pressed(Button.A):
        greenAmount += 1
    if input.is_gesture(Gesture.SHAKE):
        blueAmount += 1
basic.forever(on_forever2)
