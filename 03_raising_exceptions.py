# we can raise custom error

def increment(num):
    try:
        return num+10
    except:
        raise ValueError("Invalid Number addition")
        
a = increment(10)  
print(a)      
"""a = increment("asdadas") #  , will raise value error
print(a)""" 