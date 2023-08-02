import pandas as pd
from sklearn.model_selection import train_test_split

def prep_HR_churn_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values (if any)
    # Example: df.fillna(0, inplace=True)

    # Encode categorical variables (if any)
    # Example: label_encoder = LabelEncoder()
    #          df['category_column'] = label_encoder.fit_transform(df['category_column'])

    # Rename attributes
    df.rename(columns={'YearsAtCompany': 'Tenure',
                       'Attrition': 'Churn'}, inplace=True)

    # Convert 'Churn' column to boolean (1 for Yes and 0 for No)
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Define the mapping of numerical values to corresponding labels for education
    education_mapping = {1: 'High School', 2: 'Some College', 3: "Bachelor's Degree", 4: "Master's Degree", 5: 'Doctorate Degree'}

    # Map the numerical values to their corresponding labels for education
    df['Education'] = df['Education'].map(education_mapping)

    return df

def split_data(df):
    # Split the data into features (X) and target (y)
    X = df.drop('Churn', axis=1)
    y = df['Churn']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    # Replace 'path/to/your/Data_Hr_Analytics_S3.csv' with the actual full file path to your dataset file
    file_path = '/Users/miattas/codeup-data-science/Employee-Churn-Prediction/Data_Hr_Analytics_S3.csv'

    # Prepare the data
    df = prep_HR_churn_data(file_path)

    # Split the data
    X_train, X_test, y_train, y_test = split_data(df)