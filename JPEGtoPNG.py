import sys
import os
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for filename in os.listdir(folder):
    img = Image.open(f'{folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{new_folder}{clean_name}.png', 'png')
