import maya.cmds as cmds
import re

def create_controls_for_joints():
    # Get the selected objects (joints)
    selected_joints = cmds.ls(selection=True, type="joint")

    if not selected_joints:
        cmds.warning("No joint objects selected.")
        return

    for joint in selected_joints:
        # Strip any existing suffix and replace with "_Ctrl"
        control_name = re.sub(r"(_[a-zA-Z]+)$", "_Ctrl", joint) if "_" in joint else joint + "_Ctrl"
        
        # Create the NURBS circle as the control
        control = cmds.circle(name=control_name, normal=(1, 0, 0), radius=1.0)[0]

        # Match transformation (position and rotation) to the joint
        position = cmds.xform(joint, query=True, worldSpace=True, translation=True)
        rotation = cmds.xform(joint, query=True, worldSpace=True, rotation=True)
        cmds.xform(control, worldSpace=True, translation=position)
        cmds.xform(control, worldSpace=True, rotation=rotation)

        # Create a group for the control
        group_name = f"{control_name}_Grp"
        control_group = cmds.group(empty=True, name=group_name)

        # Match the group transformation to the control
        cmds.xform(control_group, worldSpace=True, translation=position)
        cmds.xform(control_group, worldSpace=True, rotation=rotation)

        # Parent the control under the group
        cmds.parent(control, control_group)

        # Finally, parent the group to the joint
        cmds.parent(control_group, joint)

# Run the function
create_controls_for_joints()