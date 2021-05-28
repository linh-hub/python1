from random import randint

print("nhap dam,la,keo")
player = input()
computer = randint(0,2) 

print("you chose" + player)
print("computer choses" + computer)


if computer == 0:
	computer = "dam"
elif computer == 1:
	computer = "la"
else:
	computer = "keo"


if player == "keo":
	if computer == "keo":
		print("draw")
	elif computer == "dam":
		print("lose")
	else:
		print("win")
		
if player == "dam":
	if computer == "keo":
		print("win")
	elif computer == "dam":
		print("draw")
	else:
		print("lose")
		
if player == "la":
	if computer == "keo":
		print("lose")
	elif computer == "dam":
		print("win")
	else:
		print("draw")

