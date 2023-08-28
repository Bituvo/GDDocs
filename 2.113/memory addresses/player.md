## Player

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `INT` | Cube ID | 0x3222D0, 0x1F0 |
| `INT` | Ship ID | 0x3222D0, 0x1FC |
| `INT` | Ball ID | 0x3222D0, 0x208 |
| `INT` | UFO ID | 0x3222D0, 0x214 |
| `INT` | Wave ID | 0x3222D0, 0x220 |
| `INT` | Robot ID | 0x3222D0, 0x22C |
| `INT` | Spider ID | 0x3222D0, 0x238 |
| `INT` | Trail ID | 0x3222D0, 0x25C |
| `INT` | Explosion ID | 0x3222D0, 0x268 |
| `BOOL` | Glow | 0x3222D0, 0x27C |
| `FLOAT` | Wave pulse size | 0x2E63A0 |

Available while playing a level:

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `FLOAT` | X | 0x3222D0, 0x164, 0x224, 0x67C |
| `FLOAT` | Y | 0x3222D0, 0x164, 0x224, 0x680 |
| `BYTES` | Gamemode array | 0x3222D0, 0x164, 0x224, 0x638 | See [get gamemode.py](/2.113/scripts/get%20gamemode.py) |
| `BOOL` | Inverted gravity | 0x3222D0, 0x164, 0x224, 0x63E |
| `BOOL` | Dead | 0x3222D0, 0x164, 0x39C | Setting to 1 freezes the player and locks rotation at 0 degrees if in the air |
| `FLOAT` | Speed | 0x3222D0, 0x164, 0x224, 0x648 | See [speed enumeration](/2.113/enumerations/speed.md)
| `FLOAT` | Hitbox size | 0x3222D0, 0x164, 0x224, 0x644 | Anything other than 1 enables mini mode |
| `BOOL` | Practice mode | 0x3222D0, 0x164, 0x495 | Can be set to change modes but won't toggle button overlay |
| `BOOL` | Dashing | 0x3222D0, 0x164, 0x224, 0x614 |