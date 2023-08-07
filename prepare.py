import pandas as pd
from sklearn.model_selection import train_test_split



# def prep_HR_churn_data(file_path):
#     # Load the dataset
#     df = pd.read_csv(file_path)

#     # Drop duplicates
#     df.drop_duplicates(inplace=True)

#     # Handle missing values (if any)
#     # Example: df.fillna(0, inplace=True)

#     # Encode categorical variables (if any)
#     # Example: label_encoder = LabelEncoder()
#     #          df['category_column'] = label_encoder.fit_transform(df['category_column'])

#     # Rename attributes
#     df.rename(columns={'YearsAtCompany': 'Tenure',
#                        'Attrition': 'Churn'}, inplace=True)

#     # Convert 'Churn' column to boolean (1 for Yes and 0 for No)
#     df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

#     # Define the mapping of numerical values to corresponding labels for education
#     education_mapping = {1: 'High School', 2: 'Some College', 3: "Bachelor's Degree", 4: "Master's Degree", 5: 'Doctorate Degree'}

#     # Map the numerical values to their corresponding labels for education
#     df['Education'] = df['Education'].map(education_mapping)

#     return df

def prep_HR_churn_data(HR_df):
    # Load the dataset
    # HR_df = pd.read_csv(file)

    # Drop duplicates
    HR_df.drop_duplicates(inplace=True)

    #Handle missing values (if any)
    HR_df.fillna(0, inplace=True)

    # Encode categorical variables (if any)
    # Example: label_encoder = LabelEncoder()
    #          df['category_column'] = label_encoder.fit_transform(df['category_column'])

    # Rename attributes
    HR_df.rename(columns={'YearsAtCompany': 'Tenure'}, inplace=True)

    # Convert 'Attrition' column to boolean (1 for Yes and 0 for No)
    HR_df['Yes_Attrition'] = np.where(HR_df['Attrition'] == 'Yes', 1, 0).astype(int)
    
    
    # Assuming you have your DataFrame named 'df', and you want to keep only the specified columns
    selected_df = HR_df[['Age','Yes_Attrition', 'Tenure', 'Education']]

    return selected_df
#-------------- SPLIT-------

def split_selected(selected_df):
    ''' The below functions were created in regression exercises and will be aggregated to make a master clean_data function for the final 
        report
    '''
    train_validate, selected_test = train_test_split(selected_df, test_size=0.2, random_state=123)
    selected_train, selected_validate = train_test_split(train_validate, test_size=0.25, random_state=123)
    
    print(f'Train shape: {selected_train.shape}')
    print(f'Validate shape: {selected_validate.shape}')
    print(f'Test shape: {selected_test.shape}')
    return selected_train, selected_validate, selected_test

def X_y_split(selected_train, selected_validate, selected_test):
    # Splitting the data into X and Y to take out the data with churn and those without 
    selected_X_train = selected_train.select_dtypes(exclude=['object']).drop(columns=['Yes_Attrition'])
    selected_y_train = selected_train.select_dtypes(exclude=['object']).Yes_Attrition
    
    selected_X_validate = selected_validate.select_dtypes(exclude=['object']).drop(columns['Yes_Attrition'])
    selected_y_validate = selected_validate.select_dtypes(exclude=['object']).Yes_Attrition
    
    selected_X_test = selected_test.select_dtypes(exclude=['object']).drop(columns=['Yes_Attrition'])
    selected_y_test = selected_test.select_dtypes(exclude=['object']).Yes_Attrition
    return selected_X_train, selected_y_train, selected_X_validate, selected_y_validate, selected_X_test, selected_y_test

def selected_features(df):
    # Select the features you want to observe
    selected_features = ['Age', 'Education', 'Tenure', 'Attrition']
    selected_df = df[selected_features]
    return selected_df

def save_selected_features_to_csv(csv_name, df):
    # Save the new DataFrame to a new CSV file
    df.to_csv(csv_name, index=False)



