# Example of reading gamemode
GAMEMODES = ["Cube", "Ship", "UFO", "Ball", "Wave", "Robot", "Spider"]

def get_gamemode():
	array = read_bytes(6, 0x3222D0, 0x164, 0x224, 0x638) # Read 6 bytes
	index = array.index(b"\x01") + 1 if b"\x01" in array else 0

	return GAMEMODES[index]