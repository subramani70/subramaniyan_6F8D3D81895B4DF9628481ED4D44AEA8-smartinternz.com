def fact_rec(a):
     if a==0 or a==1:
       return 1
     else:
       return a*fact_rec(a-1)

number=int(input("enter the value"))
res=fact_rec(number)
print("the factorial of {} is {}.".format(number,res))
