a=input("Enter the length of the list :")        
l=[]                                             
for g in range (a):                            
    b=input("Enter the element :")          
      
    l.append(b)                             
print ("Given elements",l)  
for  i in range (len(l)):                        
    index=i                                 
    num=l[i]                               
    for j in range(i+1,len(l)):              
        if num>l[j]:                  
            index=j                 
            num=l[j]             
    tem=l[i]                              
    l[i]=l[index]                        
    l[index]=tem  
print (l)  
