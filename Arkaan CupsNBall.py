user = input().upper()
ball = [1,0,0]
for i in range(len(user)):
	if user[i] == "A":
		x = ball[0]
		ball[0] = ball[1]
		ball[1] = x
	elif user[i] == "B":
		x = ball[1]
		ball[1] = ball[2]
		ball[2] = x
	elif user[i] == "C":
		x = ball[0]
		ball[0] = ball[2]
		ball[2] = x
for i in range(3):
	if ball[i]==1:
		print(i+1)