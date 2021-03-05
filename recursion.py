def recursion(count):
    if count == 500: # base case
        return 0
    else:
        print('Hello World', count)
        recursion(count+1)

count = 0
recursion(count)