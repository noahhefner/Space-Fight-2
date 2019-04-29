
sf_menus = PageManager()

page_home = MenuPage("HOME")
# Home buttons
button_play = TextButton("PLAY", "GAME")
button_settings = TextButton("UPGRADES", "UPGRADES")
button_highscores = TextButton("HIGHSCORES", "HIGHSCORES")
button_quit = TextButton("QUIT", "QUIT")

page_home.add_text_button(button_play)
page_home.add_text_button(button_upgrades)
page_home.add_text_button(button_highscores)
page_home.add_text_button(button_quit)

page_upgrades = MenuPage("UPGRADES")
# Upgrades buttons
button_speed = TextButton("+SPEED (-10 Coins)", None)
button_ammo = TextButton("+AMMO (-20 Coins)", None)
button_lives = TextButton("+LIFE (-30 Coins)", None)
button_back = TextButton("BACK", "HOME")

page_upgrades.add_text_button(button_speed)
page_upgrades.add_text_button(button_ammo)
page_upgrades.add_text_button(button_lives)
page_upgrades.add_text_button(button_back)

page_highscores = MenuPage("HIGHSCORES")
# Highscores buttons
button_back = TextButton("BACK", "HOME")
# Read highscores from text file and use a loop to create ten buttons with Args
# name as the persons name and None as the to_page. Use another loop to add
# the buttons to the page.
page_highscores.add_text_button(button_back)

sf_menus.add_menu_page(page_home)
sf_menus.add_menu_page(page_upgrades)
sf_menus.add_menu_page(page_highscores)

sf_menus.update()
sf_menus.display(screen)
