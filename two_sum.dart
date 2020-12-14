//Give a set of integers, return the indices of the two numbers that add up to a given target

import 'dart:io';
void main() {
  
  //set of integers, ex) 1 3 7 9 2
  stdout.write("Input: ");
	List<String> numlist = stdin.readLineSync().split(' ');
	List<int> nums = numlist.map(int.parse).toList();
	
  //a target, ex) 11
	stdout.write("Target: ");
	int target = int.parse(stdin.readLineSync());

  //return if the length of set is zero or one
	if(nums.length < 2){
		print("return null");
		return;
	}
	
	for(int i=0;i<nums.length;i++){
		for(int j=i+1;j<nums.length;j++){
			if(nums[i] + nums[j] == target){
				print('index = '+i.toString()+', '+j.toString());
				return;
			}
		}
	}
	
	print('No result found');
}

