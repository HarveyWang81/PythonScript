import os


def tree(search_path, level=0):
    try:
        for var in os.listdir(search_path):
            if os.path.isfile(os.path.join(search_path, var)):
                print("{0} {1}".format(' ' * level + '|_', var))
            elif os.path.isdir(os.path.join(search_path, var)):
                print("{0} {1}".format(' ' * level + '|_', var))
                tree(os.path.join(search_path, var), level + 2)
    except Exception:
        print("您输入的路径有问题！")


search_path = input('请输入一个路径:').replace(' ', '')
tree(search_path)
