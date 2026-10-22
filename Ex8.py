# TOWER HANOI
from PIL import Image

def tower_of_hanoi(n, source, helper, destination):

    if n == 1:
        print("Move Disk 1 From", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, helper)
    print("Move Disk", n, "From", source, "to", destination)
    tower_of_hanoi(n - 1, helper, source, destination)


n = int(input("Enter Number Of Disks: "))

tower_of_hanoi(n, "A", "B", "C")

total_moves = (2 ** n) - 1
print("Total Moves:", total_moves)

if total_moves == 7:

    img = Image.open("ex6.png")
    img.show()
    
if total_moves == 15:

    img = Image.open("ex1_6.png")
    img.show()
