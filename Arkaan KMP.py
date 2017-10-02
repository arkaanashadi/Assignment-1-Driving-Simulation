user=input().split("-")
for i in range (len(user)):
	user[i] = user[i][0]
print(("".join(user)).upper())