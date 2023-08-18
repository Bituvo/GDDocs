# Example of getting the current level difficulty
NORMAL_DIFFICULTIES = ["easy", "normal", "hard", "harder", "insane"]
DEMON_DIFFICULTIES = ["easy demon", "medium demon", "insane demon", "extreme demon"]

def get_difficulty():
	if read_bool(0x3222D0, 0x164, 0x22C, 0x114, 0x2B0):
		return "auto"

	elif read_bool(0x3222D0, 0x164, 0x22C, 0x114, 0x29C):
		demon_difficulty = read_int(0x3222D0, 0x164, 0x22C, 0x114, 0x2A0)
		if demon_difficulty == 0:
			return "hard demon"
		else:
			return DEMON_DIFFICULTIES[demon_difficulty - 3]
	
	normal_difficulty = read_int(0x3222D0, 0x164, 0x22C, 0x114, 0x1E4)
	return NORMAL_DIFFICULTIES[normal_difficulty // 10 - 1]