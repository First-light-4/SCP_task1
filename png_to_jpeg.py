import os
from PIL import Image


def main():
    content = os.listdir(r'C:\Users\vsavc\OneDrive\Desktop\GIT\SCP_task1\people')
    print(content)
    for i in content:
        im1 = Image.open(rf'C:\Users\vsavc\OneDrive\Desktop\GIT\SCP_task1\people\{i}')
        im1.save(rf'C:\Users\vsavc\OneDrive\Desktop\GIT\SCP_task1\people\{i.split(".")[0]}.jpeg')
        os.remove(rf'C:\Users\vsavc\OneDrive\Desktop\GIT\SCP_task1\people\{i}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
