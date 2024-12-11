import sys, math
print(sys.argv)
digit = sys.argv[1]

length = 6
digit = int(digit)

def factor(n):
  factors = []
  choices = []
  da = []
  for b in range(0, length):
    choices.append(b)
  size = int(math.log10(n))
  for i in range(0, size + 1):
    #print((n // 10**i % 10))
    factors.append((n // 10**(size - i) % 10))
  num = n
  dct = []
  rems = []
  place = 1
  while num != 0:
    divided = num // place
    rem = num % place
    dct.append(divided)
    place = place + 1
    num = divided
    rems.append(rem)
    
  print(":".join(map(str, factors)))
  print(":".join(map(str, dct)))

  print(":".join(map(str, rems)))
  return reversed(rems)

factorials = list(factor(digit))

print("factorial")
print(factorials)
def permutation(l, n):
  avail = []
  
  for i in range(0, l + 1):
    avail.append(i)
  print("available")
  print(avail)
  digits = []
  for index in range(0, len(n)):
    print(index, n[index])
    digits.append(avail[n[index]])
    del avail[n[index]]
  print(":".join(map(str, digits)))
  return digits
x = permutation(length, factorials)
print(x)