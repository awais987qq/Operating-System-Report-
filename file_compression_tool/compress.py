import os
import zipfile
import gzip
import shutil

def compress_file(input_path, output_path, method='zip', level='best'):
    if method == 'zip':
        with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED if level == 'best' else zipfile.ZIP_STORED) as zipf:
            zipf.write(input_path, os.path.basename(input_path))
    elif method == 'gzip':
        with open(input_path, 'rb') as f_in, gzip.open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def compress_folder(input_folder, output_path, method='zip', level='best'):
    if method != 'zip':
        raise ValueError("Only .zip format supports folder compression.")
    with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED if level == 'best' else zipfile.ZIP_STORED) as zipf:
        for root, dirs, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=input_folder)
                zipf.write(file_path, arcname)