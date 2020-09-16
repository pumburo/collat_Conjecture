import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

initialValue = int(input("Type initial value and press enter." + "\n"))
endValue = int(input("Type end value and press enter.(0 for endless) " + "\n"))
req1 = '''
Would you like to see all steps?
1-Yes
2-No
'''
print(req1)
stepsResponse = int(input())
req2 = '''
Would you like to generate graph?
1-Yes
2-No
'''
print(req2)
graphResponse = int(input())

controlValue = 0
graphCounter = 0
valueArray = []
counterArray = []
testVar = 0

try:
    if initialValue == 1 or initialValue == 0:
        print("\n" + "Trying to calculate", initialValue, "is meaningless. Starting from 2." + "\n")
        initialValue = 2

    while (initialValue <= endValue or endValue == 0):
        controlValue = initialValue
        #graphCounter+=1
        #valueArray.append(initialValue)
        greatestValue = 0

        if stepsResponse == 1:
            print(initialValue, "is calculating.")
        counter = 0

        while (controlValue != 1):
            counter+=1
            left = controlValue % 2
            
            if left == 0:
                controlValue = controlValue / 2
            elif left != 0:
                controlValue = controlValue * 3
                controlValue+=1
            
            if stepsResponse == 1:
                print("Step " + str(counter) + ":", int(controlValue))
            
            if controlValue > greatestValue:
                greatestValue = controlValue

            graphCounter+=1
            valueArray.append(controlValue)
            counterArray.append(graphCounter)

            #print("Counter array:", counterArray, "Value array:", valueArray)

        if stepsResponse == 1:
            if initialValue != endValue:
                print(initialValue, "is calculated in", counter, "steps. Greatest value is:", int(greatestValue), "\n" * 3)
            elif initialValue == endValue:
                if stepsResponse == 1:
                    print(str(initialValue), "is calculated in", counter, "steps. Greatest value is:", int(greatestValue))
                elif stepsResponse == 2:
                    print("\n" * 3 + str(initialValue), "is calculated in", counter, "steps. Greatest value is:", int(greatestValue))

        elif stepsResponse == 2:
            print(initialValue, "is calculated in", counter, "steps. Greatest value is:", int(greatestValue))

        initialValue+=1

    if graphResponse == 1:
        figure(num=None, figsize=(50, 15), dpi=80, facecolor='gray')
        plt.plot(counterArray, valueArray, '-ok')
        plt.show()
    
    testVar+=1


except:
    if testVar != 0:
        print("Procces stoped by user.")
    
    try:
        if graphResponse == 1:
            figure(num=None, figsize=(50, 15), dpi=80, facecolor='gray')
            plt.plot(counterArray, valueArray, "-ok")
            plt.show()
        elif graphResponse == 2:
            print("Procces stoped by user.")

    except:
        print("BOOOOM!!!" + "\n" + "Program become bomb.")