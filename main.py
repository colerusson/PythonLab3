import argparse
import numpy
import os
import math


def main(number: int) -> int:
    # Write the code to sum up cubed numbers here.
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    output = 0
    starting_val = number
    for i in range(starting_val):
        cubed_val = i**3
        while cubed_val > 10:
            cubed_val = cubed_val // 10
        if cubed_val % 2 == 0:
            output += cubed_val

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    result = main(arguments.n)
    print('cube(' + str(arguments.n) + ') = ' + str(result))
