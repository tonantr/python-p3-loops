#!/usr/bin/env python3

# i = 0
# while i < 5:
#   print("Looping!")
#   i += 1

# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)

# List comprehensions allow us to transform sequences of data in
# a single line. Here's how we would accomplish the above task with
# a list comprehension

# inch_heights = [height * 7920 for height in player_heights]


def happy_new_year():
    # code goes here!
    counting_down = 10
    while counting_down > 0:
        print(counting_down)
        counting_down -= 1

    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    square_integers = list()
    for i in int_list:
        square_integers.append(i**2)

    return square_integers


def fizzbuzz():
    # code goes here!
    # num = 1
    # while num < 101:
    #     if num % 3 == 0 and num % 5 == 0:
    #         print('FizzBuzz')
    #     elif num % 3 == 0:
    #         print('Fizz')
    #     elif num % 5 == 0:
    #         print('Buzz')
    #     else:
    #         print(num)
        
    #     num += 1

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
