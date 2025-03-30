from tprofile import profile

@profile
def my_function(x):
    # your function code here
    return x * x

my_function(10)
