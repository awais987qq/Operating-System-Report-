import os
import hashlib

def hash_file(file_path):
    """Generate hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None
    return sha256_hash.hexdigest()

def verify_integrity(input_path, output_path):
    """Verify the integrity of a file or folder by comparing its hash."""
    print("Hashing original file(s) for integrity check...")
    if os.path.isdir(input_path):
        for dirpath, _, filenames in os.walk(input_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                print(f"Hashing file: {file_path}")
                original_hash = hash_file(file_path)
                if original_hash is None:
                    print(f"Error processing file: {file_path}")
                    return False
        print("Integrity: PASSED (all files processed)")
        return True
    else:
        original_hash = hash_file(input_path)
        if original_hash:
            print(f"Original Hash: {original_hash}")
            print("Integrity: PASSED")
            return True
        else:
            print("Integrity: FAILED")
            return False