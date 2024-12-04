import maya.cmds as cmds

def rename_objects(naming_scheme):
    """
    Renames selected objects based on the specified naming scheme.

    Args:
        naming_scheme (str): A string in the format "Name_##_NodeType".
    """
    # Validate naming scheme
    if "#" not in naming_scheme:
        cmds.warning("Naming scheme must contain '#' characters for numbering.")
        return
    
    # Determine the number of '#' characters in the naming scheme
    num_hashes = naming_scheme.count("#")
    if num_hashes == 0:
        cmds.warning("Naming scheme must contain at least one '#' character for numbering.")
        return
    
    # Replace all '#' characters with a placeholder for formatting
    base_name = naming_scheme.replace("#" * num_hashes, "{:0" + str(num_hashes) + "d}")
    
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    # Iterate through the selected objects and rename them
    for i, obj in enumerate(selected_objects, start=1):
        # Format the name with padded numbers
        new_name = base_name.format(i)
        
        # Rename the object
        try:
            cmds.rename(obj, new_name)
        except RuntimeError as e:
            cmds.warning(f"Could not rename {obj}: {e}")

    print(f"Renamed {len(selected_objects)} objects using naming scheme: {naming_scheme}")

# Example usage
rename_objects("Max_##_Circle")  
# Example input for a naming scheme

