"""
Noah Hefner
Highscore Saving Methods
Last Edit: 6 July 2020
"""
import os

def get_highscores ():
  """
  Pulls a list of highscores from a text file.

  Returns:
    List (int): List of highscore numbers.
  """

  highscores = list()
  high_score_file = open("highscore_numbers.txt", "r")

  for line in high_score_file:

    line = int(line.strip())
    highscores.append(line)

  high_score_file.close()

  return highscores

def get_names ():
    """
    Pulls a list of names from a text file.

    Returns:
        List (string): List of highscore names.
    """

    names =list()
    name_file = open("highscore_names.txt", "r")

    for line in name_file:

      line = str(line.strip())
      names.append(line)

    name_file.close()

    return names

def is_highscore (score):

    score_file = open(str(os.path.abspath("highscore_numbers.txt")), "r")
    contents = score_file.readlines()

    for i in range(len(contents)):

        if score > int(contents[i]):

            score_file.close()

            return True

    score_file.close()
    return False

def add_highscore (score, name):
    """
    Adds a highscore to the name and score files.
    """

    index = 0

    score_file = open("highscore_numbers.txt", "r")
    contents = score_file.readlines()

    for i in range(len(contents)):

        if score > int(contents[i]):

            break

        index += 1

    contents.insert(index, "\n")
    contents.insert(index, str(score))
    score_file.close()

    score_file = high_score_file = open("highscore_numbers.txt", "w")

    for i in range(len(contents)):

        contents[i] + "\n"

    contents = contents[0:6]

    contents = "".join(contents)

    score_file.write(contents)
    score_file.close()

    name_file = open("highscore_names.txt", "r")
    contents = name_file.readlines()

    contents.insert(index, "\n")
    contents.insert(index, str(name))
    name_file.close()

    name_file = high_score_file = open("highscore_names.txt", "w")

    for i in range(len(contents)):

        contents[i] + "\n"

    contents = contents[0:5]

    contents = "".join(contents)

    name_file.write(contents)
    name_file.close()
