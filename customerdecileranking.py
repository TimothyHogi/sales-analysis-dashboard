import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

def generate_analytics(df: pd.DataFrame) -> pd.DataFrame:
    # Convert 'deposit' to binary indicator for ease of calculation
    df["deposit_binary"] = df["deposit"].map({"yes": 1, "no": 0})
    
    # Challenge1: Call the function to encode and prepare features
    df_features = encode_and_prepare_features(df)

    # Calculate predicted probability using logistic regression model
    model = LogisticRegression(max_iter=1000)
    
    # Selecting the predictors as specified
    feature_cols = ["age", "balance"] + [col for col in df_features.columns if col.startswith("job_") or col.startswith("marital_")]
    X = df_features[feature_cols]
    y = df["deposit_binary"]

    model.fit(X, y)
    df["predicted_prob"] = model.predict_proba(X)[:, 1]

    # Challenge2: Call the function to process deciles and compute gains
    gain_df = compute_gains_chart(df)

    # Plot Gains Chart / Lift Chart
    plt.figure(figsize=(8, 5))
    plt.plot(gain_df["decile"], gain_df["cumulative_yes"], marker="o", label="Cumulative Yes", color="green")
    # Reference line for random model
    plt.plot([1, 10], [df["deposit_binary"].sum()/10, df["deposit_binary"].sum()], linestyle="--", label="Random Selection")
    plt.xlabel("Decile (1=Highest Prob, 10=Lowest Prob)")
    plt.ylabel("Cumulative Yes")
    plt.title("Gains Chart")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculate summary statistics about stopping bottom 3 deciles (8, 9, 10)
    total_yes = df["deposit_binary"].sum()
    # "Bottom 3" in terms of probability are deciles 8, 9, and 10
    lost_yes = gain_df.loc[gain_df["decile"] >= 8, "yes_in_decile"].sum()
    calls_saved = df.shape[0] * 0.3
    efficiency_gain = calls_saved / lost_yes if lost_yes > 0 else float("inf")

    print(f"Total yes deposits: {total_yes}")
    print(f"Yes deposits lost if we stop calling bottom 3 deciles: {lost_yes}")
    print(f"Total calls saved (30%): {calls_saved}")
    print(f"Efficiency gain (calls saved per yes lost): {efficiency_gain:.2f}")

    return gain_df


def encode_and_prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encode categorical features 'job' and 'marital' into dummy variables.
    """
    # Create dummies for categorical variables
    job_dummies = pd.get_dummies(df['job'], prefix='job')
    marital_dummies = pd.get_dummies(df['marital'], prefix='marital')
    
    # Concatenate dummies with original numerical features
    df_features = pd.concat([df[['age', 'balance']], job_dummies, marital_dummies], axis=1)
    
    return df_features


def compute_gains_chart(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create decile ranks and compute cumulative 'yes' counts.
    """
    # Step 1: Rank probabilities and divide into 10 groups (deciles)
    # Decile 1 should be the highest probability
    df['decile'] = pd.qcut(df['predicted_prob'], 10, labels=range(10, 0, -1))
    
    # Step 2: Group by decile and count the number of actual 'yes' conversions
    gain_df = df.groupby('decile')['deposit_binary'].sum().reset_index()
    gain_df.columns = ['decile', 'yes_in_decile']
    
    # Step 3: Sort by decile (1 to 10) and calculate cumulative sum
    gain_df = gain_df.sort_values('decile').reset_index(drop=True)
    gain_df['cumulative_yes'] = gain_df['yes_in_decile'].cumsum()
    
    return gain_df