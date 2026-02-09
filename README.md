
# *Asteroids* with Pygame

In this project, you will create a simple arcade-style game inspired by **Asteroids**. The player controls a spaceship that can rotate, move, and shoot bullets to destroy asteroids. If the ship crashes into an asteroid, the game ends.




Step 1: Create the Spaceship Class

Your spaceship should:

* Start in the center of the screen
* Have a position, velocity, and angle
* Rotate left and right using keyboard input
* Accelerate in the direction it is facing
* Wrap around the screen when it exits

**Hints**

* Use `pygame.Vector2` for position and velocity
* Use rotation math to move the ship forward
* Draw the ship as a **triangle**

**Checkpoint**

* You can rotate and move the ship smoothly around the screen

---

## Step 2: Create the Bullet Class

Bullets should:

* Spawn at the ship’s position
* Move in the direction the ship is facing
* Travel at a constant speed
* Disappear when they leave the screen

**Controls**

* Press **SPACE** to fire a bullet

**Hints**

* Bullets do *not* need screen wrapping
* Store bullets in a list

**Checkpoint**

* Bullets fire in the correct direction and disappear off-screen

---

## Step 3: Create the Asteroid Class

Asteroids should:

* Spawn at random locations
* Avoid spawning directly on top of the ship
* Move slowly in a random direction
* Wrap around the screen
* Be drawn as circles


**Checkpoint**

* Multiple asteroids drift across the screen endlessly

---

## Step 4: Collision Detection

Add collision logic:

* **Ship vs Asteroid** → Game Over
* **Bullet vs Asteroid**

  * Bullet disappears
  * Asteroid disappears
  * Large asteroids split into smaller ones

**Hints**

* Use distance between centers for collision detection
* Compare distance to the sum of object radii

**Checkpoint**

* Asteroids break apart when shot
* Crashing ends the game

---

## Step 6: Game Over and Restart

When the game ends:

* Display a **GAME OVER** message
* Allow the player to restart by pressing **R**

**Checkpoint**

* Game cleanly restarts without closing the program

---

## Step 6: Main Game Loop

Your main loop should:

1. Handle events (quit, key presses)
2. Process continuous movement input
3. Update all game objects
4. Check for collisions
5. Draw everything
6. Control frame rate (≈ 60 FPS)




