"""For a detailed guide on all the features of the Circuit Playground Express (cpx) library:
https://adafru.it/cp-made-easy-on-cpx"""
import time
import microcontroller
from adafruit_circuitplayground.express import cpx

# Set this as a float from 0 to 1 to change the brightness. The decimal represents a percentage.
# So, 0.3 means 30% brightness!
cpx.pixels.brightness = 0.3

# Changes to NeoPixel state will not happen without explicitly calling show()
cpx.pixels.auto_write = False

# Light Saber colors:  light blue, Green, Red !
saber_colors = ( (0, 0, 0), (0, 121, 255), (58, 238, 49), (204, 0, 0) )
blade_on = False

while True:

    # Press the buttons to play sounds!
    if cpx.button_a:

        if blade_on == False:

            color_index = 1

            #cpx.pixels.fill(saber_colors[color_index])

            cpx.pixels[9] = saber_colors[color_index]
            cpx.pixels[0] = saber_colors[color_index]
            time.sleep(0.1)
            cpx.pixels.show()

            cpx.pixels[8] = saber_colors[color_index]
            cpx.pixels[1] = saber_colors[color_index]
            time.sleep(0.1)
            cpx.pixels.show()

            cpx.pixels[7] = saber_colors[color_index]
            cpx.pixels[2] = saber_colors[color_index]
            time.sleep(0.1)
            cpx.pixels.show()

            cpx.pixels[6] = saber_colors[color_index]
            cpx.pixels[3] = saber_colors[color_index]
            time.sleep(0.1)
            cpx.pixels.show()

            cpx.pixels[5] = saber_colors[color_index]
            cpx.pixels[4] = saber_colors[color_index]
            time.sleep(0.1)
            cpx.pixels.show()

            cpx.play_file("cool_saber.wav")

            blade_on = True

        else:

            blade_on = False

            color_index = 0

            cpx.pixels.fill( saber_colors[color_index] )
            cpx.pixels.show()

    elif cpx.button_b:

        if color_index < (len(saber_colors) - 1):
            color_index += 1

        else:
            color_index = 0
            blade_on = False

        cpx.pixels.fill( saber_colors[color_index] )
        cpx.pixels.show()

    if cpx.shake(20) and blade_on:
        cpx.play_file("saber_swing.wav")
    
    cpx.detect_taps = 2
    if cpx.tapped and blade_on == False:
        cpx.play_file("happy_three_chirp.wav")


