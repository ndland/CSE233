from graphics import *

def main():

    f = open('A.txt', 'r')
    g = open('B.txt', 'r')
    matrix_a = []
    matrix_b = []
    result = []

    # Read in A.txt
    for line in f:
        intValues = []
        stringValues = line.strip().split(',')
        for stringValue in stringValues:
            intValues.append(int(stringValue)) 
        matrix_a.append(intValues)

    # Read in B.txt
    for line in g:
        intValues = []
        stringValues = line.strip().split(',')
        for stringValue in stringValues:
            intValues.append(int(stringValue)) 
        matrix_b.append(intValues)

    del(matrix_a[0]) # Do not need the size of the matrix
    del(matrix_b[0]) # Do not need the size of the matrix

    # Populate the product of matrix_a and matrix_b
    sums = 0
    for i in range(len(matrix_a)): # i is 0,1,2: represents the rows in matrix_a
        temp = []
        for j in range(len(matrix_b[0])): # j is 0,1,2,3,4: represents the columns in matrix_b
            for k in range(len(matrix_b)): # k is 0,1,2,3,4,5,6: represents the rows in matrix_b
                sums = sums + (matrix_a[i][k] * matrix_b[k][j]) 
            temp.append(sums)
            sums = 0
        result.append(temp)

    # Find the mins and maxs of each matrix
    matrix_a_max = max(max(matrix_a))
    matrix_a_min = min(min(matrix_a))
    matrix_b_max = max(max(matrix_b))
    matrix_b_min = min(min(matrix_b))
    matrix_a_b_max = max(max(result))
    matrix_a_b_min = min(min(result))

    # Heat Graph
    x = 17 * 25 + 150
    y = 7 * 25 + 50

    win = GraphWin("Matrix", x, y)
    win.setCoords(0, 0, x, y)
    title_a = Text(Point((7 * 25 + 50)/2, 12.5), "A")
    title_b = Text(Point((5 * 25 + 50)/2 + 7 * 25 + 50, 12.5), "B")
    title_a_b = Text(Point((7 * 25 + 50)/2 + 5 * 25 + 7 * 25 + 75, 12.5), "A * B")
    title_a.draw(win)
    title_b.draw(win)
    title_a_b.draw(win)

    for i in range(0, 3):  #Draw A matrix
        for j in range(0, 7):
            g = (matrix_a[i][j] - matrix_a_min) / (matrix_a_max - matrix_a_min)
            c = [(g * (255 - 0) + 0), (g * (0 - 0) + 0), (g * (0 - 255) + 255)]
            heat1 = Rectangle(Point(25 * (j + 1), y - (25 * (i + 1))), Point(25 * (j + 2), y - (25 * (i + 2))))
            heat1.setFill(color_rgb(c[0], c[1], c[2]))
            heat1.draw(win)
    for i in range(0, 7): #Draw B matrix
        for j in range(0, 5):
            g = (matrix_b[i][j] - matrix_b_min) / (matrix_b_max - matrix_b_min)
            c = [(g * (255 - 0) + 0), (g * (0 - 0) + 0), (g * (0 - 255) + 255)]
            heat1 = Rectangle(Point((25 * (j + 1) + (7 * 25 ) + 50), y - (25 * (i + 1))), Point((25 * (j + 2) + (7 * 25 ) + 50), y - (25 * (i + 2))))
            heat1.setFill(color_rgb(c[0], c[1], c[2]))
            heat1.draw(win)
    for i in range(0, 3): #Draw A * B matrix
        for j in range(0, 5):
            g = (result[i][j] - matrix_a_b_min) / (matrix_a_b_max - matrix_a_b_min)
            c = [(g * (255 - 0) + 0), (g * (0 - 0) + 0), (g * (0 - 255) + 255)]
            heat1 = Rectangle(Point((25 * (j + 1) + (7 * 25 ) + (5 * 25 ) + 100), y - (25 * (i + 1))), Point((25 * (j + 2) + (7 * 25 ) + (5 * 25 ) + 100), y - (25 * (i + 2))))
            heat1.setFill(color_rgb(c[0], c[1], c[2]))
            heat1.draw(win)

    win.getMouse()

main()
