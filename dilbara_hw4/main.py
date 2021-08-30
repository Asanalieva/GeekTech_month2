import calculator
import random
rand_list = []
for i in range(1,21):
    n = random.randint(1,100)
    rand_list.append(n)
aa = random.choice(rand_list)
bb = random.choice(rand_list)
print("1st random integer is", aa)
print("2nd random integer is", bb)
s1 = calculator.Calculator().plus(aa, bb) #put here extra integers (args)
s2 = calculator.Calculator().minus(aa, bb) #put here extra integers (args)
s3 = calculator.Calculator().devide(aa, bb)#put here extra integers (args)
s4 = calculator.Calculator().mult(aa, bb)#put here extra integers (args)



