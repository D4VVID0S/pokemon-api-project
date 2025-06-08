import os
import polars as pl
import inspect

def create_csv(df: pl.DataFrame, df_name: str = None, directory: str = "store_data/csv_files"):
    """
    Save a Polars DataFrame to a CSV file, inferring the filename from the variable name if df_name is None.

    Parameters:
        df (pl.DataFrame): The DataFrame to save.
        df_name (str, optional): Desired filename (without extension).
            If None, will infer the variable name from the caller's context.
        directory (str): Directory to save the CSV into.
    """

    # Infer df_name from the calling context if not provided
    if df_name is None:
        frame = inspect.currentframe().f_back
        candidates = [name for name, val in frame.f_locals.items() if val is df]    
        df_name = candidates[0] if candidates else "dataframe"
        
    # Ensure the output directory exists
    os.makedirs(directory, exist_ok=True)

    # Build the full file path
    file_path = os.path.join(directory, f"{df_name}.csv")

    # Write the DataFrame to CSV
    df.write_csv(file_path)
