''' A sequence of integer of even length is said to be left heavy if sum of first half is greater than second half if second is greater than first right-heavy and also same then Balenced'''
 
a = input().split(",")
Len = len(a)//2 # To get integer Len Value
left = 0
right = 0
for i in range(len(a)):
    if i < Len:
        left +=int(a[i])
    else :
        right +=int(a[i])  # Here we have a[i] for += then a[i] must be int for these manpulation
if(left == right):
        print("Balanced")
        
elif(left<right):
        print('Right Heavy')
        
else:
        print("Left Heavy")        
   
        