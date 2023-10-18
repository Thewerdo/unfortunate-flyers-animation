#This program uses Euclid's Algorithm to find the simplified form of a fraction that is inputted by the user

#introduction
print("Welcome to my fraction simplifier!")

while True:
  #determine initial values
  top=int(input("Type in an integer numerator:"))
  bottom=int(input("Type in an integer denominator:"))

  #if either value is = 0, fraction is always either undefined or zero
  if bottom == 0:
    print("This fraction is undefined.")
  
  elif top == 0:
    print("This fraction is zero.")

  elif top < 0 or bottom < 0:
    print("This program can only handle positive numbers.")
  
  else: #all other cases
    #find gcd, calculate
    Max = max (top, bottom)
    Min = min (top, bottom)
    R = Max % Min

    while R != 0:
      Max = Min
      Min = R
      R = Max % Min

    GCD = Min
    
    top1=int(top/GCD)
    bottom1=int(bottom/GCD)
  
    if bottom1 == 1: #if denominator is 1
      print("The fraction simplified is ", top1, ".")

    elif GCD == 1: #fraction cannot be reduced
      print("The fraction", top1, "/", bottom1, "is already fully simplified.")
    
    else:
      print("The simplified fraction is ", top1, "/", bottom1, ".")