friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
print(random.choice(friends))
a = random.randint(0,len(friends))
print(a)
print(friends[a])