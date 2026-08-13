text1 =input("Enter a text:")
words=text1.split()
result=[]
for word in words:
  if word[0].isupper() and word[1:].islower():
    result.append(word)
print("Sequences are:",result)

text2 =input("\nEnter a text to check word containing'z':")
words=text2.split()
result2=[]
for word in words:
  if 'z' in word or 'Z' in word:
    result2.append(word)
print("Words containing 'z':",result2)

text3 =input("Enter text:")
has_upper=False
has_lower=False
has_digit=False
has_underscore=False
valid=True
for ch in text3:
  if ch.isupper():
    has_upper=True
  elif ch.islower():
    has_lower=True
  elif ch.isdigit():
    has_digit=True
  elif ch=='_':
    has_underscore=True
  else:
    valid=False
if valid and has_upper and has_lower and has_digit and has_underscore:
  print("Valid string")
else:
  print("Invalid string")

ip="192.168.001.010"
parts=ip.split('.')
new_parts=[]
for part in parts:
  new_parts.append(str(int(part)))
new_ip='.'.join(new_parts)
print("Given IP=",ip)
print("Updated IP after removing trailing zeros:",new_ip)
