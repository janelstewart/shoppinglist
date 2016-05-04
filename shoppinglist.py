item = raw_input("Please add an item to your shopping list:")

def shopping_list(item):
    shopping_list = []
    shopping_list.append(item)
    return shopping_list
    # raw_input("is your shopping list complete? Please type yes or no")
    # if(yes)
    # if(no)

    if(item in shopping_list):
        print "Item already listed."
    else:
        shopping_list.append(item)

#     shopping_list2 = raw_input("is your shopping list complete? Please type yes or no")
#         if(yes):
#             #print shopping list 
#         if(no):
#             #  raw_input("add next item") 
# else:

print shopping_list(item)