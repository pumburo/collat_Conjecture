import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

quest = '''
Would you like to generate graph?(1/2)
1-Yes
2-No
'''
print(quest)
qres = int(input())
value = int(input("Type start value: "))
stopValue = int(input("Type stop value(0 for endless.): "))
valueArray = []
counterArray = []
cnt = 0

if value == 1:
    value+=1

try:
    while True:
        print(str(value) + " is calculating.")
        newValue = value
        counter = 0        

        while ( newValue != 1 ):
            counter+=1
            left = newValue % 2

            if value == newValue:
            	topValue = newValue
            
            if left == 0:
                newValue = newValue / 2
            elif left != 0:
                newValue = newValue * 3
                newValue+=1

            if topValue <= newValue:
            	topValue = newValue
            
            print(newValue)

            if newValue == 1:
                print(str(value) + " is calculated in " + str(counter) + " steps." + " Greatest value is " + str(int(topValue)) + ".")
                print(" \n", " \n", " \n", " \n")

            cnt+=1
            valueArray.append(newValue)
            counterArray.append(cnt)

        if value == stopValue:
        	break
        
        value+=1

except:
    print("Procces stoped by user.")

if qres == 1:
	figure(num=None, figsize=(50, 15), dpi=80, facecolor='gray')
	plt.plot(counterArray, valueArray, '-ok')
	plt.show()
