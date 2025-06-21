import os

def get_subfolders(input_path: str) -> list[str]:
    """
    Retrieves all immediate subfolders within a given input path.

    Args:
        input_path (str): The path to the directory to scan for subfolders.

    Returns:
        list[str]: A list of full paths to the immediate subfolders.
                   Returns an empty list if the input_path does not exist,
                   is not a directory, or if there are no subfolders.
    """
    subfolders = []
    if not os.path.isdir(input_path):
        print(f"Error: '{input_path}' is not a valid directory or does not exist.")
        return subfolders

    try:
        for entry_name in os.listdir(input_path):
            full_path = os.path.join(input_path, entry_name)
            if os.path.isdir(full_path):
                subfolders.append(full_path)
    except PermissionError:
        print(f"Permission denied: Could not access '{input_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred while scanning '{input_path}': {e}")

    return subfolders