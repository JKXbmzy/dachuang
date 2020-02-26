import collections

f = open(r"C:\Users\zoein\Desktop\week2\word.txt",encoding="utf-8")
a = f.read().split()

print(a)
print(collections.Counter(a))

words_dic = {}

for k in a:
    if k in words_dic:
        words_dic[k] += 1
    else:
        words_dic[k] = 1

print(words_dic)

f.close()
