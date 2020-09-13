import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
value = int(input("Type start value: "))
stopValue = int(input("Type stop value(0 for endless.): "))
newArray = []
counterArray = []
cnt = 0
if value == 1:
    value+=1
try:
    while ( value != stopValue ):
        print(str(value) + " is calculating.")
        newValue = value
        counter = 0        
        while ( newValue != 1 ):
            counter+=1
            left = newValue % 2
            if left == 0:
                newValue = newValue / 2
            elif left != 0:
                newValue = newValue * 3
                newValue+=1
            print(newValue)
            if newValue == 1:
                print(str(value) + " is calculated in " + str(counter) + " steps.")
                print(" \n", " \n", " \n", " \n")
            cnt+=1
            newArray.append(newValue)
            counterArray.append(cnt)
        value+=1
except:
    print("Procces stoped by user.")
figure(num=None, figsize=(50, 15), dpi=80, facecolor='gray')
plt.plot(counterArray, newArray, '-ok')
plt.show()
