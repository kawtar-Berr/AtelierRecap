# script_simple.py

import os

def main():
    files = os.listdir('.')  # liste tout ce qui est dans le dossier courant
    print("Fichiers dans le workspace :")
    for f in files:
        print(" -", f)
    print(f"Nombre total de fichiers : {len(files)}")

if __name__ == '__main__':
    main()
