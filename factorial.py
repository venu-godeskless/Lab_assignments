"""
Write a program that contains a function that has one parameter, n,
representing an integer greaterthan 0. The function should return n! (n factorial). Then write a main function that
calls this function with
the values 1 through 20, one at a time, printing the returned results. This is what your
output should look
like:
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800
"""



n=int(input('enter the number:'))
fact =1

for i in range(1,n+1):
    fact*=i
    # fact=fact

    x=1
    for j in range(i,i+1):
        print(j,fact)


