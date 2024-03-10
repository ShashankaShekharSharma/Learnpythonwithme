# Gurunath is a popular store in IIT Madras. Among other things, it sells stationary items. The owner of the store gives you the list of transactions that happened in a day. Each transaction comes with an unique transaction ID. He wants to calculate the cost of each transaction. Can you help him find out?
#The List trans is a list of transactions that happened at the shop in a given day. Each element in this list is a dictionary. The details of one such transaction is given below
# {
#     'TID': 'Gurunath_8528',
#     'Items': [
#         {'Name':'Notebook', 'Price':50,'Qty':4},
#         {'Name':'Pencil','Price':10,'Qty':1}, 
#         {'Name':'Eraser','Price':15,'Qty':1}, 
#         {'Name':'File','Price':80,'Qty':1}
#     ]
# }
# Write a function named get_summary that accepts trans as argument. It should return a list of dictionaries. Each dictionary should have two keys: TID and cost. For example one of the elements of the list would be as follows:
# {
#     'Cost':305,
#     'TID':'Gurunath_8528'
# }
#The computation of the cost is Summation of Price*Qty
# 1. The ordered elements in the returned list should be the same as the order in the input list, i.e., the ith element in the ordered list should correspond to the transaction cost of the ith element in the trans.
# 2. You do not have to accept input from the user or print the output in the console. You just have to write the function definition
def get_summary(trans):
    d = []
    a = {}
    for i in trans:
        cost = 0
        for items in trans['items']:
            cost += items['price']*items['qty']
        a['cost'] = cost
        a['tid'] = trans['TID']
        d.append(a)
    return d