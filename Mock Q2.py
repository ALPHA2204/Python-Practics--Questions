''' A Data Entery has faulty keyboard. The keys 0 and 1 are very unrealiable Sometimes they donot work ,  operator use "l"for replecement of 1 and "o" is replecment of 0 . ''' 

''' Test Cases
 # 1) 987o35l7o4
 output - 3 Mistakes
         9870351704
'''

Nums = input()
With_Mistake = ""
count = 0
for i in Nums:
    if i == "o":
        count += 1
        With_Mistake += "0"
    elif i == "l":
        count += 1
        With_Mistake += "1"
    else:
        With_Mistake += i
        
if(count == 0):
    print("No Mistake")
else:
    print(f'{count} Mistake')
    print(With_Mistake)
    
