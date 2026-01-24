import os

def create_folder(folder_path):
  """Creates a folder at the specified path.

  Args:
    folder_path: The path of the folder to create.
  """
  try:
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder '{folder_path}' created successfully or already exists.")
  except OSError as e:
    print(f"Error creating folder '{folder_path}': {e}")

if __name__ == "__main__":
  folder_to_create = "my_new_folder"
  create_folder(folder_to_create)
