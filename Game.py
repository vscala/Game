#!/usr/bin/env python3
"""
A text based shooter game (not really)
"""
#import msvcrt
#import Player
import tcod as libtcod

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    screen_width = 80
    screen_height = 50

	player_x = int(screen_width / 2)
	player_y = int(screen_width / 2)

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

    libtcod.console_init_root(screen_width, screen_height, 'The Game that is Played', False)

	key = libtcod.Key()
	mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush()

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            player_x += dx
            player_y += dy
			        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == '__main__':
    main()