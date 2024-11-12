num = list(range(1,11))
print("Numbers from 1 to 10.....\n",num)
for i in num:
 if(i%2 == 1):
     num.remove(i)
print("The values after removing odd numbers.....\n",num)
