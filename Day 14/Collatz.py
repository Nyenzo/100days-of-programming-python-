M = input("Enter the value of M:\n")
M = int(M)
counter = 0
while M > 1:
    counter +=1
    N=M
    if M % 2 == 0:
        M=M/2
        print("%s/2=%s" %(N,M))
    else:
        M=M*3+1
        print("%s*3+1=%s" %(N,M))
print("Number of iterations is:" +str(counter))        
        
