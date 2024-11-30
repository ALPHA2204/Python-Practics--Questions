# Para is a sequence of space-seperated words. All words will be in lowe case . There will ba a single space between conscutive words. 

# Write a function named exact_count that accepts the String para and a positive integer n as arguments.you have to return True if there is at least one word in para that occurs exactly n times , and false otherwise.

def exact_count(para , n):
    Dic = {}
    para = para.split(" ")
    for i in para:
        if i  not in Dic: # Here we use the not in Dic.
              Dic[i] = 1
        else:
            Dic[i] += 1
    for i in Dic:
        if Dic[i] == n:
            return True
        else :
            return False
        
print(exact_count("Alok Alok   Tiwari also is called Seter in Parth",3))
            
                
    