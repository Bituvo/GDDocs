## Editor

| Type | Description | Offsets | Notes |
| :--: | ----------- | ------- | ----- |
| `BOOL` | In editor | 0x3222D0, 0x168 |
| `FLOAT` | Block X | 0x3222D0, 0x168, 0x380, 0x2C4, 0x34 |
| `FLOAT` | Block Y | 0x3222D0, 0x168, 0x380, 0x2C4, 0x38 |
| `FLOAT` | Block scale | 0x3222D0, 0x168, 0x380, 0x2C4, 0x35C |
| `FLOAT` | Block rotation | 0x3222D0, 0x168, 0x380, 0x2C4, 0x20 | Out of 360 degrees (default is 0) |
| `INT` | Block L | 0x3222D0, 0x168, 0x380, 0x2C4, 0x40C |
| `INT` | Block L2 | 0x3222D0, 0x168, 0x380, 0x2C4, 0x410 |
| `FLOAT` | Editor length | 0x2E67A4 | Will update instantly and not let you place blocks outside the region |
| `INT` | Editor layer | 0x3222D0, 0x168, 0x354 | Will be -1 if all layers are selected |