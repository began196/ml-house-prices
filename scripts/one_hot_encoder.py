from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def onehotencode_data(df):
    # Identify categorical columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Initialize OneHotEncoder
    encoder = OneHotEncoder(sparse=False, drop=None)

    # Fit and transform the categorical columns
    encoded_cols = encoder.fit_transform(df[categorical_cols])

    # Create DataFrame with encoded columns
    encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(categorical_cols))

    # Drop original categorical columns and concatenate encoded columns
    df = df.drop(categorical_cols, axis=1)
    df_encoded = pd.concat([df, encoded_df], axis=1)

    return(df_encoded)