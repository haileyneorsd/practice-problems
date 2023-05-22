
#https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1?page=1&difficulty[]=-1&sortBy=submissions

#using permutations is not efficient bc returns all combinations of arr, and adding digits is the same result regardless of the order of the digits.
#arr.sort() to sort array in ascending order
#if sum>0, the sum is too high so decrease sum by decreasing highest digit (second-=1)
#else (if sum<0) the sum is too low so increase sum by increasing lowest digit (first+=1). 

from itertools import permutations

#Function to find triplets with zero sum.   
def findTriplets(arr, n): 
    arr.sort()
    for i in range(n):
        first=i+1
        second=n-1 
        while first<second:
            sum=arr[i]+arr[first]+arr[second]
            if sum==0:
                return True
            elif sum>0:
                second-=1 
            else:
                first+=1 
            
    return False

if __name__ == '__main__':

    n = 5 
    arr = [0, -1, 2, -3, 1]
    print(findTriplets(arr,n))
    #True

    n1 = 3 
    arr1 = [1, 2, 3]
    print(findTriplets(arr1,n1))
    #False