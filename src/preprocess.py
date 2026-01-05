
def preprocess_file(dataset):
    from src.read import read_file
    from sklearn.preprocessing import OneHotEncoder
    import src.read
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_percentage_error
    import joblib
    obj = (dataset.dtypes == 'object')
    object_cols = list(obj[obj].index)
    print("Categorical variables:",len(object_cols))

    int_ = (dataset.dtypes == 'int')
    num_cols = list(int_[int_].index)
    print("Integer variables:",len(num_cols))

    fl = (dataset.dtypes == 'float')
    fl_cols = list(fl[fl].index)
    print("Float variables:",len(fl_cols))
    new_dataset = dataset.dropna()
    
    s= (new_dataset.dtypes == 'object')
    object_cols = list(s[s].index)
    print("Categorical variables:")
    print(object_cols)
    print('No. of. categorical features: ', len(object_cols))
    
    OH_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    OH_cols = pd.DataFrame(OH_encoder.fit_transform(new_dataset[object_cols]))
    OH_cols.index = new_dataset.index
    OH_cols.columns = OH_encoder.get_feature_names_out()
    df_final = new_dataset.drop(object_cols, axis=1)
    df_final = pd.concat([df_final, OH_cols], axis=1)
    
    return df_final