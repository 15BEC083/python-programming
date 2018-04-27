char = "abcdefghijklmnopqrstuvwxyz"
str = raw_input()
for i in char:
  count = str.count(i)
  if count > 1:
    print i,
