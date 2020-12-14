//Determine if the input number is odd or even in dart

import 'dart:io';
void main() {
	int number = int.parse(stdin.readLineSync());
	number%2==0?
		print('even'):print('odd');
}
