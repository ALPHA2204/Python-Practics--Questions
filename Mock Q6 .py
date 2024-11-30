# The Scores_datset is alist of Dictionaries one of whose is given below for your reference:

#{'Seq No.':1,'Name': 'Deepak','Gender':'F','City':'Bengalur'
#  'Mathematics':85,'Physics':100}


# The Instrution is allow to Create a Group of Similar Students

# A group should be associated wuth a particular subject.
# The Difference btween scores of any two student in the grioup should be at least mark_limit:
# You Should have to make a group for only on Subject
# And You Should to find maximum student group formed ,And also the no of Student

def crowd_group(scores , sub , limt):
    list = []
    for stu in scores:
        list.append(stu[sub]) # It Create a Matrix by in the [12,34,56,22,12,34,78]
    list.sort() # List.short
    grp = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i]-list[j] <=limt:
                if j-i+1>grp:    # This is finding the no of Student that is in the Group by index number and by adding +1 they are 
                    grp = j-i+ 1  # the student which marks is compsred to other ..
    return grp
                
                
    