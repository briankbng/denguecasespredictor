import logging
import pickle

import pandas as pd
from lightgbm import LGBMRegressor

logging.basicConfig(level=logging.INFO)


def load_data(path):
    logging.info("Loading Data")
    df = pd.read_csv(path)
    df.date = pd.to_datetime(df.date)
    df = df.set_index(['date'])
    y = df.pop('cases')
    return df, y


def train_model(features, label):
    logging.info("Training Model")
    lgb = LGBMRegressor(
        num_leaves=120,
        max_depth=7,
        n_estimators=1000,
        learning_rate=0.005
    )
    lgb.fit(features, label)

    return lgb


def main(data_path: str, model_path: str):
    X, y = load_data(path=data_path)
    model = train_model(features=X, label=y)
    logging.info("Writing Model to disk")
    pickle.dump(model, open(model_path, 'wb'))


if __name__ == '__main__':
    main(data_path='../../data/processed/cleaned_RF_corrected_MA_Last_LN_added.csv',
         model_path='../../models/lightGBM_MAY_2021')
