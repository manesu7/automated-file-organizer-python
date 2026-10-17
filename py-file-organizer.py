import os
import shutil
from pathlib import Path

def organize_files():
    # Define the project directory and the target test-folder
    project_dir = Path(__file__).parent.resolve()
    test_folder = project_dir / "test-folder"
    
    # Check if the target folder exists before proceeding
    if not test_folder.exists() or not test_folder.is_dir():
        print(f"Error: The folder '{test_folder}' does not exist.")
        print("Please create it and add files to organize.")
        return

    print(f"Scanning files in: {test_folder}\n")
    
    # Iterate through all items inside 'test-folder'
    for item in os.listdir(test_folder):
        item_path = test_folder / item
        
        # Only process files, skip directories
        if item_path.is_file():
            # Extract the extension in lowercase (e.g., '.pdf', '.docx')
            file_extension = item_path.suffix.lower()
            
            # Skip files that have no extension
            if not file_extension:
                continue
                
            # Strip the dot from the extension to format the folder name (e.g., 'pdf', 'docx')
            ext_name = file_extension.lstrip('.')
            
            # Handle specific custom folder naming rules requested
            if ext_name == 'jpg':
                folder_name = "jpg-files-folder"
            else:
                folder_name = f"{ext_name}-files"
                
            # Define the final path inside the project's folder
            destination_folder = project_dir / folder_name
            
            # Create the category folder if it doesn't exist
            destination_folder.mkdir(parents=True, exist_ok=True)
            
            # Target path for the moved file
            destination_file_path = destination_folder / item
            
            try:
                # Move the file from test-folder to the project-level category folder
                shutil.move(str(item_path), str(destination_file_path))
                print(f"Moved: {item} -> {folder_name}/")
            except Exception as e:
                print(f"Failed to move {item}: {e}")

if __name__ == "__main__":
    organize_files()
