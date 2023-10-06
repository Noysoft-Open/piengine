import os
import sys 
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent 
print(base_path)

if sys.argv[1] == "build":
    print(sys.argv[1])
    os.system('pyinstaller %s/piengine/mygame/mygame.spec' % str(base_path))

if sys.argv[1] == "test":
    print(sys.argv[1])
    os.system('python %s/piengine/mygame/mygame.py' % str(base_path))
 