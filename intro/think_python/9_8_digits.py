def is_palindrome(i,start,len):
    s = str(i)[start:start+len]
    return s[::-1] == s


        
def check_puzzle(i):
    return (is_palindrome(i,2,4) and
            is_palindrome(i+1,1,5) and
            is_palindrome(i+2,1,4) and
            is_palindrome(i+3,0,6) )

def check_all():

    i = 100000
    while i<= 999999:
        if check_puzzle(i):
            print i
        i = i+1

check_all()
                      
