import os
from PIL import Image


def main(path):
    for i in content:
        im1 = Image.open(rf'{path}\{i}')
        im1.save(rf'{path}\{i.split(".")[0]}.jpeg')
        os.remove(rf'{path}\{i}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = r'C:\Users\vsavc\OneDrive\Desktop\GIT\SCP_task1\people'
    main(path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
