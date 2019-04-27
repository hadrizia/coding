'''
    Problem: 
        Sock Merchant
    Input: 
        n: 9
        ar: 10 20 20 10 10 30 50 10 20
    Ouput:
        3
'''
def arToDict(ar):
    dict_ar = {}
    for element in ar:
            if element not in dict_ar:
                dict_ar[element] = 1
            else:
                dict_ar[element] = dict_ar[element] + 1
    return dict_ar

def countPairs(dict_ar):
    count = 0
    for value in dict_ar.values():
        count += value / 2
    return count

'''
    Given that:
        colors = number of colors
    Time efficiecy: O(n * colors)
'''
def sockMerchant(n, ar):
    count = 0
    
    if n > 1:
        dict_ar = arToDict(ar)
        count = countPairs(dict_ar)
    return count

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print sockMerchant(n, ar)