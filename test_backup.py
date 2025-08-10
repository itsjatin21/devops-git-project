import shutil
import os

def backup_file(source, destination):
    if os.path.exists(source):
        shutil.copy(source, destination)
        print(f"Backed up {source} to {destination}")
    else:
        print(f"File {source} does not exist.")

# Example usage
if __name__ == "__main__":
    backup_file("example.txt", "backup_example.txt")
