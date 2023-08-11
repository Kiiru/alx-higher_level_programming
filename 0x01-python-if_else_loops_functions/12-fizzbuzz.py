#!/usr/bin/python3

def fizzbuzz():
    string = ''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            string += "FizzBuzz "
        elif i % 3 == 0:
            string += "Fizz "
        elif i % 5 == 0:
            string += "Buzz "
        else:
            string += "{:d} ".format(i)
    print(string, end='')
