'''
    title - FeramtsNearMisses
    filename - main.py
    external file - NONE
    list of file program creates - NONE
    programmer name - Archana Pogaku
    email - archanapogaku@lewisu.edu
    course number - CPSC-60050-001
    section number - SU22
    finished date - 08-01-2023
    submitted date - 09-01-2023

    program overview -
        - for this program python language has been chosen as it handles big integer by
          storing its digits in an array. so it doesnt have any overflow problems
          until we have enough memory. but the upper limit of k is limited to 2000 as it takes too long
          for the program to execute when k is greater 2000.
        - the program starts by taking inputs of n, k with the mentioned constraints.
        - this has two loops each to iterate x and y values till k for generating possible x and y combinatons.
        - there is a function caclulate_near_miss which calculates near miss and relative miss
          from the given x, y, n parameters.
        - for every minimum relative miss found, program prints x, y, z, miss, relative miss to terminal.

    resources -
        - https://datatofish.com/executable-pyinstaller/
          referred this docs to generate exe file from python file
          `pyinstaller --onefile main.py` command for generation of exe file


'''



import math


def calculate_near_miss(x, y, n):
    '''

    :param x: holds x value from outer for loop
    :param y: holds y value from inner for loop
    :param n: holds degree given by user
    :return: nearest z value, miss value and relative miss value

    this function takes x, y, n as input and calculates the nearest z value such that
    x^n + y^n = z^n + d
    where d is the miss value and z is such that d is very minimum
    '''

    sum = x**n + y**n

    # from fermats theorem (x^n + y^n)^(1/n) = z and z is a float value and never an integer
    # r holds the float value
    r = sum ** (1.0/n)

    # minz and maxz holds the floor and ceil of r. minz and maxz are the two closest integers for r
    minz = math.floor(r)
    maxz = math.ceil(r)

    # here we calculate which of minz^n and maxz^n are closer to sum
    # z holds the value of minz or maxz such that z^n is closest to sum
    # miss holds the minimum error value between sum and minz^n or maxz^n
    if math.floor((maxz ** n) - sum) < math.floor(sum - (minz ** n)):
        miss = math.floor((maxz ** n) - sum)
        z = maxz
    else:
        miss = math.floor(sum - (minz ** n))
        z = minz

    # returning z, miss, miss/z which is relative miss value
    return z, miss, miss/z


if __name__ == "__main__":
    n = int(input("enter n value (2 < n < 12): "))

    # minMiss is set to highest possible value
    minMiss = math.inf

    if 2 < n < 12:
        k = int(input("enter k value ( 10 < k < 2000): "))
        if 10 < k <= 2000:

            # two loops to generate all the possible the combination of x and y values
            for x in range(10, k+1):
                for y in range(10, k+1):
                    z, miss, rel_miss = calculate_near_miss(x, y, n)
                    if rel_miss < minMiss:
                        print(f"x = {x}  |  y = {y}  |  z = {z}  |  miss = {miss}  |  relative miss = {rel_miss}")
                        print("-"*100)
                        minMiss = rel_miss
        else:
            print("invalid k value ")
    else:
        print("invalid n value")

    ex = input("press any key to exit: ")
