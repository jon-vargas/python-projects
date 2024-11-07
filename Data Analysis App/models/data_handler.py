import pandas as pd

def summarize_data(data):
    df = pd.DataFrame(data)
    return df.describe()
