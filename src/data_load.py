import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load the dataset from a specified file path.
    Args:
    - file_path (str): The path to the dataset file.
    
    Returns:
    - DataFrame: Loaded dataset as a pandas DataFrame.
    """
    try:
        logging.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        raise e

def clean_column_names(df):
    """
    Clean column names by trimming spaces.
    Args:
    - df (DataFrame): The dataset to clean.
    
    Returns:
    - DataFrame: Dataset with trimmed column names.
    """
    logging.info("Trimming spaces from column names.")
    df.columns = df.columns.str.strip()
    return df

def clean_monetary_columns(df, columns):
    """
    Clean monetary columns by removing '$' and ',' and converting to float.
    Args:
    - df (DataFrame): The dataset to clean.
    - columns (list): List of column names to clean.
    
    Returns:
    - DataFrame: Dataset with cleaned monetary columns.
    """
    logging.info("Cleaning monetary columns.")
    for column in columns:
        df[column] = df[column].replace('[\$,]', '', regex=True).astype(float)
    return df

def check_missing_values(df):
    """
    Check for any missing values in the dataset.
    Args:
    - df (DataFrame): The dataset to check.
    
    Returns:
    - Series: A series indicating the count of missing values in each column.
    """
    logging.info("Checking for missing values.")
    return df.isnull().sum()

def save_cleaned_data(df, output_path):
    """
    Save the cleaned dataset to a specified file path.
    Args:
    - df (DataFrame): The dataset to save.
    - output_path (str): The path to save the cleaned dataset.
    """
    logging.info(f"Saving cleaned data to {output_path}")
    df.to_csv(output_path, index=False)

def main():
    # Print a message to confirm running script
    print("Script has started executing...")

    # Define file paths
    input_file = './data/healthcare_cost.csv'
    output_file = './data/healthcare_cost_cleaned.csv'

    # Load the dataset
    df = load_data(input_file)

    # Clean the dataset
    df = clean_column_names(df)
    monetary_columns = ['Average Covered Charges', 'Average Total Payments', 'Average Medicare Payments']
    df = clean_monetary_columns(df, monetary_columns)

    # Display the updated data types and check for missing values
    logging.info("\nUpdated Data Types:")
    logging.info(df.dtypes)
    missing_values = check_missing_values(df)
    logging.info("\nMissing Values in the Dataset:")
    logging.info(missing_values)

    # Display the first few rows of the cleaned dataset for verification
    logging.info("\nFirst 5 rows of the cleaned dataset:")
    logging.info(df.head())

    # Save the cleaned dataset
    save_cleaned_data(df, output_file)

if __name__ == "__main__":
    main()
