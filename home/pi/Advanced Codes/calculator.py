#CALCULATOR





import math

 print("enter 3 numbers")
x=input()
y=input()
z=input()


#TYPECASTING SO THAT A STRING IS NOT READ AND INSTEAD AN INTEGER IS READ

x=int(x)
y=int(x)
z=int(z)

#LAMBDA WORKS AS A MACRO


doSum = lambda x,y,z : x+y+z
print("sum = ",doSum(x,y,z))

doProduct = lambda x,y,z : x*y*z
print("product = ", doProduct(x,y,z))

doDivision = lambda x,y,z : x/y/z
print("quotient is = ",doDivision(x,y,z))

doLogProduct = math.log10(doProduct(x,y,z))
print("log base 10 of product =",doLogProduct)
