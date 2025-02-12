# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n):
            min_index = i
            
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                   min_index = j
            
            arr[min_index], arr[j] = arr[j], arr[min_index]
        
        return arr