# Healthcare Cost Analysis Project

## Project Overview

This project analyzes healthcare costs across various providers and states in the United States. The analysis focuses on understanding the distribution of costs, identifying patterns, and providing insights into healthcare spending.

## Project Structure

- `data/`: Contains the raw and cleaned datasets.
  - `healthcare_cost_cleaned.csv` # Cleaned dataset
  - `healthcare_cost.csv` # Original dataset
- `env/`: Virtual environment files
- `src/`: Source code files
  - `cost_analysis.py` # Cost analysis script
  - `data_load.py` # Data loading and cleaning script
  - `eda_visual.py` # Exploratory data analysis and visualization script
  - `main.py` # Main script to execute all tasks
- `reports/`: Contains the final report and Jupyter Notebook with analysis.
  - `Healthcare_Cost_Analysis_Report.ipynb` # Jupyter Notebook with analysis and visuals
- `README.md`: Project documentation

## Installation

To set up the environment and install the required packages, follow these steps:

1. **Clone the Repository**:

git clone <repository-url>
cd Healthcare_Cost_Analysis

2. **Create a Virtual Environment**:

python3 -m venv env
source env/bin/activate

3. **Install the Required Packages**:

pip install -r requirements.txt

## Data Source

The dataset used in this project is publicly available and provides information on healthcare costs for different providers across the United States. The data includes variables such as `DRG Definition`, `Provider State`, `Total Discharges`, `Average Covered Charges`, `Average Total Payments`, and `Average Medicare Payments`.

## Data Cleaning

The original dataset was cleaned to remove unnecessary spaces, convert monetary values to numeric types, and ensure there were no missing values. The cleaned dataset is saved as `healthcare_cost_cleaned.csv` in the `data` directory.

## Usage

To run the analysis and generate the visualizations:

1. **Run the Data Loading and Cleaning Script**:

python src/data_load.py

2. **Perform Exploratory Data Analysis and Visualization**:

python src/eda_visual.py

3. **Conduct Cost Analysis**:

python src/cost_analysis.py

## Visualizations

The project includes several visualizations to help understand the data:

1. **Average Total Discharges by State**: A bar plot showing the average number of discharges per state.
2. **Average Total Payments and Average Medicare Payments by DRG**: A dual bar and line graph comparing total payments and Medicare payments for the top 10 DRGs by total discharges.
3. **Average Covered Charges by State**: A boxplot illustrating the variation in covered charges across different states.
4. **Discharges vs Payments by Zip Code**: A scatter plot showing the relationship between total discharges, average payments, and zip codes, highlighting area-based differences in financial outcomes.

These visualizations provide insights into the variability of healthcare costs by state, DRG, and geographic location.

## Conclusion

This project offers a detailed analysis of healthcare costs across the United States, providing valuable insights for both technical and non-technical audiences. The visualizations and analysis are designed to be accessible to a wide audience, from high school students to top-level executives.

## Next Steps

Further analysis could involve:

- Deep dives into specific states or providers.
- Predictive modeling to estimate healthcare costs based on various factors.
- Extending the analysis to include more recent data or additional variables.

## License

This project is open-source and available under the [MIT License](LICENSE).
