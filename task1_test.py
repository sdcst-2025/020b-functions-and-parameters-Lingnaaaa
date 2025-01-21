
import task1


def test1(a,b):
  sum = a + b
  return sum
def output(a,b,sum):
  print(f"The sum of a number with {a},{b} is {sum}")


def test2(a,b):
  sum= a + b
  return sum
  
  
if __name__ == "__main__":
  z=test1(11,2.5)
  output(11,2.5,z)

  i=test2(8,-2)
  output(8,-2,i)

  #output()
  #test2()
