import pymel.core as pm
from mymaya.tools import select


def copy(sel, delete_original=True):
    """
    Copies shape node of first item to others in list
    @param sel: list of objects, first item must have shape node to copy
    @type sel: list
    @param delete_original: delete original shape node object, default=True
    @type delete_original: bool
    @return: None
    """

    # Separate shape object from list
    object = sel.pop(0)

    # Check to make sure first object has a shape node
    if not select.shape_node(object):
        print("Error: First object should have shape node")

    else:
        # For every other item selected, copy and parent shape node, then delete copy
        for item in sel:
            objectCopy = pm.duplicate(object)
            shapeCopy = select.shape_node(objectCopy)
            pm.parent(shapeCopy, item, s=True, r=True)
            pm.delete(objectCopy)
    if delete_original:
        # Delete original shape object
        pm.delete(object)

    return


if __name__ == '__main__':
    selection = pm.ls(sl=True)
    copy(selection)
