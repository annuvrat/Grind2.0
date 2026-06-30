arr= [{"firstname":"pinshu"},{"firstname":"pinshu"}]


total=0
for char in  arr:
    if char.get("firstname")=="pinshu":
        total += 1
print(total)
