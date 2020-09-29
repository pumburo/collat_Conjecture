#include <stdio.h>

int main(){
    int initialValue;
    int endValue;
    printf("\n\tType initial value: ", initialValue);
    scanf("%d", &initialValue);
    printf("\n\tType end value: ", endValue);
    scanf("%d", &endValue);
    int controlValue;
    while (initialValue <= endValue){
        printf("\n%s", "");
        printf("\nCalculation start for ", initialValue); printf("%d", initialValue); printf("%s", ".");
        controlValue = initialValue;
        int stepCounter = 0;
        int greatestValue = 0;
        while (controlValue != 1){
            if (controlValue % 2 == 0){
                controlValue = controlValue / 2;
            }
            else {
                controlValue = 3 * controlValue + 1;
            }
            if (greatestValue < controlValue){
                greatestValue = controlValue;
            }
            stepCounter++;
            printf("\n%s", "In step "); printf("%d", stepCounter); printf("%s", " of "); printf("%d", initialValue); printf("%s", " is: "); printf("%d", controlValue);
        }
        printf("\n%d", initialValue); printf("%s", " is calculated in "); printf("%d", stepCounter); printf("%s", " steps. Greatest value is "); printf("%d", greatestValue); printf("%s", ".");
        initialValue++;
    }
}