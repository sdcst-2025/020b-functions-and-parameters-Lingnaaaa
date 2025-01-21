#!python3

def sum(a,b):
    #print(a)
    #print(b)
    sum = a + b
    print(f'The sum is {sum} in {a,b}')
    return sum


if __name__ == "__main__":
    print("This is my program")

    assert sum(5,2) == 7
    assert sum(1,2) == 3
    assert sum(5,-32) == -27
    assert sum(5,2.5) == 7.5
    assert round(sum(5.1,2.3),1) == 7.4
    
