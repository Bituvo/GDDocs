## Player

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `FLOAT` | Wave pulse size | 0x2E63A0 |

Available while playing a level:

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `FLOAT` | X-position | 0x3222D0, 0x164, 0x224, 0x67C |
| `FLOAT` | Y-position | 0x3222D0, 0x164, 0x224, 0x680 |
| `BYTES` | Gamemode array | 0x3222D0, 0x164, 0x224, 0x638 | Causes issues when set |
| `BOOL` | Inverted gravity | 0x3222D0, 0x164, 0x224, 0x63E |
| `BOOL` | Dead | 0x3222D0, 0x164, 0x39C | Setting to 1 freezes the player and locks rotation at 0 degrees if in the air |
| `FLOAT` | Speed | 0x3222D0, 0x164, 0x224, 0x648 | See [speed enumeration](/enumerations/speed.md)
| `FLOAT` | Hitbox size | 0x3222D0, 0x164, 0x224, 0x644 | Anything other than 1 enables mini mode |
| `BOOL` | Practice mode | 0x3222D0, 0x164, 0x495 | Can be set to change modes but won't toggle button overlay |
| `BOOL` | Dashing | 0x3222D0, 0x164, 0x224, 0x614 |