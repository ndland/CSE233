# A simple program to convert Kilometers into miles


def main():
    print ("This program will convert kilometers into miles")

    kilometers = float(input("Please enter the number of kilometers: "))
    miles = kilometers * 0.62

    print (str(kilometers) + " kilometers is the equivalence of "
           + str(miles) + " miles")

main()
