Products = """
    1. Head Phones (hps_...)
        1. Wireless
        2. Earbuds
        3. Circumaural
        4. Supra-aural
        5. Noise-Cancelling
        6. Bone
        7. Conduction
        8. Closed-Back
        9. Open-Back
        10. Semi-Open
        11. Waterproof
        12. DJ

    2. Smart Phones (smp_...)
    3. Watches
        1. Analog
        2. Watches
        3. Digital
        4. Watches
        5. Smart
        6. Watch
        7. Dress
        8. Watches
        9. Quartz
        10. Watches
        11. Field
        12. Chronograph
        13. Swiss
        14. Pilots
        15. Tactile
        16. Casual
        17. Luxury"""


Str = """
Notebook
Ultraportable
Ultrabook
Chromebook
MacBook
Convertible
Tablet as a laptop
Netbook
"""


def Str_to_Bullets(Str):
    import re

    Res = re.findall('\S+', Str)
    print(*[f"    {i}. {ele}" for i, ele in enumerate(Res, 1)], sep='\n')


import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
Files = os.listdir(BASE_DIR)

for file in Files:
    if len(file[:file.find('.')])==2 and file.startswith('s'):
        print(file)
        os.rename(BASE_DIR / file, BASE_DIR / ('hp_' + file[1:]))

print(os.listdir(BASE_DIR))
