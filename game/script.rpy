# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    $ chapter = 1
    call ch1

    $ chapter = 2
    call ch2

    $ chapter = 3
    call ch3

    $ chapter = 4
    call ch4

    $ chapter = 5
    call ch5

    $ chapter = 6
    call ch6

    $ chapter = 7
    call ch7

    $ chapter = 8
    call ch8

    $ chapter = 9
    call chEpilogue

    # This ends the game.
    return
