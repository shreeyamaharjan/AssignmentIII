def towerHanoi(n, source, destination, temporary):
    if n == 1:
        print("Move disk {} from {} to {} ".format(n, source, destination))

    else:
        towerHanoi(n - 1, source, temporary, destination)
        print("Move disk {} from {} to {} ".format(n, source, destination))
        towerHanoi(n-1, temporary, destination, source)


n = int(input("Enter the number of disks : "))
towerHanoi(n, 'A', 'B', 'C')
