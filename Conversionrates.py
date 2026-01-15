import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency


def generate_analytics(data: pd.DataFrame) -> None:
    """Generates analytics on conversion rates for 'deposit' across several categories and
    performs Chi-Square tests and visualization of 'Conversion Lift' by job type."""

    # Overall conversion rate
    overall_conversion = (data["deposit"] == "yes").mean()

    # Challenge1: Calculate conversion rates by job, education, and marital
    data_by_category = analyze_conversion_by_category(data)

    # Challenge2: Perform Chi-Square testing on job and education vs deposit
    chi2_results = perform_chi_square_tests(data)

    print("Conversion Rates by Category:\n", data_by_category)
    print(
        f"\nChi-Square Test Results:\nJob: p-value={chi2_results['job_p_value']:.5f}, Education: p-value={chi2_results['education_p_value']:.5f}"
    )

    # Calculate Conversion Lift for visualization
    # We join back to the job index specifically for the plot
    job_lift = data_by_category["job_conversion"] / overall_conversion

    plt.figure(figsize=(10, 6))
    job_lift.dropna().plot(kind="bar", color='skyblue', edgecolor='black')
    plt.axhline(1, color='red', linestyle='--', label='Baseline (Overall)')
    plt.title("Conversion Lift by Job Type")
    plt.ylabel("Conversion Lift relative to overall")
    plt.xlabel("Job")
    plt.legend()
    plt.tight_layout()
    plt.show()


def analyze_conversion_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the percentage of 'yes' outcomes in 'deposit' for 'job', 'education', and 'marital' categories.
    """
    categories = ['job', 'education', 'marital']
    results = {}

    for cat in categories:
        # Calculate mean where 'yes' = 1 and 'no' = 0
        conv_rate = df.groupby(cat)['deposit'].apply(lambda x: (x == 'yes').mean())
        results[f"{cat}_conversion"] = conv_rate

    # Combine into a single DataFrame; indices will be the category names (e.g., 'admin.', 'technician')
    return pd.concat(results, axis=1)


def perform_chi_square_tests(df: pd.DataFrame) -> dict:
    """
    Perform Chi-Square tests of independence to check the relationship of 'job' and 'education'
    with 'deposit'.
    """
    p_values = {}
    
    for col in ['job', 'education']:
        # Create a contingency table (cross-tabulation)
        contingency_table = pd.crosstab(df[col], df['deposit'])
        
        # chi2_contingency returns: chi2, p, dof, expected
        _, p, _, _ = chi2_contingency(contingency_table)
        p_values[f"{col}_p_value"] = p

    return p_values