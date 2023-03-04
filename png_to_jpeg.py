import os
from PIL import Image


def main(path):
    for i in content:
        im1 = Image.open(rf'{path}\{i}')
        im1.save(rf'{path}\{i.split(".")[0]}.jpeg')
        os.remove(rf'{path}\{i}')

if __name__ == '__main__':
    path = r'C:\Users\vsavc\OneDrive\Desktop\GIT\SCP_task1\people'
    main(path)

