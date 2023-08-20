## Level

Available while viewing the level info:

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `INT` | Level ID | 0x3222D0, 0x2A0 | Won't work on official levels or daily/weekly levels |

Available while playing:

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `STR` | Level name | 0x3222D0, 0x164, 0x22C, 0x114, 0xFC | See [get level name.py](/scripts/get%20level%20name.py) |
| `STR` | Creator | 0x3222D0, 0x164, 0x22C, 0x114, 0x144 |
| `STR` | Level string | 0x3222D0, 0x164, 0x22C, 0x114, 0x12C, 0x0 |
| `INT` | Level ID | 0x3222D0, 0x164, 0x22C, 0x114, 0xF8 |
| `INT` | Clicks | 0x3222D0, 0x164, 0x2B4 |
| `INT` | Total jumps | 0x3222D0, 0x164, 0x22C, 0x114, 0x224 |
| `INT` | Previous attempt percentage | 0x3222D0, 0x164, 0x4C0 |
| `INT` | Session percentage record | 0x3222D0, 0x164, 0x4C0 | Does not apply to practice mode |4
| `INT` | Current attempt | 0x3222D0, 0x164, 0x4A8 |
| `INT` | Total attempts | 0x3222D0, 0x164, 0x22C, 0x114, 0x218 |
| `STR` | Current percentage | 0x3222D0, 0x164, 0x124, 0xB4, 0x3C0, 0x12C |
| `INT` | Maximum percentage | 0x3222D0, 0x164, 0x488, 0x248 |
| `INT` | Maximum practice percentage | 0x3222D0, 0x164, 0x488, 0x26C |
| `FLOAT` | Level length | 0x3222D0, 0x164, 0x3B4 |
| `INT` | Stars | 0x3222D0, 0x164, 0x22C, 0x114, 0x2AC |
| `INT` | Featured score | 0x3222D0, 0x164, 0x22C, 0x114, 0x27C | Level is featured if this is greater than zero |
| `BOOL` | Epic | 0x3222D0, 0x164, 0x22C, 0x114, 0x280 |
| `BOOL` | Demon | 0x3222D0, 0x164, 0x22C, 0x114, 0x29C | See [get level difficulty.py](/scripts/get%20level%20difficulty.py) |
| `BOOL` | Auto | 0x3222D0, 0x164, 0x22C, 0x114, 0x2B0 | See [get level difficulty.py](/scripts/get%20level%20difficulty.py) |
| `INT` | Difficulty | 0x3222D0, 0x164, 0x22C, 0x114, 0x1E4 | See [get level difficulty.py](/scripts/get%20level%20difficulty.py) |
| `INT` | Demon difficulty | 0x3222D0, 0x164, 0x22C, 0x114, 0x2A0 | See [get level difficulty.py](/scripts/get%20level%20difficulty.py) |
| `INT` | Level type | 0x3222D0, 0x164, 0x22C, 0x114, 0x364 | See [level type enumeration](/enumerations/level%20type.md) |
| `INT` | Song ID | 0x3222D0, 0x164, 0x488, 0x1C4 | Doesn't work with official songs |
| `STR` | Time since upload | 0x3222D0, 0x164, 0x22C, 0x114, 0x174 | Usually only correct with more recent levels |
| `STR` | Time since last update | 0x3222D0, 0x164, 0x22C, 0x114, 0x18C | Usually only correct with more recent levels |
| `BOOL` | Paused | 0x3222D0, 0x164, 0x52F |