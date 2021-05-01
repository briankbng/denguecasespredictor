import logging
import os
import pickle
from typing import List

import numpy as np

logging.basicConfig(level=logging.INFO)


class CaseReasoner:
    """
    Dengue Case Reasoner

    - receive incoming row of feature
    - load pre-trained model
    - produce predicted case number.

    Parameter
    ----------
    model_path: the pre-trained model path

    Method
    ----------
    predict(row_of_data: list) -> int:
        receive a list of data: [mean_temp, max_temp, min_temp, humidity, mean_rain_fall, mean_wind]

        return: dengue case number prediction, integer

    peroid_predict(row_of_data: List[list], period: int) -> float:
        receive list of list:
            [[mean_temp, max_temp, min_temp, humidity, mean_rain_fall, mean_wind],
             [mean_temp, max_temp, min_temp, humidity, mean_rain_fall, mean_wind],
             .....]
        and the period: int, such as how many a range of day, for example: Mon - Fri: 5 Days

        the length of row_of_data shall be same as period

        return: average dengue cased in this period

    ----------
    """

    def __init__(self, model_path: str):
        if os.path.exists(model_path):
            logging.info("Loading Model")
            self.model = pickle.load(open(model_path, 'rb'))
        else:
            raise FileNotFoundError(
                "Prediction Model path not exist, please check path or model")

    def __repr__(self):
        return f"Dengue Case Reasoner with model: {self.model}."

    def predict(self, row_of_data: list) -> int:
        if isinstance(row_of_data, list) and len(row_of_data) != 1:
            array = np.array(row_of_data).reshape(1, -1)
        else:
            raise ValueError(
                "Input data must a list of feature values, length must > 1")
        return self.model.predict(array)

    # produce range prediction, such as within this week, how many cases.
    def period_predict(self, row_of_data: List[list], period: int) -> float:
        if len(row_of_data) == period:
            period_list = []
            for i in range(period):
                period_list.append(self.model.predict[row_of_data][i])
            return sum(period_list) / len(period_list)
        else:
            raise ValueError('length of row_of_data much same as period')


if __name__ == '__main__':
    model_path = '/Users/johnnylu/Documents/NUS_ISS_Program/denguecasespredictor/models/lightGBM_APR_2021'
    reasoner = CaseReasoner(model_path)
    test_data = [28.69, 34.3, 24.7, 77.55, 0.00, 4.16]
    print(float(reasoner.predict(test_data)))
