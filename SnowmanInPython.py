import maya.cmds as cmds

#Create the base of the snowman with a sphere
cmds.polySphere(radius=3, subdivisionsX=20, subdivisionsY=20, axis=(0, 3, 0), createUVs=2, constructionHistory=True)
cmds.move(0, 3, 0, relative=True)

#middle of Snowman
cmds.polySphere(radius=2, subdivisionsX=20, subdivisionsY=20, axis=(0, 3, 0), createUVs=2, constructionHistory=True)
cmds.move(0, 8, 0, relative=True)

#Head of snowman
cmds.polySphere(radius=1.25, subdivisionsX=20, subdivisionsY=20, axis=(0,3,0), createUVs=2, constructionHistory=True)
cmds.move(0, 11.25, 0, relative=True)

#snowman's nose
cmds.polyCone(radius=1, height=2, subdivisionsX=20, subdivisionsY=20, subdivisionsZ=0, axis=(0,1,0), roundCap=0, createUVs=3, constructionHistory=True)
cmds.move (0, 11.25, 1.6)
cmds.rotate(90, 0, 0, relative=True, objectSpace=True, forceOrderXYZ=True)
cmds.scale(0.075, 0.35, 0.075, relative=True)

#snowman's eyes
cmds.polySphere(radius=1, subdivisionsX=15, subdivisionsY=15, axis=(0,3,0), createUVs=2, constructionHistory=True)
cmds.move(0.325, 11.8, 1.1, relative=True)
cmds.scale(0.1, 0.1, 0.03)
cmds.rotate(-25, 13, 0, relative=True, objectSpace=True, forceOrderXYZ=True)

# Duplicate previous object, adjust position and rotation
cmds.duplicate(rr=True)
cmds.move(-0.65, 0, 0, relative=True)
cmds.rotate(0, -26, 0, relative=True)

# Snowman's buttons
cmds.polyCylinder(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0), roundCap=False, createUVs=3, constructionHistory=True)
cmds.rotate(90, 0, 0, relative=True)
cmds.scale(0.15, 0.01, 0.15, relative=True)
cmds.move(0, 8, 2, relative=True)

cmds.polyCylinder(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0), roundCap=False, createUVs=3, constructionHistory=True)
cmds.rotate(60, 0, 0, relative=True)
cmds.scale(0.15, 0.01, 0.15, relative=True)
cmds.move(0, 9, 1.75, relative=True)

cmds.polyCylinder(radius=1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0), roundCap=False, createUVs=3, constructionHistory=True)
cmds.rotate(120, 0, 0, relative=True)
cmds.scale(0.15, 0.01, 0.15, relative=True)
cmds.move(0, 7, 1.75, relative=True)

# Snowman's arms
cmds.polyCylinder(radius=0.1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0), roundCap=False, createUVs=3, constructionHistory=True)
cmds.rotate(0, 0, 60, relative=True)
cmds.move(-2.58, 9.5, 0, relative=True)

cmds.polyCylinder(radius=0.1, height=2, subdivisionsX=20, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0), roundCap=False, createUVs=3, constructionHistory=True)
cmds.rotate(0, 0, 120, relative=True)
cmds.move(2.58, 9.5, 0, relative=True)
