/*
Working:
Each element is placed at its correct position
after each iteration
*/
#include<iostream>
using namespace std;
class InsertionSort
{
    public:
    int arr[12] = {1,3,6,22,8,9,25,12,15,16,20,10};
    int size = sizeof(arr)/sizeof(arr[0]);
    int key, j;
    
    void insertion()
    {
     for(int i = 1;i<size;i++)
        {
          key = arr[i];
            j = i-1;
        
            while(key < arr[j] && j>=0 )
            {
                arr[j+1] = arr[j];
                --j;
            }
            arr[j+1] = key;
        }
    }
    void display()
    {
        for (int  i = 0; i <size; i++)
        {
            cout<<arr[i]<<" ";
        }
        
    }
};

int main()
{
    InsertionSort insert;
    insert.insertion();
    insert.display();
}