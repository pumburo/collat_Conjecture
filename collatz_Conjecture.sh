echo "Type initial value: "
read initialValue
echo "Type end value: "
read endValue

while (( $initialValue <= $endValue || $endValue == 0 )); do
    controlValue=$initialValue
    stepCounter=0
    echo "Calculation start for $initialValue."
    greatestValue=0
    while [[ $controlValue != 1 ]]; do
        let stepCounter++
        if [[ $(( $controlValue % 2 )) == 0 ]]; then
            controlValue=$(( $controlValue / 2 ))
        elif [[ $(( controlValue % 2 )) != 0 ]]; then
            controlValue=$(( 3 * $controlValue + 1 ))
        fi
        if [[ $greatestValue < $controlValue ]]; then
            greatestValue=$controlValue
        fi
        echo "In step $stepCounter of $initialValue is $controlValue."
    done 
    echo "$initialValue is calculated in $stepCounter steps. Greatest value is $greatestValue."
    echo ""
    let initialValue++
done