dis_ans = []
print("Please input 10 numbers")
for i in range(10):
	user = int(input())
	if (user%42) not in dis_ans:
		dis_ans.append(user%42)
print("Distinct answer:",len(dis_ans))