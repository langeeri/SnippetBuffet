""" normalizer.py

Module for processing CSV data with timestamp interpolation.

This module defines a function to read CSV data and interpolate timestamps if necessary.
The processed data is then saved to a new CSV file.

Constants
---------
SOURCE_NAME : str
    The base (source) name for CSV files (excluding extension).
ENCODING : str
    The encoding used for reading CSV files.
DELIMITER : str
    The delimiter used in CSV files.
INTERVAL : str
    The resampling interval for timestamp interpolation.

Functions
---------
interpolate_timestamp(name: str) -> pd.DataFrame
    Interpolate timestamps in CSV data.

Usage
-----
To interpolate timestamps in a CSV file, use the interpolate_timestamp function.
For example:
    if __name__ == "__main__":
        interpolated_df = interpolate_timestamp(SOURCE_NAME)
        interpolated_df.to_csv(f'{SOURCE_NAME}_interpolated{CSV_EXTENSION}', index=False, sep=DELIMITER)
"""

# Third-party imports
import pandas as pd

# Constants
SOURCE_NAME: str = 'tc_18_1'
ENCODING: str = 'ISO-8859-1'
DELIMITER: str = ';'
INTERVAL: str = '10S'


def interpolate_timestamp(name: str) -> pd.DataFrame:
    """
    Interpolate timestamps in CSV data.

    Parameters
    ----------
    name : str
        The base name for CSV files (excluding extension).

    Returns
    -------
    pandas.DataFrame
        Interpolated DataFrame with timestamps.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(f'{name}.csv', delimiter=DELIMITER, encoding=ENCODING)

        # Check if heat pump is running (TC1 ot.komp. > 0), if not, interpolate timestamps
        if (df['TC1 ot.komp.'] <= 0).all():
            df_interpolated = df.resample(INTERVAL).interpolate()
        else:
            df_interpolated = df.copy()

        return df_interpolated

    except FileNotFoundError:
        print(f"Error: File '{name}.csv' not found.")
        return pd.DataFrame()  # Return an empty DataFrame in case of error


if __name__ == "__main__":

    try:
        interpolated_df = interpolate_timestamp(SOURCE_NAME)
        # Save the modified data to a new CSV file with the correct extension
        interpolated_df.to_csv(f'{SOURCE_NAME}_interpolated.csv', index=False, sep=DELIMITER)

    except Exception as e:
        print(f"An error occurred: {str(e)}")




