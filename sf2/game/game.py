"""
Noah Hefner
Space Fight 2.0
Game Classes
Last Edit: 7/19/2020
"""

# Imports
import math
import pygame
import random
from sf2.common.constants import BLACK, WHITE
from sf2.common.strings import audio_paths, image_paths
from sf2.common.settings import settings_game, settings_program

# Initialize pygame
pygame.init()

class Alien(pygame.sprite.Sprite):
    """
    In-game alien entity.

    Attributes:
        image (pygame.image): Image for alien sprite.
        rect (pygame.image.rect): Position, height, width values for image.
        drop_carrier (boolean): True if alien is a drop carrier.
        speed (int): Speed multiplier for aliem movement.
    """

    def __init__(self, image_string):
        """
        Instantiate an alien object.

        Parameters:
            image_string (string): Path of image file to be used for alien.
        """

        super(Alien, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.__random_spawn()

        self.drop_carrier = self.__drop_carrier_chance()
        self.speed = settings_game["alien_speed"]

    def update(self, player_center):
        """
        Calculates path towards player and moves alien.

        Parameters:
            player_center (tuple): Coordinates of player object.
        """

        diff_x = player_center[0] - self.rect.center[0]
        diff_y = player_center[1] - self.rect.center[1]

        angle = math.atan2(diff_y, diff_x)

        velx = math.cos(angle) * self.speed
        vely = math.sin(angle) * self.speed

        self.__move(velx, vely)

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

    def is_drop_carrier(self):
        """
        Get boolean of drop_carrier attribute.

        Returns:
            self.drop_carrier (boolean): True for carrier, False for non-carrier.
        """

        return self.drop_carrier

    def __drop_carrier_chance(self):
        """
        Generate True or False given drop probability in settings.

        Returns:
            boolean: True if alien is carrier, False if alien is not a carrier.
        """

        carrier = random.randrange(0, settings_game["drop_probability"])

        if not carrier:

            return True

        else:

            return False

    def __move(self, velx, vely):
        """
        Move the alien according to x and y axis velocities.
        """

        self.rect.x += velx
        self.rect.y += vely

    def __random_spawn(self):
        """
        Generate random spawn point.

        Returns:
            tuple (int): X and Y coordinates for random spawn location.
        """

        position = []
        x = None
        y = None

        left_right = random.randrange(0, 3)

        # Left side of screen
        if left_right == 0:

            x = random.randrange(-600, -100)
            y = random.randrange(-600, settings_program["screen_height"] + 600)

        # Middle portion of screen
        # This one is tricky because we have to avoid spawning the alien in the
        # field of play. We want to ensure we only spawn aliens off-screen.
        elif left_right == 1:

            x = random.randrange(0, settings_program["screen_width"])

            top_bottom = random.randrange(0, 2)

            if top_bottom == 0:

                y = random.randrange(-600, -100)

            else:

                y = random.randrange(settings_program["screen_height"] + 100,
                                     settings_program["screen_height"] + 700)

        # Right side of screen
        else:

            x = random.randrange(settings_program["screen_width"] + 100,
                                 settings_program["screen_width"] + 700)
            y = random.randrange(-600, settings_program["screen_height"] + 600)

        position.append(x)
        position.append(y)

        return position

class AudioPlayer:
    """
    Plays sounds.
    """

    def __init__(self):
        """
        Instantiate a new AudioPlayer object.
        """

    def stop (self):
        """
        End all audio from the mixer.
        """

        pygame.mixer.stop()

    def play_sound (self, audio_file_name, repeat = False):
        """
        Plays an audio clip.

        Arguments:
            audio_file_name: Name of audio file. Must be one of the files in the
                             resources/audio folder.
            repeat: Triggers repeat of the sound (use for theme song).
        """

        sound = pygame.mixer.Sound(audio_paths[audio_file_name])

        if repeat:
            sound.play(-1)
        else:
            sound.play()

class Bullet(pygame.sprite.Sprite):
    """
    In-game bullet entity.

    Attributes:
        image (pygame.image): Image for Bullet sprite.
        rect (pygame.image.rect): Position, height, width values for image.
    """

    def __init__(self, image_string, mouse_pos, player_pos):
        """
        Initiate bullet class.

        Args:
            image_string (string): Image path for bullet image.
            x_traj (int): X axis trajectory of the bullet.
            y_traj (int): Y axis trajectory of the bullet.
        """

        super(Bullet, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0]
        self.rect.y = player_pos[1]
        self.mouse_pos = mouse_pos
        self.speed = int(settings_game["bullet_speed"])
        self.trajectory = self.__calculate_trajectory(mouse_pos, player_pos)

    def update(self):
        """
        Move bullet. Kill bullet when it goes off the screen.
        """

        self.rect.x += self.trajectory[0]
        self.rect.y += self.trajectory[1]

        if self.rect.x + self.rect.width < 0 or \
                self.rect.y + self.rect.height < 0:

            self.kill()

        elif self.rect.y > settings_program["screen_height"] or \
                self.rect.x > settings_program["screen_width"]:

            self.kill()

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

    def __calculate_trajectory(self, mouse_pos, player_pos):
        """
        Calculate the trajectory of the bullet given player/mouse coordinates.

        Parameters:
            mouse_pos (list): X and Y coordinates of the mouse.
            player_pos (list): X and Y coordinates of the player.
        Returns:
            list: X and Y axis trajectories.
        """

        angle = math.atan2(player_pos[1] - mouse_pos[1],
                           player_pos[0] - mouse_pos[0])
        x_traj = math.cos(angle) * (-1 * self.speed)
        y_traj = math.sin(angle) * (-1 * self.speed)

        return [x_traj, y_traj]

class Cursor(pygame.sprite.Sprite):
    """
    Cursor that is blitted in place of the system cursor.

    Attributes:
      image (pygame.image): Image for cursor sprite.
      rect (pygame sprite rect): Rect attributes for sprite image.
    """

    def __init__(self, cursor_image):
        """
        Initialize a Cursor object.

        Parameters:
            image_string (str): Path of image file used for cursor.
        """

        super(Cursor, self).__init__()

        self.image = pygame.image.load(cursor_image).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def update(self, mouse_pos):
        """
        Set center of cursor to the mouse position.
        """

        self.rect.center = (mouse_pos[0], mouse_pos[1])

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

class Drop(pygame.sprite.Sprite):
    """
    Powerups that drop when an alien is killed.

    Attributes:
        image_string (str): Image path for drop image. This is randomly chosen.
        rect (pygame.image.rect): Position, height, width values for image.
        dropped_frames (int): Number of frames that the drop has existed.
    """

    def __init__(self, x_coord, y_coord):

        super(Drop, self).__init__()

        self.image_string = random.choice([image_paths["drop_life"],
                                           image_paths["drop_coin"],
                                           image_paths["drop_bullets"]])
        self.image = pygame.image.load(self.image_string)
        self.rect = self.image.get_rect()
        self.set_x(x_coord)
        self.set_y(y_coord)
        self.dropped_frames = 0

    def update(self):
        """
        Times the drop for dropped_frames. Kills drop at frame limit.
        """

        if self.dropped_frames == int(settings_game["drop_frames"]):

            self.kill()

    def get_type(self):
        """
        Gets the image path of the drop.

        Returns:
            self.image_string (str): Image path of the drop.
        """

        return self.image_string

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

class Explosion(pygame.sprite.Sprite):
    """
    Spawns an explosion at the given location.

    Attributes:
        e1 (pygame.image): Image path for frame 1/5 of the explosion.
        e2 (pygame.image): Image path for frame 2/5 of the explosion.
        e3 (pygame.image): Image path for frame 3/5 of the explosion.
        e4 (pygame.image): Image path for frame 4/5 of the explosion.
        e5 (pygame.image): Image path for frame 5/5 of the explosion.
        image_list (list): A subscriptable list for easily parsing the frames.
        frame (int): The total frames elapsed in the explosion.
        exp_num (int): Index of currently showing frame.
        image (pygame.image): The image object that gets blited by front end.
        rect (pygame.image.rect): Position, height, width values for image.
    """

    def __init__(self, x, y):
        """
        Initializes explosion class.

        Parameters:
            x (int): X value for the explosion to spawn.
            y (int): Y value for the explosion to spawn.
        """

        super(Explosion, self).__init__()

        self.e1 = pygame.image.load(image_paths["e1"]).convert()
        self.e2 = pygame.image.load(image_paths["e2"]).convert()
        self.e3 = pygame.image.load(image_paths["e3"]).convert()
        self.e4 = pygame.image.load(image_paths["e4"]).convert()
        self.e5 = pygame.image.load(image_paths["e5"]).convert()

        self.e1.set_colorkey(BLACK)
        self.e2.set_colorkey(BLACK)
        self.e3.set_colorkey(BLACK)
        self.e4.set_colorkey(BLACK)
        self.e5.set_colorkey(BLACK)

        self.image_list = [self.e1, self.e2, self.e3, self.e4, self.e5]
        self.frame = 0
        self.exp_num = 0

        self.image = self.e1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """
        Cycles through the exp_list to display the correct frame and kills the
        sprite at the frame limit.
        """

        if self.frame == 16:

            self.kill()

        elif self.frame % 4 == 0:

            self.exp_num += 1

        self.frame += 1
        self.image = self.image_list[self.exp_num]

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

class Game:
    """
    Handles all sprite movement, collision detection, score, etc.

    Attributes:
        aliens (pygame.sprite.Group): Sprite group of all aliens.
        bullets (pygame.sprite.Group): Sprite group of all bullets.
        drops (pygame.sprite.Group): Sprite group of all drops.
        explosions (pygame.sprite.Group): Sprite group of all explosions.
        stars (pygame.sprite.Group): Sprite group of all stars.

        cursor (Cursor): The cursor sprite.
        player (Player): The player sprite.

        audio_player (AudioPlayer): Handles all audio for the game.

        coins (int): Number of coins the player has.
        score (int): Current score the player has.
        hud (HUD): Overlay that contains information for the player.
    """

    def __init__(self, screen, clock):
        """
        Initialize a GameBackend object.
        """

        self.screen = screen
        self.clock = clock

        # Sprite Groups
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()

        # Sprites
        self.cursor = Cursor(settings_game["cursor_type_string"])
        self.player = Player(settings_game["player_type_string"])
        for i in range(20):
            new_alien = Alien(image_paths["alien1"])
            self.aliens.add(new_alien)
        for i in range(int(settings_program["screen_width"] / 2)):
            new_star = Star(image_paths["star"])
            self.stars.add(new_star)

        # AudioPlayer
        self.audio_player = AudioPlayer()
        self.audio_player.play_sound("theme", True)

        self.coins = settings_game["coins"]
        self.score = 0
        self.hud = self.HUD(self.score, self.player.bullets, self.coins, self.player.lives)

    def display (self):
        """
        Draw the game to the screen.
        """

        # Fill background
        self.screen.fill(BLACK)

        # Draw stars
        self.stars.draw(self.screen)

        # Draw the HUD
        self.hud.display(self.screen)

        # Draw the bullets
        self.bullets.draw(self.screen)

        # Draw the explosions
        self.explosions.draw(self.screen)

        # Draw the drops
        self.drops.draw(self.screen)

        # Draw the aliens
        self.aliens.draw(self.screen)

        # Draw the player
        self.screen.blit(self.player.image, [self.player.rect.x, self.player.rect.y])

        # Draw the cursor
        self.screen.blit(self.cursor.image, [self.cursor.rect.x, self.cursor.rect.y])

        # Flip screen
        pygame.display.flip()

        # Tick clock
        self.clock.tick(settings_program["fps"])

    def update (self):
        """"
        Handles user input, collision detection, and updates all sprites.

        Parameters:
            user_events (pygame.event): List of user inputs.
        Returns:
            Boolean: True for continue the game, False to end the game.
        """

        self.__update_window_title()
        user_events = pygame.event.get()

        """ ------------------------ Keyboard Input ------------------------ """

        # Handle user input
        for event in user_events:

            if event.type == pygame.QUIT:

                # Kill program
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:

                    self.player.change_speed(0, -1 * settings_game["player_speed"])

                if event.key == pygame.K_a:

                    self.player.change_speed(-1 * settings_game["player_speed"], 0)

                if event.key == pygame.K_s:

                    self.player.change_speed(0, settings_game["player_speed"])

                if event.key == pygame.K_d:

                    self.player.change_speed(settings_game["player_speed"], 0)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_w:

                    self.player.change_speed(0, settings_game["player_speed"])

                if event.key == pygame.K_a:

                    self.player.change_speed(settings_game["player_speed"], 0)

                if event.key == pygame.K_s:

                    self.player.change_speed(0, -1 * settings_game["player_speed"])

                if event.key == pygame.K_d:

                    self.player.change_speed(-1 * settings_game["player_speed"], 0)

            # Fire bullet when user presses left mouse button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                    self.player.bullets > 0:

                self.audio_player.play_sound("bullet_fire")
                self.__spawn_bullet()

        """ ------------------------ Sprite Updates ------------------------ """
        # Explosion update
        for explosion in self.explosions:
            explosion.update()

        # Drop update
        for drop in self.drops:
            drop.update()

        # Bullet update
        for bullet in self.bullets:
            bullet.update()

        # Alien update
        for alien in self.aliens:
            alien.update(self.player.rect.center)

        # Star update
        for star in self.stars:
            star.update()

        self.player.update()
        self.cursor.update(pygame.mouse.get_pos())
        self.hud.update(self.score, self.player.bullets,
                        self.coins, self.player.lives)

        """ --------------------- Collision Detection --------------------- """

        # Bullet-Alien collision
        alien_bullet_collision = \
            pygame.sprite.groupcollide(self.aliens, self.bullets, False, True)

        for alien in alien_bullet_collision:

            self.audio_player.play_sound("explosion")

            # Spawn an explosion and kill the alien sprite
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.score += 1
            alien.kill()

            # Make a new alien to take its place
            self.__update_alien_speed()
            new_alien = Alien(image_paths["alien1"])
            self.aliens.add(new_alien)

            # Spawn a drop if the alien was a carrier
            if alien.is_drop_carrier():

                drop = Drop(alien.get_x(), alien.get_y())
                self.drops.add(drop)

        # Player-Alien collision
        alien_player_collision = \
            pygame.sprite.spritecollide(self.player, self.aliens, True)

        for alien in alien_player_collision:

            self.audio_player.play_sound("hitmarker")

            # Spawn an explosion in that area and subtract one player life
            explosion = Explosion(alien.rect.x, alien.rect.y)
            self.explosions.add(explosion)
            self.player.lives -= 1  # Function this into player class

        # Player-Drop collision
        player_drop_collision = \
            pygame.sprite.spritecollide(self.player, self.drops, True)

        for drop in player_drop_collision:

            # Perform the perks ability/benefit
            if drop.get_type() == image_paths["drop_bullets"]:

                self.audio_player.play_sound("pickup_bullets")
                self.player.bullets += settings_game["drop_bullets"]

            elif drop.get_type() == image_paths["drop_coin"]:

                self.audio_player.play_sound("pickup_coin")
                self.coins += 1

            elif drop.get_type() == image_paths["drop_life"]:

                self.audio_player.play_sound("pickup_life")
                self.player.lives += 1

        # End game if the player is out of lives
        if self.player.lives <= 0:

            self.audio_player.stop()
            return False

        # Return True if the game should continue
        return True

    def get_aliens(self):
        """
        Gets the aliens sprite group.

        Returns:
            self aliens (pygame.sprite.Group): Sprite group of aliens.
        """

        return self.aliens

    def get_bullets(self):
        """
        Gets the bullets sprite group.

        Returns:
            self.bullets (pygame.sprite.Group): Sprite group of bullets.
        """

        return self.bullets

    def get_drops(self):
        """
        Gets the drops sprite group.

        Returns:
            self.drops (pygame.sprite.Group): Sprite group of drops.
        """

        return self.drops

    def get_explosions(self):
        """
        Gets the explosions sprite group.

        Returns:
            self.explosions (pygame.sprite.Group): Sprite group of explosions.
        """

        return self.explosions

    def get_stars(self):
        """
        Gets the stars sprite group.

        Returns:
            self.stars (pygame.sprite.Group): Sprite group of stars.
        """

        return self.stars

    def __spawn_bullet(self):
        """
        Spawns a bullet and adds it to bullet sprite list.
        """

        mouse_pos = pygame.mouse.get_pos()
        new_bullet = Bullet(settings_game["bullet_type_string"], mouse_pos,
                            self.player.rect.center)
        self.bullets.add(new_bullet)
        self.player.bullets -= 1

    def __update_alien_speed(self):
        """
        Increment alien speed based on player score.
        """

        settings_game["alien_speed"] += 0.01

    def __update_window_title (self):
        """
        Update the window title to include current fps count.
        """

        fps = str(int(self.clock.get_fps()))
        pygame.display.set_caption("SPACE FIGHT 2.0 - FPS: " + fps)

    class HUD:
        """
        Visual overlay that contains player information.

        Attributes:
            heart (pygame.sprite.Sprite): Heart sprite used to blit lives.
            counter_score (pygame.sprite.Sprite): Player score counter.
            counter_bullets (pygame.sprite.Sprite): Player bullet counter.
            counter_coins (pygame.sprite.Sprite): Player coins counter.
        """

        def __init__(self, score, bullets, coins, lives):
            """
            Initialize a HUD object.

            Parameters:
                score (int): Current score of player.
                bullets (int): Current bullet count of player.
                coins (int): Current coin count of player.
            """

            self.lives = lives

            self.heart = pygame.sprite.Sprite()
            self.heart.image = \
                pygame.image.load(image_paths["heart"]).convert()
            self.heart.rect = self.heart.image.get_rect()

            self.counter_score = pygame.sprite.Sprite()
            self.counter_score.image = settings_game["font"].render(
                "SCORE    " + str(score), False, WHITE)
            self.counter_score.rect = self.counter_score.image.get_rect()

            self.counter_bullets = pygame.sprite.Sprite()
            self.counter_bullets.image = settings_game["font"].render(
                "BULLETS    " + str(bullets), False, WHITE)
            self.counter_bullets.rect = self.counter_bullets.image.get_rect()

            self.counter_coins = pygame.sprite.Sprite()
            self.counter_coins.image = settings_game["font"].render(
                "COINS    " + str(coins), False, WHITE)
            self.counter_coins.rect = self.counter_coins.image.get_rect()

        def display (self, screen):

            screen.blit(self.counter_bullets.image, [self.counter_bullets.rect.x, self.counter_bullets.rect.y])

            screen.blit(self.counter_score.image, [self.counter_score.rect.x, self.counter_score.rect.y])

            screen.blit(self.counter_coins.image, [self.counter_coins.rect.x, self.counter_coins.rect.y])

            for i in range(self.lives):

                x = (settings_game["hud_spacing"] * (i + 1)) + \
                    (i * self.heart.rect.width)

                y = settings_game["hud_spacing"]

                screen.blit(self.heart.image, [x, y])

        def update(self, score, bullets, coins, lives):
            """
            Remake counter sprites with appropriate data.

            Parameters:
                score (int): Current score of player.
                bullets (int): Current bullet count of player.
                coins (int): Current coin count of player.
                lives (int): Current number of lives remaining.
            """

            # Update number of lives
            self.lives = lives

            # Update bullet counter
            self.counter_bullets.image = settings_game["font"].render(
                "BULLETS    " + str(bullets), False, WHITE)
            self.counter_bullets.rect = self.counter_bullets.image.get_rect()
            self.counter_bullets.rect.x = settings_game["hud_spacing"]
            self.counter_bullets.rect.y = self.heart.rect.y + \
                self.heart.rect.height + (settings_game["hud_spacing"] * 2)

            # Update coin counter
            self.counter_coins.image = settings_game["font"].render(
                "COINS    " + str(coins), False, WHITE)
            self.counter_coins.rect = self.counter_coins.image.get_rect()
            self.counter_coins.rect.x = settings_game["hud_spacing"]
            self.counter_coins.rect.y = self.counter_bullets.rect.y + \
                self.counter_bullets.rect.height + settings_game["hud_spacing"]

            # Update score counter
            self.counter_score.image = settings_game["font"].render(
                "SCORE    " + str(score), False, WHITE)
            self.counter_score.rect = self.counter_score.image.get_rect()
            self.counter_score.rect.x = settings_game["hud_spacing"]
            self.counter_score.rect.y = self.counter_coins.rect.y + \
                self.counter_coins.rect.height + settings_game["hud_spacing"]

class Player(pygame.sprite.Sprite):
    """
    In-game player entity.

    Attributes:
        image (pygame.image): Image for player sprite.
        original (pygame.image): Same as image. Used for rotation.
        rect (pygame.image.rect): Position, height, width values for image.
        bullets (int): Number of bullets the player has.
        lives (int): Number of lives the player has.
        velx (int): Velocity of player on x axis.
        vely (int): Velocity of player on y axis.
    """

    def __init__(self, image_string):
        """
        Instantiate a player object.

        Parameters:
            image_string (string): Path of image file to be used for player.
        """

        super(Player, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey([0, 0, 0])
        self.original = self.image
        self.rect = self.image.get_rect()
        self.velx = 0
        self.vely = 0

        self.bullets = settings_game["start_bullets"]
        self.lives = settings_game["start_lives"]

        # Set starting position for player
        self.set_x(settings_program["screen_width"] / 2)
        self.set_y(settings_program["screen_height"] / 2)

    def update(self):
        """
        Rotate and move player, then check for screen edge collision.
        """

        self.__rotate()
        self.__move()
        self.__check_screen_edge_hit()

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y

    def change_speed(self, velx, vely):
        """
        Change speed of player on x and y axis.

        Parameters:
            velx (int): X axis velocity for player.
            vely (int): Y axis velocity for player.
        """

        self.velx += velx
        self.vely += vely

    def __check_screen_edge_hit(self):
        """
        Prevents the player from moving off the window.
        """

        if self.rect.x + self.rect.width >= settings_program["screen_width"]:
            self.rect.right = settings_program["screen_width"]

        if self.rect.x <= 0:
            self.rect.left = 0

        if self.rect.y <= 0:
            self.rect.top = 0

        if self.rect.y + self.rect.height >= settings_program["screen_height"]:
            self.rect.bottom = settings_program["screen_height"]

    def __move(self):
        """
        Move the player according to x and y axis velocities.
        """

        self.rect.x += self.velx
        self.rect.y += self.vely

    def __rotate(self):
        """
        Rotates the player to face the cursor.
        """

        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        diff_y = self.rect.center[1] - mouse_y
        diff_x = self.rect.center[0] - mouse_x
        angle = math.degrees(math.atan2(-1 * diff_y, diff_x)) - 180
        self.image = pygame.transform.rotate(self.original, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

class Star(pygame.sprite.Sprite):
    """
    Star image used to create background.

    Attributes:
        image (pygame.image): Image for Star sprite.
        rect (pygame sprite rect): Rect attributes for sprite image.
        velyt (int): Y-axis velocity of star.
    """

    def __init__(self, image_string):
        """
        Instantiate a Star object.

        Parameters:
            image_string (string): Path of image file for the star.
        """

        super(Star, self).__init__()

        self.image = pygame.image.load(image_string).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, settings_program["screen_width"])
        self.rect.y = random.randrange(0, settings_program["screen_height"])
        self.vely = random.randrange(-3, 0)

    def update(self):
        """
        Move star, reset position if it goes off the top of the screen.
        """

        self.rect.y += self.vely

        if self.rect.y + self.rect.height < 0:

            self.set_y(settings_program["screen_height"])

    def get_x(self):
        """
        Get x value of rect.

        Returns:
            self.rect.x (int): X value of rect.
        """

        return self.rect.x

    def get_y(self):
        """
        Get y value of rect.

        Returns:
            self.rect.y (int): Y value of rect.
        """

        return self.rect.y

    def set_x(self, new_x):
        """
        Set x value for rect.

        Parameters:
            new_x (int): New x value for rect.
        """

        self.rect.x = new_x

    def set_y(self, new_y):
        """
        Set y value for rect.

        Parameters:
            new_y (int): New y value for rect.
        """

        self.rect.y = new_y
