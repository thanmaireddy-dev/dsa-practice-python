def rotate_array(arr, k):
    n= len(arr)
    k= k%n
    def rotate(p1,p2):
        while(p1<p2):
            arr[p1], arr[p2]= arr[p2], arr[p1]
            p1= p1+1
            p2= p2-1
    rotate(0,n-1)
    rotate(0,k-1)
    rotate(k,n-1)
    return arr

print(rotate_array([1,2,3,4,5,6,7],3))      
        
            
      
        
           
       
        

