#include<iostream>
using namespace std;
void sort(int arr[],int size){
	int i,min,max;
	int arr1[size];
	for(i=0;i<size;i++){
		if(arr[i+1]<arr[i]){
			arr[i]=arr[i+1];
		}
	}
	cout<<"\nArray: ";
	for(i=0;i<size;i++){
		cout<<arr1[i]<<" ";
	}
	cout<<"\nMin of array is: "<<arr[0];
	cout<<"\nMax of array is: "<<arr[size-1];
}
int main(){
	int max,size;
	cout<<"Enter Size of Array: "<<endl;
	cin>>size;
	int arr[size];
	for(int i=0;i<size;i++){
		cout<<"Enter arr["<<i<<"] : ";
		cin>>arr[i];
	}
	sort(arr,size);
	
	return 0;
}
