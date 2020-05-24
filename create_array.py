from random import randint

def create_array(length=10,maxint=50):
    array = [randint(0,maxint) for _ in range(length)]
    return array