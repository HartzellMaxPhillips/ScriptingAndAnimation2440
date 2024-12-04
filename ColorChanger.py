import maya.cmds as cmds

def set_override_color(color):
    """
    Change the override color of shape nodes for the selected objects.

    Args:
        color (int or str): The color value (0-31) or color name to apply.
    """
    # Define a mapping of color names to their respective Maya color index values
    color_mapping = {
        "black": 1, "dark_gray": 2, "light_gray": 3, "gray": 4, 
    "dark_blue": 5, "blue": 6, "dark_green": 7, "green": 8,
    "dark_purple": 9, "purple": 10, "dark_red": 11, "red": 12, 
    "dark_orange": 13, "orange": 14, "yellow": 15, "light_yellow": 16, 
    "white": 17, "light_blue": 18, "aqua": 19, "light_green": 20, 
    "dark_brown": 21, "brown": 22, "pink": 23, "peach": 24, 
    "olive": 25, "lime": 26, "teal": 27, "cyan": 28, 
    "magenta": 29, "light_purple": 30, "gold": 31
    }
    
    # Convert color name to value if necessary
    if isinstance(color, str):
        color = color_mapping.get(color.lower())
        if color is None:
            cmds.warning(f"Invalid color name: {color}. Valid options are: {', '.join(color_mapping.keys())}")
            return
    
    # Validate that color is within the range of 0-31
    if not (0 <= color <= 31):
        cmds.warning("Color value must be an integer between 0 and 31.")
        return
    
    # Get selected objects
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    for obj in selected_objects:
        # Get all shape nodes in the hierarchy of the object
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True)

        if not shapes:
            cmds.warning(f"No shape nodes found for {obj}.")
            continue

        for shape in shapes:
            # Enable the override display settings
            cmds.setAttr(f"{shape}.overrideEnabled", 1)
            cmds.setAttr(f"{shape}.overrideColor", color)

    print(f"Override color set to {color} for the selected objects.")

# Example usage
set_override_color("blue")  # Use a color name
# set_override_color(6)    # Use a color index
