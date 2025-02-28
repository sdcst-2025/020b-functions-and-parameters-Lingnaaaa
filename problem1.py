#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""

def hypotenuse(a,b,x):
  a=int(a)
  b=int(b)
  c=0
  if x is True:
     c=(a**2+b**2)**0.5
     print(f"{c}")
     return c
  if x is False and b > a:
     c=(b**2-a**2)**0.5
     print(c)
     return c
  if x is False and a > b:
     c=(a**2-b**2)**0.5
     print(c)
     return c

if __name__ == "__main__":
    assert hypotenuse(3,4,True) == 5
    assert hypotenuse(5,12,True) == 13
    assert hypotenuse(3,5,False) == 4
    assert hypotenuse(13,12,False) == 5
    
    