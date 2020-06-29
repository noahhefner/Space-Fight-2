import pygame
from button import Button
from menu_manager import MenuManager
from page import Page
from settings import settings
from strings import image_paths

pygame.init()

def print_yee_haw ():

    print("yee haw!")

def add_one ():

    settings["random_value"] += 1
    print(str(settings["random_value"]))

"""
Use bottom-up approach to build the menu system. Start with buttons, then make
the pages, then add the pages to a menu manager.
"""

man = MenuManager()

test_page = Page("home")
page2 = Page("not_home")

test_button = Button(image_paths["coin"], man.navigate, "not_home", pos = [0,0])
button2 = Button(image_paths["heart"], man.navigate, "home", pos = [0,0])

test_page.add_element(test_button)
page2.add_element(button2)

man.add_page(test_page)
man.add_page(page2)

man.set_start_page(test_page)

running = True

while running:

    running = man.update()
    man.display()
