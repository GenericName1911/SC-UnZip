import sys
import os
from sc_compression import decompress as decompress_data

def decompress_files():
    if len(sys.argv) < 2:
        return
    # Process each file path provided in command-line arguments
    for file_path in sys.argv[1:]:
        # Skip if the file does not exist (failsafe)
        if not os.path.isfile(file_path):
            continue
        try:
            # Open and read the compressed file
            with open(file_path, 'rb') as input_file:
                compressed_data = input_file.read()
            # Decompress the data
            decompressed_data, *extra_data = decompress_data(compressed_data)
            # Create a new file with the 'd_' prefix
            base_name = os.path.basename(file_path)
            output_file_name = f"d_{base_name}"
            output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)
            # Write the decompressed data to the new file
            with open(output_file_path, 'wb') as output_file:
                output_file.write(decompressed_data)
        except Exception:
            pass

if __name__ == '__main__':
    decompress_files()
