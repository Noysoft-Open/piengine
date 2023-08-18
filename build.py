import os
import sys 
from pathlib import Path

base_path = Path(__file__).resolve().parent.parent 

if sys.argv[1] == "create":
    print(sys.argv[1])
    os.system('cmd /k "pyinstaller %s\piengine\mygame\mygame.spec"' % str(base_path))

if sys.argv[1] == "test":
    print(sys.argv[1])
    os.system('cmd /k "python %s\piengine\mygame\mygame.py"' % str(base_path))
