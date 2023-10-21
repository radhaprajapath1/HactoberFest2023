# checks if the input list has all elements as even 

def ifevenlist(self, s: lst) -> bool:
    for l in lst:
        if l%2!=0:
            return False
    return True
