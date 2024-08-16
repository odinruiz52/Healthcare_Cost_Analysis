import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Load the cleaned dataset
    df = pd.read_csv('./data/healthcare_cost_cleaned.csv')

    # Print dataset summary
    logging.info("Dataset Summary:")
    logging.info(df.describe(include='all'))

    # Set the overall aesthetic style for the plots
    sns.set(style="whitegrid", palette="muted")

    # Bar Plot of Average Total Discharges by State
    plt.figure(figsize=(15, 8))
    state_avg_discharges = df.groupby('Provider State')['Total Discharges'].mean().sort_index()
    sns.barplot(x=state_avg_discharges.index, y=state_avg_discharges.values)
    plt.title('Average Total Discharges by State', fontsize=18)
    plt.xlabel('State', fontsize=14)
    plt.ylabel('Average Total Discharges', fontsize=14)
    plt.xticks(rotation=90, fontsize=12)
    plt.show()

    # Updated Visualization: Average Total Payments and Average Medicare Payments by DRG
    # Select top 10 DRGs by total discharges
    top_n_drg = df.groupby('DRG Definition')['Total Discharges'].sum().nlargest(10).index

    # Filter the dataset to include only the top 10 DRGs
    df_top_drg = df[df['DRG Definition'].isin(top_n_drg)]

    # Calculate average total payments and average Medicare payments for each DRG
    drg_summary = df_top_drg.groupby('DRG Definition').agg({
        'Average Total Payments': 'mean',
        'Average Medicare Payments': 'mean'
    })

    # Create a dual bar and line plot
    fig, ax1 = plt.subplots(figsize=(14, 8))

    # Bar plot for Average Total Payments
    sns.barplot(x=drg_summary.index, y=drg_summary['Average Total Payments'], ax=ax1)
    ax1.set_xlabel('DRG Definition', fontsize=14)
    ax1.set_ylabel('Average Total Payments ($)', fontsize=14, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_xticks(range(len(drg_summary.index)))  # Ensure the correct number of ticks
    ax1.set_xticklabels(drg_summary.index, rotation=45, ha='right', fontsize=10)

    # Line plot for Average Medicare Payments
    ax2 = ax1.twinx()
    ax2.plot(drg_summary.index, drg_summary['Average Medicare Payments'], color='green', marker='o')
    ax2.set_ylabel('Average Medicare Payments ($)', fontsize=14, color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.title('Average Total Payments and Average Medicare Payments by DRG', fontsize=16)
    plt.tight_layout()
    plt.show()

    # Boxplot of Charges by State
    plt.figure(figsize=(15, 8))
    sns.boxplot(x='Provider State', y='Average Covered Charges', data=df)
    plt.title('Average Covered Charges by State', fontsize=18)
    plt.xlabel('State', fontsize=14)
    plt.ylabel('Average Covered Charges', fontsize=14)
    plt.xticks(rotation=90, fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

    # Scatter Plot of Discharges vs Payments by Zip Code
    plt.figure(figsize=(12, 8))
    sns.scatterplot(x='Total Discharges', y='Average Total Payments', 
                    size='Total Discharges', hue='Provider Zip Code', 
                    palette='viridis', sizes=(20, 200), data=df, alpha=0.6)

    plt.title('Discharges vs Payments by Zip Code', fontsize=18)
    plt.xlabel('Total Discharges', fontsize=14)
    plt.ylabel('Average Total Payments', fontsize=14)
    plt.legend(title='Zip Code', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
