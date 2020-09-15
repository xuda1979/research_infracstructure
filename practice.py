import collections
cnt = collections.Counter()
dic = ['a','a','b']
freq = collections.Counter(dic)
print(freq.most_common(10))
print(freq['a'])
dp = [[0]*10]*10
print(dp)
for __ in range(10):
    print("hello")