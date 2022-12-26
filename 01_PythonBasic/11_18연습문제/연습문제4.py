import random

num_list = []
while len(num_list) < 6:
    random_number = random.randint(1,46)
    if random_number in num_list:
        pass
    else:
        num_list.append(random_number)

print(num_list)

#lotto = list(range(1,46))
#lotto_number = random.sample(lotto,6)
#print(lotto_number)