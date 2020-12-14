//Given an array of integers, return the indices of the two numbers that add up to a given target

#include <iostream>
using namespace std;

//Searching a pair algorithm
int search(int *nums, int target,int len){

    for(int i=0;i<len;i++){
        for(int j=i+1;j<len;j++){
            if(nums[i] + nums[j] == target){
                cout<<i<<" "<<j<<endl;
                return 1;
            }
        }
    }

    return 0;
}

int main(){
    int nums[5] = {1,3,7,9,2};
    int target = 11;
    int len = sizeof(nums)/4;

    int result = search(nums, target, len);
    
    if(result == 0)
        cout<<"The pair not found"<<endl;

    return 0;
}

