
"""
Script to detect the encoding of a file using the chardet library.

Dependencies
------------
chardet : Python library for character encoding detection.

Constants
---------
INPUT_FILE : str
    Path to the file for which to detect the encoding.
"""

# Third party imports
import chardet

# Constants
INPUT_FILE: str = 'replace-me.csv'

def detect_encoding(file_path: str) -> str:
    """
    Detect the encoding of a file.

    Parameters
    ----------
    file_path : str
        Path to the file for which to detect the encoding.

    Returns
    -------
    str
        Detected encoding of the file.
    
    """
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())

    return result['encoding']

if __name__ == "__main__":
    encoding_result = detect_encoding(INPUT_FILE)
    print(f"The detected encoding is: {encoding_result}")
