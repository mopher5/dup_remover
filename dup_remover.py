import os
import hashlib
import argparse

def calculate_hash(file_path):
    hash_algo = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_algo.update(chunk)
    return hash_algo.hexdigest()

def find_and_remove_duplicates(folder_path, delete_duplicates):
    hash_dict = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            if file_hash in hash_dict:
                if delete_duplicates:
                    os.remove(file_path)
                    print(f"Removed duplicate file: {file_path}")
                else:
                    print(f"Duplicate file found: {file_path}")
            else:
                hash_dict[file_hash] = file_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find and remove duplicate images.")
    parser.add_argument("folder_path", help="The folder path to check for duplicates.")
    parser.add_argument("-d", "--delete", action="store_true", help="Automatically delete duplicate images.")
    args = parser.parse_args()

    find_and_remove_duplicates(args.folder_path, args.delete)