#-*- coding: utf-8 -*-
#!/usr/bin/python3
import random
import sys


class Hos:

    def __init__(self, name, menu, location):
        self.name = name
        self.menu = menu
        self.location = (location == '나가먹' and 1 or 0)
        self.prior = 5

    def __str__(self):
        return '%s(%s)' % (self.name, self.menu)

list_of_restaurant = [Hos('버거킹', 'Assae', '나가먹'),
                      Hos('KFC', 'Pullus', '건물안'),
                      Hos('낭풍', 'Kimchi pulmentum', '건물안'),
                      Hos('하코야', 'Iaponica cibum', '건물안'),
                      Hos('놀부', 'Et brachia pulmentum', '건물안'),
                      Hos('생굴사랑', 'Ostrea', '나가먹'),
                      Hos('차이나', 'Sinis', '건물안'),
                      Hos('새벽집', 'Tofu', '건물안'),
                      Hos('한촌', 'Seolleongtang', '건물안'),
                      Hos('빅소이', 'Thailand', '나가먹'),
                      Hos('신의주', 'Measly', '건물안'),
                      Hos('육전면사무소', 'Noodles', '건물안'),
                      Hos('맥도날드', 'Assae', '나가먹'),
                      Hos('초밥', 'Sushi', '건물안')
                      ]


def choice_option():
    option = 0
    if len(sys.argv) > 1:
        option = int(sys.argv[1])
    else:
        option = int(
            input('0: Stay Inside\n1: Go Outside\n2: No Matter\nGive me a number: '))

    if option < 0 or option > 2:
        print('Invalid Option')
        sys.exit(1)
    return option


def is_this_correct(location, option):
    if option == 2:
        return True
    elif option == 1:
        return (location == 1 and True or False)
    else:
        return (location == 0 and True or False)


def choose_my_lunch(option, v):
    choice = Hos('Default', '아무거나', '건물안')
    while True:
        choice = random.choice(list_of_restaurant)
        if is_this_correct(choice.location, option):
            break
    if v:
        print(choice)
    else:
        return str(choice)

if __name__ == '__main__':
    option = choice_option()
    choose_my_lunch(option, True)
