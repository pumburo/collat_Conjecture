try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure
    libImp = 1
except:
    print("matplotlib is doesn'n exist. If you want to generate graph, you need to install this libary.")
    libImp = 2

initialValue = int(input("Type initial value and press enter." + "\n"))
endValue = int(input("Type end value and press enter.(0 for endless) " + "\n"))
req1 = '''
Would you like to see all steps?
1-Yes
2-No
'''
print(req1)
stepsResponse = int(input())

if libImp == 1:
    req2 = '''
Would you like to generate graph?
1-Yes
2-No
    '''
    print(req2)
    graphResponse = int(input("\n"))
elif libImp == 2:
    graphResponse = 2

controlValue = 0
graphCounter = 0
valueArray = []
counterArray = []
graphVar = 0

try:
    if initialValue == 1 or initialValue == 0:
        print("\n" + "Trying to calculate", initialValue, "is meaningless. Starting from 2." + "\n")
        initialValue = 2

    while (initialValue <= endValue or endValue == 0):
        controlValue = initialValue
        graphCounter+=1
        counterArray.append(graphCounter)
        valueArray.append(initialValue)
        greatestValue = 0

        if stepsResponse == 1:
            print(initialValue, "is calculating.")
        counter = 0
        graphVar+=1

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
        graphVar = 0

except:    
    try:
        lastCalculatedValue = initialValue - 1
        print("Last calcualted value is:", lastCalculatedValue)
        if graphResponse == 1 and graphVar == 0:
            figure(num=None, figsize=(50, 15), dpi=80, facecolor='gray')
            plt.plot(counterArray, valueArray, "-ok")
            plt.show()
        elif graphResponse == 2:
            print("Procces stoped by user.")

    except:
        print("BOOOOM!!!" + "\n" + "Program is explode.")
        explode = '''
          _ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              ;   ;
              /   \
             /     \
____________/__ __ _\_____________
        '''
        print(explode)
