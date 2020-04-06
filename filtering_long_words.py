"""
Write a function filter_long_words() that takes a list of words and an integer n
and returns the list of
words that are longer than n
"""

def filter_long_words(list,n):
    new_list=[]
    for i in list:
        if len(i)<=n:
            pass
        else:
            new_list.append(i)
    return new_list

x=filter_long_words(['venu','ratan','two'],3)
print(x)