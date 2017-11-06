user=input().split("-")
print(user)
for i in range (len(user)):
	user[i] = user[i][0]
print(user)
print(("".join(user)).upper())