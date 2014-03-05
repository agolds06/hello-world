Battlecruiser.py

Contains the module for the Battlecruiser sprite. The update function uses the array of buttons to check which direction the sprite should be moving in.

Enemy.py

Normal sprite class. When this module is run, it produces 10 enemy sprites that bounce off the walls.

game.py

Main game loop. Contains functions for handling collision of sprites with each other and end game scenario. Buttons are handled in a boolean array, which enables the user to hold down the button for input. Lasers have an internal cooldown time, so SPACE cannot just spam unlimited lasers. Enemies are added if the enemy sprite array is empty, or every 200 cycles. Lasers are fired 2 at a time from the Battlecruiser's guns. Game over if background stops scrolling or if ship is hit by enemy. Enemies only spawn on top half of screen, so a sprite cannot just appear where the ship is.

Laser.py

Normal sprite module. Also has methods for checking if a laser is off the screen, and if it hits an enemy sprite. In the latter case, the image changes to an explosion and lingers for a few frames.

Scroller.py

Module for the scrolling background. Updates every frame and alerts game loop when it reaches the end of the image.
