print "Type initial value: ";
$initialValue = <STDIN>;
print "Type end value: ";
$endValue = <STDIN>;

while ($initialValue <= $endValue) {
	$controlValue = $initialValue;
	$stepCounter = 0;
	print "Calculation start for $initialValue\n";
	$greatestValue = 0;
	while ($controlValue != 1) {
		$stepCounter++;
		if ($controlValue % 2 == 0) {
			$controlValue = $controlValue / 2;
		} else {
			$controlValue = 3 * $controlValue + 1;
		}
		if ($greatestValue < $controlValue) {
			$greatestValue = $controlValue;
		}
		print "In step $stepCounter of $initialValue is $controlValue. \n";
	}
	print "$initialValue is calculated in $stepCounter steps. Greatest value is $greatestValue. \n \n";
	$initialValue++;
}