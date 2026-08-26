# # Multiples of 3 or 5
#Solutions
# 1. My
#2. Using list comprehensions
#3 Using a generator (Memory Efficient)
def multiples_of_3_or_5(limit):
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            yield i

for num in multiples_of_3_or_5(1000):
    print(num)

# 4. Using set and range() to avoid duplicates manually

# #3 Find the multiples of 3 or 5 below 1000.
# lst = []
# maxval = int(1000)
# for i in range(1,maxval):
#     if i%3 ==0 or i%5 ==0:
#         lst.append(i)
#         print(i)
#         
# print("the numbers are:", lst)
# print(sum(lst))
# print(10%5)
# print(10//5)
# 
# 
# # Pythonic way using List Comprehension:
lst = [i for i in range(1,1000) if i%3 ==0 or i %5 ==0]
for i in lst:
    print(sum(i))
    
    
lst = [i for i in range(1,100) if i%3==0 or i%5==0]
for i in lst:
    print(sum(I))
