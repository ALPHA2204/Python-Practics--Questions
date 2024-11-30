# The Scores_datset is alist of Dictionaries one of whose is given below for your reference:

#{'Seq No.':1,'Name': 'Deepak','Gender':'F','City':'Bengalur'
#  'Mathematics':85,'Physics':100}

# A Student X can mentore to another student iff Codition Satisfies;
# 10 <= X.subject - Y.subject <= 20
# Write a function named mentore that accept the following options:
# Score_dataset
# Subject


# The function should return a dictionary having the following structure :
# Key : Seq No. of student
#Value : list of Seq No. of Student who csn be mentore by the above student
# Note Student cannot mentore himself 


def mentor(score_data , subject):
    L ={}
    for student in score_data:
        L[student["SeqNo"]] = []  # Here we creating a key vlaue pair of SeqNo. and the value is List
        for j in score_data:
            if j["SeqNo"] != student["SeqNo"]:# Here we going to get j() in the loop in score_data Set .
                marks = student[subject]-j[subject]  # Here Subject is Given in the Argument
                if 10<=marks<=20:
                      L[student["SeqNo"]].append(j["SeqNo"])
    return L
#Good catch! The current implementation allows a student to mentor themselves, which isn't ideal. Let's refine the logic to exclude the student from their own list of mentees.