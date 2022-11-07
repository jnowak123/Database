with open('Dane/przyklad.txt') as f:
    nums = [line.strip() for line in f]

#1
ans = [0, 0]
for num in nums:
    if num[0] == num[-1]:
        ans[0] += 1
        if ans[1] == 0:
            ans[1] = num
print(ans)

#2
def isprime(num):
    div = num // 2
    while div > 2:
        if num % div == 0:
            return False
        div -= 1
    return True

def smallestdiv(num):
    div = 2
    while num % div != 0:
        div += 1
    return div

ansa = [0, 0]
ansb = [0, 0]
for num in nums:
    x = int(num)
    divs = []
    while x != 1:
        div = smallestdiv(x)
        x = x / div
        if isprime(div):
            divs.append(div)
    if len(divs) > ansa[1]:
        ansa[0] = num
        ansa[1] = len(divs)
    if len(set(divs)) > ansb[1]:
        ansb[0] = num
        ansb[1] = len(set(divs))

print(ansa, ansb)
