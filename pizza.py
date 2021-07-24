##############################################
# Pizza.py
# Compares sq in per dollar of a pizza deal
# 
# Inputs - Price and size of 'za
# Outputs - Square inches per dollar of input 'za
#
# Schwarz <Schwarzyz@gmail.com>
# 
##############################################

import argparse
import math

def main():
    # Arg parser 
    parser = argparse.ArgumentParser(description='Determine sq in per dollar of pizza')

    # Arg -n decreases 'za radius by 1, essentially subtracting the portion of the 'za that is crust
    parser.add_argument('-n', '--nocrust', action='store_const', const=True, default=False, help='Reduces radius of \'za by 1')
    parser.add_argument('-p', '--price', required=True, type=float, help='Price of pizza in US dollars')
    parser.add_argument('-s', '--size', required=True, choices=["small", "medium", "large", "extraLarge"], help ='Size of pizza')
    parser.add_argument('-v', '--verboose',action='store_const', const=True, default=False, help='Print data')

    args = parser.parse_args()

    # Set args to variables
    noCrustBool = args.nocrust
    verboose = args.verboose
    size = args.size
    price = args.price

    # Dict containing std pizza radii in US inches
    if noCrustBool:
        # if -n flag is set, reduce radius by 1
        sizes = {"small" : 4 , "medium": 5 , "large" : 6, "extraLarge" : 7}    
    else:
        sizes = {"small" : 5 , "medium": 6 , "large" : 7, "extraLarge" : 8}



    def circleArea(radius):
        return round(math.pi * math.pow(radius, 2), 3)

    sqin = circleArea(sizes[size])
    result = sqin/price

    if verboose:
        print str(sqin) + " sq in, at $" + str(price) + ", is " + str(result) + " sq in per dollar"
    else:    
        print result
    return result

if __name__ == "__main__": main()
