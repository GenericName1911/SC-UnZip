import sys
import os
import re
import argparse
from sc_compression import decompress as decompress_data

def clean_filename(file_name):
    """
    Remove trailing patterns like ' (1)' from the filename,
    so that 'demo (1).csv' becomes 'demo.csv'.
    """
    # Remove trailing pattern ' (number)' before the extension.
    return re.sub(r'\s*\(\d+\)(?=\.[^.]+$)', '', file_name)

def decompress_files(input_files, output_dir_name):
    # Process each file provided in input_files
    for file_path in input_files:
        # Skip if the file does not exist
        if not os.path.isfile(file_path):
            continue
        try:
            # Determine the directory where the input file is located
            file_dir = os.path.dirname(file_path)
            # Create the output directory inside the file's directory
            output_directory = os.path.join(file_dir, output_dir_name)
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)

            # Open and read the compressed file
            with open(file_path, 'rb') as input_file:
                compressed_data = input_file.read()
            # Decompress the data
            decompressed_data, *extra_data = decompress_data(compressed_data)
            # Clean the file name by removing trailing ' (number)' if present
            base_name = os.path.basename(file_path)
            cleaned_name = clean_filename(base_name)
            # Build the full output file path
            output_file_path = os.path.join(output_directory, cleaned_name)
            # Write the decompressed data to the new file
            with open(output_file_path, 'wb') as output_file:
                output_file.write(decompressed_data)
        except Exception:
            pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Decompress files.")
    parser.add_argument('files', nargs='+', help="Input files to decompress.")
    parser.add_argument('-d', '--directory', default='decompressed',
                        help="Output directory name (default: 'decompressed') to be created in each file's folder")
    args = parser.parse_args()
    decompress_files(args.files, args.directory)
