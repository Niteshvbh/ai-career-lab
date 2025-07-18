import os

# Folder where your image files are located
folder_path = "path/to/your/folder"  # 🔁 Replace with actual path, e.g., "F:/images"

# Get list of files in the folder
files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]
files.sort()  # Optional: sort to ensure consistent ordering

# Rename files
for index, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_filename = f"marathi_movie_{index}.jpg"
    new_path = os.path.join(folder_path, new_filename)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_filename}")

print("✅ Renaming completed!")
