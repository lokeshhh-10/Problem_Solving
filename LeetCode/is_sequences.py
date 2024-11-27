s = 'abc'
t = 'ahbgdc'
sums = 0
l = 0
for r in range(len(t)):
    if s[l] == t[r]:
        sums+=1
        l+=1

print(sums == len(s))
