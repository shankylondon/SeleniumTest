for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row-col == 2) or (row+col == 8):
            print("*", end=" ")
        elif(row == 2 and col == 1):
            print("P", end=" ")
        elif (row == 2 and col == 2):
            print("R", end=" ")
        elif (row == 2 and col == 3):
            print("I", end=" ")
        elif (row == 2 and col == 4):
            print("T", end=" ")
        elif (row == 2 and col == 5):
            print("T", end=" ")
        else:
            print(" ", end=" ")
    print()


