#! python3

import task2

def test1(number):
  assert task2.largest((3,1,4,7,13,9)) == 13
  currtmax=0
  currtmax=max(number)
  return currtmax


def test2():
  assert task2.largest([5,1,12.3]) == 12.3
  
if __name__ == "__main__":
  test1()
  test2()
