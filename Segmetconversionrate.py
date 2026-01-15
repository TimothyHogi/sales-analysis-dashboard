import pandas as pd

def generate_analytics(data: list[dict]) -> dict:
    df = pd.DataFrame(data)

    # Challenge1: Extract and calculate conversion rate for 'Blue-collar' + 'Married' + 'Loan=Yes' segment
    df_segment1 = get_blue_collar_married_loan_segment(df)
    conversion_rate1 = df_segment1['deposit'].eq('yes').mean()

    # Challenge2: Extract and calculate conversion rate for 'Campaign > 5' + 'Poutcome = failure' segment
    df_segment2 = get_campaign_gt5_poutcome_failure_segment(df)
    conversion_rate2 = df_segment2['deposit'].eq('yes').mean()

    # Segment3: 'Student/Retired' + 'Single'
    segment3_mask = (
        (df['job'].isin(['student', 'retired'])) & (df['marital'] == 'single')
    )
    df_segment3 = df.loc[segment3_mask]
    conversion_rate3 = df_segment3['deposit'].eq('yes').mean()

    # Calculate Cost per Acquisition (CPA) for each segment
    # Assume cost = sum of campaign*duration as proxy
    cpa1 = (df_segment1['campaign'] * df_segment1['duration']).sum() / df_segment1['deposit'].eq('yes').sum()
    cpa2 = (df_segment2['campaign'] * df_segment2['duration']).sum() / df_segment2['deposit'].eq('yes').sum()
    cpa3 = (df_segment3['campaign'] * df_segment3['duration']).sum() / df_segment3['deposit'].eq('yes').sum()

    # Estimate blanket 30% cut savings on total cost
    total_cost = (df['campaign'] * df['duration']).sum()
    blanket_cut_savings = total_cost * 0.3

    # Calculate savings by removing segments 1 and 2 only
    cost_segments_1_2 = (
        (df_segment1['campaign'] * df_segment1['duration']).sum()
        + (df_segment2['campaign'] * df_segment2['duration']).sum()
    )

    results = {
        'conversion_rates': {
            'Blue-collar_Married_LoanYes': conversion_rate1,
            'CampaignGt5_PoutcomeFailure': conversion_rate2,
            'StudentRetired_Single': conversion_rate3,
        },
        'cost_per_acquisition': {
            'Blue-collar_Married_LoanYes': cpa1,
            'CampaignGt5_PoutcomeFailure': cpa2,
            'StudentRetired_Single': cpa3,
        },
        'cost_savings_estimate': {
            'blanket_30_percent_cut': blanket_cut_savings,
            'remove_segments_1_2_only': cost_segments_1_2,
            'savings_difference': blanket_cut_savings - cost_segments_1_2,
        },
    }

    return results


def get_blue_collar_married_loan_segment(df: pd.DataFrame) -> pd.DataFrame:
    """Filter DataFrame to segment: job = 'blue-collar', marital = 'married', loan = 'yes'.
    Return filtered DataFrame for conversion and CPA calculation."""

    # Challenge1: Implement filtering for blue-collar, married, loan=yes segment
    def get_blue_collar_married_loan_segment(df: pd.DataFrame) -> pd.DataFrame:
    """Filter DataFrame to segment: job = 'blue-collar', marital = 'married', loan = 'yes'."""
    # Create the filter mask
    mask = (df['job'] == 'blue-collar') & \
           (df['marital'] == 'married') & \
           (df['loan'] == 'yes')
    
    # Return the subset of the dataframe
    return df.loc[mask].copy()


def get_campaign_gt5_poutcome_failure_segment(df: pd.DataFrame) -> pd.DataFrame:
    """Filter DataFrame to segment: campaign > 5 and poutcome = 'failure'.
    Return filtered DataFrame for conversion and CPA calculation."""

    # Challenge2: Implement filtering for campaign >5 and poutcome = failure segment
    def get_campaign_gt5_poutcome_failure_segment(df: pd.DataFrame) -> pd.DataFrame:
    """Filter DataFrame to segment: campaign > 5 and poutcome = 'failure'."""
    # Create the filter mask
    mask = (df['campaign'] > 5) & (df['poutcome'] == 'failure')
    
    # Return the subset of the dataframe
    return df.loc[mask].copy()