import maya.cmds as mc
import pymel.core as pm


class Curve:

    def __init__(self, curve):
        self.curve = curve
        self.name = curve[0]
        self.type = mc.getAttr('{}.form'.format(self.name))
        self.degree = mc.getAttr('{}.degree'.format(self.name))
        self.spans = mc.getAttr('{}.spans'.format(self.name))
        self.cvs = self.degree + self.spans

    def loc_per_cv(self):
        for cv in range(self.cvs):
            locator = self._create_loc()
            self._attach_to_curve(locator[0], cv)

    def _create_loc(self):
        return mc.spaceLocator()

    def _attach_to_curve(self, child, cv):
        # attach to motion path
        # @param: fm = fraction mode
        motion_path = mc.pathAnimation(child, str(self.name), fm=True)
        # break U value connection of motion path
        pm.disconnectAttr('{}_uValue.output'.format(motion_path))
        # set U value
        spacing = 1.0 / (self.cvs - 1)
        u_position = spacing * cv
        pm.setAttr('{}.uValue'.format(motion_path), u_position)
