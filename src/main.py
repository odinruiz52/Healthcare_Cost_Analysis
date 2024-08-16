from data_load import main as load_and_clean_data
from eda_visual import main as eda_visualization

def main():
    # Step 1: Load and clean the data
    load_and_clean_data()

    # Step 2: Perform EDA and visualize
    eda_visualization()

if __name__ == "__main__":
    main()
