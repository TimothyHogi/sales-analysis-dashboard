import pandas as pd
import matplotlib.pyplot as plt


def generate_analytics(data: pd.DataFrame) -> None:
    """Analyze campaign conversion rates and high campaign call statistics."""
    # Convert 'deposit' to binary for easier calculation
    data["deposit_binary"] = data["deposit"].map({"yes": 1, "no": 0})

    # Challenge1: Calculate conversion rates for each campaign count
    data = calculate_conversion_rates(data)

    # Plotting the conversion rates line chart
    plt.figure(figsize=(10, 6))
    plt.plot(data["campaign"], data["conversion_rate"], marker="o")
    plt.title("Conversion Rate by Campaign Number")
    plt.xlabel("Campaign Number")
    plt.ylabel("Conversion Rate")
    plt.grid(True)
    plt.show()

    # Challenge2: Calculate total calls and "yes" percentage when campaign > 5
    total_calls, yes_percentage = analyze_high_campaign_calls(data)

    print(f"Total calls with campaign > 5: {total_calls}")
    print(f"Percentage of 'yes' deposits for campaign > 5: {yes_percentage:.2f}%")


def calculate_conversion_rates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate conversion rates (percentage of 'yes')
    for each value of the 'campaign' column.

    Returns a DataFrame grouped by 'campaign' with a 'conversion_rate' column.
    """
    # Challenge1: Implement calculate_conversion_rates to handle conversion rate calculation
    def calculate_conversion_rates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate conversion rates (percentage of 'yes')
    for each value of the 'campaign' column.
    """
    # Group by campaign and calculate the mean of the binary 'yes' values
    conversion_df = df.groupby("campaign")["deposit_binary"].mean().reset_index()
    
    # Rename the column to match what the plotting code expects
    conversion_df.columns = ["campaign", "conversion_rate"]
    
    return conversion_df


def analyze_high_campaign_calls(df: pd.DataFrame) -> tuple:
    """
    Calculate total number of calls where 'campaign' > 5 and the
    percentage of those calls that resulted in a 'yes' deposit.

    Returns a tuple: (total_calls, yes_percentage)
    """
    # Challenge2: Implement analyze_high_campaign_calls to compute counts and percentages
    def analyze_high_campaign_calls(df: pd.DataFrame) -> tuple:
    """
    Calculate total number of calls where 'campaign' > 5 and the
    percentage of those calls that resulted in a 'yes' deposit.
    """
    # Filter the dataframe for rows where campaign is greater than 5
    high_campaign_df = df[df["campaign"] > 5]
    
    total_calls = len(high_campaign_df)
    
    # Avoid division by zero if there are no calls above 5
    if total_calls > 0:
        yes_percentage = high_campaign_df["deposit_binary"].mean() * 100
    else:
        yes_percentage = 0.0
        
    return total_calls, yes_percentage
