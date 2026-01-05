from src.preprocess import preprocess_file
import src.read

def train(df_final):
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.metrics import mean_absolute_percentage_error
    import joblib
    X = df_final.drop(['price'], axis=1)
    Y = df_final['price']

    X_train, X_valid, Y_train, Y_valid = train_test_split(
        X, Y, train_size=0.8, test_size=0.2, random_state=0)
    
    model_RFR = RandomForestRegressor(n_estimators=10)
    model_RFR.fit(X_train, Y_train)
    Y_pred = model_RFR.predict(X_valid)

    mean_absolute_percentage_error(Y_valid, Y_pred)
    joblib.dump(model_RFR, "models/model1.pkl")