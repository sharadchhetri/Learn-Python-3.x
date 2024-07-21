## Commented line also works.

import os
from pathlib import Path

# p = Path("pythonTest/L1/L2")
# p.mkdir(parents=True, exist_ok=True)
try:
    p = Path("NewDir/L1")
    p.mkdir(parents=True, exist_ok=False)

except FileExistsError:
    print("Directory Exists")


# try:
#     os.makedirs('osDir/nest1/nest2')
# except FileExistsError:
#     print('File already exists')

