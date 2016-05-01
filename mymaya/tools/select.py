import pymel.core as pm

def main():
    pass


def first_or_default(list, default=None):
    for item in list:
        if item:
            return item
    return default


def shape_node(object, default=None):
    return pm.listRelatives(object, shapes=True)


if __name__ == '__main__':
    main()
