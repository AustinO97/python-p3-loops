#!/usr/bin/env python3

def happy_new_year():
    i = 11
    while i > 1:
        i -= 1
        print(i)
        if i <= 1:
            print('Happy New Year!')


def square_integers(int_list):
    int_list = [i * i for i in int_list]
    return int_list

def fizzbuzz():
    i = 1
    while i < 101:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
        i += 1