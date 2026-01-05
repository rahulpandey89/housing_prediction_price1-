import src.read
import joblib
model = joblib.load("./training/models/model1.pkl")
def predict(df):
    """
    df: preprocessed DataFrame ready for prediction
    returns: predicted values
    """
    X = df.drop(['price'], axis=1)
    predictions = model.predict(X)
    return predictions