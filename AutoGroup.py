import maya.cmds as cmds

def group_selected_objects():
    # Get the list of selected objects
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    for obj in selected_objects:
        # Query the position and rotation of the selected object
        obj_position = cmds.xform(obj, query=True, worldSpace=True, translation=True)
        obj_rotation = cmds.xform(obj, query=True, worldSpace=True, rotation=True)
        
        # Create a new group with no transformation
        group_name = f"{obj}_Grp"
        new_group = cmds.group(empty=True, name=group_name)
        
        # Apply the same transformation to the new group
        cmds.xform(new_group, worldSpace=True, translation=obj_position)
        cmds.xform(new_group, worldSpace=True, rotation=obj_rotation)
        
        # Parent the selected object under the new group
        cmds.parent(obj, new_group)

# Run the function
group_selected_objects()