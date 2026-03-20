print(ord("A"))
print(ord("a"))
print(ord("0"))
print(ord("@"))
print(chr(65))
print(chr(97))
print(chr(48))
print(chr(64))

char=input("Enter a single character:")
if type(char) is str and len(char)==1:
    print("Valid input")
else:
    print("Enter only ONE character")

ascii_val=ord(char)

print(f"Character:{char}")
print(f"ASCII value:{ascii_val}")

if ascii_val>=65 and ascii_val<=90:
    print("Type:Uppercase letter")

if ascii_val>=97 and ascii_val<=122:
    print("Type:Lowercase letter")
if ascii_val>=48 and ascii_val<=57:
    print("Type:Digit")
if ascii_val==32:
    print("Type:Space")
else:
    print("Type:Special character")