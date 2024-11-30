'''{
      "TID' : "Gurunanth_890",
      'Items':[
          {"Name":"NoteBook","Price":56,"Quantity":4},
          {"Name":"Pencles","Price":9,"Quantity":2},
          {"Name":"Pen","Price":15,"Quantity":6},
          {"Name":"Book","Price":100,"Quantity":1},
          {"Name":"Eraser","Price":5,"Quantity":3}
         ]}'''
         
        # We have to Change in the form of:
'''{
    "Cost":305
    "TID":"Gurunath_890"
}
'''
# def get_summary(Bills):
#     D=[]
#     for i in Bills:
#         A= {}
#         cost = 0
#         for items in i["Items"]:
#             cost += int(items["Price"])*int(items["Quantity"])
#         A["cost"] = cost
#         A["TID"] =i["TID"]
#         D.append(A)
#     return D


# Bills = {"TID": "Alok_6388",
#          "Items" : [{"Name":"NoteBook","Price":56,"Quantity":4},
#                     {"Name":"NoteBook","Price":56,"Quantity":4}]
#         }
# print(get_summary(Bills))
''' AI  GERNATED CODE'''
def get_summary(Bills):
    D = []
    for i in Bills:
        A = {}
        cost = 0
        for items in i["Items"]:
            cost += int(items["Price"]) * int(items["Quantity"])  # Corrected capitalization
        A["cost"] = cost
        A["TID"] = i["TID"]
        D.append(A)
                 # Append to list D, not dictionary
    return D

Bills = [{"TID": "Alok_6388",
          "Items": [{"Name": "NoteBook", "Price": 56, "Quantity": 4},
                    {"Name": "NoteBook", "Price": 56, "Quantity": 4}]
         }]  # Corrected structure to be a list of dictionaries

print(get_summary(Bills))
