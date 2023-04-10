from pathlib import Path
from objectldr import OBJloader

if __name__ == '__main__':
    base = Path(__file__).resolve().parent.parent
    filepath = base / "mygame/assets/meshes/monkey.obj"

    objldr = OBJloader()
    data = objldr.load_data(filepath)

    #for d in data:
    #    print(d)

    test_array = []

    if not test_array:
        print("Test array is empty.")
