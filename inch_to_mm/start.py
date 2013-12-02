#!/usr/local/bin/python3

import inch_to_mm_converter

def main():

	print ("This program will convert inches into millimeters")

	inches = float(input("Please enter the number of inches: "))
	# print str(inches)

	new = inch_to_mm_converter.Converter()
	millimeters = new.convert(inches)

	print (str(inches) + " inches is the equivalence of " +
		str(millimeters) + " millimeters")

if __name__=='__main__':main()
