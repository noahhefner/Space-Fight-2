# Noah Hefner
# Space Fight 2.0
# Game Class
# Last Edit: 1/2/2017

class Game(object):
    """ Holds code regarding in-game elements. """

    def __init__(self, settings):
        """ Initiates game class.

        Args:
            settings (list): list of settings from menu [type_player_string,
            type_bullet_string, player_speed]
        """

        self.bullets_left = 100
        self.score = 0
        self.lives = 3
        self.paused = False
        self.type_player_string = settings[0]
        self.type_bullet_string = settings[1]
        self.player = Player(self.type_player_string)
        self.time = time.clock()

        self.bullets = pygame.sprite.LayeredUpdates([pygame.sprite.Group])
        self.aliens = pygame.sprite.LayeredUpdates([pygame.sprite.Group])

    def game_logic(self):
        """ Handles game logic. """

        if not self.paused:

            # First, lets update everything
            self.player.update()
            self.bullets.update()
            self.aliens.update()

            # Then see what happened
            alien_bullet_collision = pygame.groupcollide(self.aliens, self.bullets,
            False, True)

            for alien in alien_bullet_collision:

                    explosion = explosion(alien.rect.x, alien.rect.y)
                    self.score += 1

                    if alien.drop <= 3:

                        drop = Drop(alien)

            alien_player_collision = pygame.spritecollide(self.player, self.aliens,
            False)

            for alien in alien_player_collision:

                explosion = Explosion(alien.rect.x, alien.rect.y)
                self.lives -= 1

            # TODO: spawn aliens on increasingly fast time-based interval

    def spawn_bullet(self):
        """ Spawns a bullet if there are bullets left. """

        bullet = Bullet(self.type_bullet_string)
        bullet.set_vel()
        game.bullets.add(bullet)
        game.bullets_left -= 1

    def process_user_events(self):
        """ Process user imput. """

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and
            self.bullets_left > 0:

                spawn_bullet()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_w:

                    self.player.change_speed(0, -1 * self.player.speed)

                elif event.key == pygame.K_a:

                    self.player.change_speed(-1 * self.player.speed, 0)

                elif event.key == pygame.K_s:

                    self.player.change_speed(0, self.player.speed)

                elif event.key == pygame.K_d:

                    self.player.change_speed(self.player.speed, 0)

                elif event.key == pygame.K_ESC:

                    self.paused = True

                else:

                    pass

    def display_frame(self, surface):
        """ Draw the appropriate sprites for the current screen. """

        for alien in self.aliens:

            Functions.draw_sprite(alien, surface)

        for bullet in self.bullets:

            Functions.draw_sprite(bullet, surface)

        Functions.draw_sprite(self.player, surface)