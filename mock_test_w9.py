petrolpumps = [[1 , 5], [10, 3], [3, 4]]

start = 0
petrol = 0
distance = 0

for i in range(len(petrolpumps)):
    petrol += petrolpumps[i][0]
    distance += petrolpumps[i][1]
    if petrol < distance:
        petrol = 0
        distance = 0
        start = i + 1

print(start)