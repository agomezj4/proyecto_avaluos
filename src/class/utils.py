import pandas as pd
import joblib

class Utils:

    def load_from_xlsx(self, path):
        return pd.read_excel(path)

    def save_to_xlsx(self, df, path):
        df.to_excel(path, index=False)

    def load_from_parquet(self, path):
        return pd.read_parquet(path)

    def save_to_parquet(self, df, path):
        df.to_parquet(path, index=False)
