# The script of the game goes in this file.

#Launch splash screen
label splashscreen:
    scene black
    with Pause(1)

    show splash with dissolve
    with Pause(1.5)

    hide text with dissolve
    with Pause(1)

    return

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ chapter = 1
    call ch1 from _call_ch1

    $ chapter = 2
    call ch2 from _call_ch2

    $ chapter = 3
    call ch3 from _call_ch3

    $ chapter = 4
    call ch4 from _call_ch4

    $ chapter = 5
    call ch5 from _call_ch5

    $ chapter = 8
    call ch8 from _call_ch8

    $ chapter = 9
    call chEpilogue from _call_chEpilogue


    # This ends the game.
    return
