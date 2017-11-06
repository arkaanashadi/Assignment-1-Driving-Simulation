# Calculates the velocity from the inputs
def velocity (a,t):
	return a*t
	
# Calculates the displacment
def displacement (a,t):
	return (t*velocity(a,t)/2)
	
def main():
	print("Please fill the following (may be filled with decimals)\n")
	
# Requests time input and makes sure it is a float
	while 1==1:
		try:
			t = float(input("Time spent on the road: "))
			break
		except:
			print("Input must be a number")
			continue

# Requests acceleration input and makes sure it is a float
	while 1==1:
		try:
			a = float(input("Acceleration: "))
			break
		except:
			print("Input must be a number")
			continue
			
# Requests distance input and makes sure it is a float
	while 1==1:
		try:
			d = float(input("Distance: "))
			break
		except:
			print("Input must be a number")
			continue

# Prints the inputs for clarity
	print("\n"*3)
	print("Results:\n")
	print("Time spent on the road: "+str(d))
	print("Acceleration: "+str(a))
	print("Distance: "+str(d)+"\n")
		
# Prints the final velocity or max speed and whether it passed the speed limit or not
	if int(velocity(a,t)) > 60:
		print("The person went over the speed limit. (Max speed was "+str(velocity(a,t))+" m/s)")

	elif int(velocity(a,t)) <= 60:
		print("The person did not go over the speed limit. (Max speed was "+str(velocity(a,t))+" m/s)")

# Prints the final velocity or max speed and whether it reached the destination or not
	if int(displacement(a,t)) >= d:
		print("The person reached the destination. (Reached "+str(displacement(a,t))+" m)")
		
	elif int(displacement(a,t)) < d:
		print("The person did not reach the destination. (Reached "+str(displacement(a,t))+" m)")
		
# Prints the distance traveled each duration (distance represented by asteriks)
	print("\n"+"Note: 1 asterisk (*) = 10m")
	for i in range(0,int(t+1)):
		print("Duration: "+str(i)+" Distance: "+"*"*int(displacement (a,i)/10))

main()