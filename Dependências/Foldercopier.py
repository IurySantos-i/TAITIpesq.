

import shutil
import os

source_root = r"F:\Clones de reps. Taiti"
destination_root = r"C:\Users\Marcos\Documents\Pesquisa TAITI\Dependências"

for root, dirs, files in os.walk(source_root):
    for d in dirs:
        src_dir = os.path.join(root, d)
        dst_dir = os.path.join(destination_root, d) + ".git"
        shutil.copytree(src_dir, dst_dir)
