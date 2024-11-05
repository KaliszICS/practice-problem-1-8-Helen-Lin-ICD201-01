
def q1():
  #Write Assignment code here
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  #Write Assignment code here
  num = input("Enter an integer: ")
  num = int(num)
  bool = (num > 0)
  print(bool)

def q3():
  #Write Assignment code here
  num = input("Enter a number: ")
  num = float(num)
  bool = num >= 0 and num <= 10
  print(bool)
  
def q4():
  #Write Assignment code here
  word1 = input("Input food: ")
  word2 = input("Input drink: ")
  bool = word1 != "pizza" and word2 != "pop"
  print(bool)

def q5():
  #Write Assignment code here
  num = input("Enter an integer: ")
  num = int(num)
  bool = (num%2) == 0
  print (f"The integer {num} is", (bool))
#Do not edit code after this
#Comment out the followwing code when running tests

#q1()
#q2()
#q3()
#q4()
#q5()
