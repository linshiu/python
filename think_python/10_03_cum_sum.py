def cum_sum(t):
    '''
    Write a function that takes a list of numbers and returns the cumulative sum; that
    is, a new list where the ith element is the sum of the first i + 1 elements
    from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].'''

    total = 0
    cum_list = []

    for i in t:
        total += i
        cum_list.append(total)
    
    return cum_list


print cum_sum([1,2,3])        
