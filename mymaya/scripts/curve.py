import maya.cmds as mc


class Curve:

    def __init__(self, curve):
        self.curve = curve
        self.name = curve[0]
        self.type = mc.getAttr('{}.form'.format(self.name))
        self.degrees = mc.getAttr('{}.degree'.format(self.name))
        self.spans = mc.getAttr('{}.spans'.format(self.name))
        self.cvs = self.degrees + self.spans
