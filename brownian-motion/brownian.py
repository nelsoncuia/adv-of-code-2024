import matplotlib.pyplot as plt 
import random

price = []


## Initial price
p = 100000
## number of months
number_of_months = 240 ##20 anos
## montlhy gain
c = 1.01 ##1%
## montlhy loss
l = 0.99 ##1%

##probability of going up
prob = 0.5


price.append(p)


for i in range(1,number_of_months):
    up_or_down = random.uniform(0, 1)
    if up_or_down > 0.3:
        price.append(price[i-1]*c)
    else:
        price.append(price[i-1]*l)



plt.plot(price)
plt.xlabel('Months passed')
plt.ylabel('Wallet value')
plt.show()

print(price)
