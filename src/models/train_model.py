import logging
import pickle
from pathlib import Path

# import os
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


def main():
    # X, y = load_data(path='../../data/processed/cleaned.csv')
    ROOT_DIR = Path(__file__).parent.parent.parent
    data_path = Path.joinpath(ROOT_DIR, 'data/processed/cleaned_RF_corrected_MA_Last_LN_added.csv')
    print(data_path)
    X, y = load_data(path=data_path)

    model = train_model(features=X, label=y)
    logging.info("Writing Model to disk")
    # model_path = os.path.realpath(os.path.dirname(__file__)+'/../../models/lightGBM_APR_2021')
    model_path = Path.joinpath(ROOT_DIR, 'models/lightGBM_APR_2021_2')
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    main()
