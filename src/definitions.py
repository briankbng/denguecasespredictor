from pathlib import Path

# This is your project root path.
ROOT_DIR = Path(__file__).parent.parent

# This is the project models path.
MODELS_DIR = Path.joinpath(ROOT_DIR, 'models')

# This is the project data path.
DATA_DIR = Path.joinpath(ROOT_DIR, 'data')

# This is the project processed data path.
PROCESSED_DATA_DIR = Path.joinpath(DATA_DIR, 'processed')

# The path name of the Decision Tree Regressor Model for the Dengue cases prediction.
# This is a pickle object.
MODEL_DT_REGRESSOR = Path.joinpath(MODELS_DIR, 'DecisionTreeRegressor.model')

# The path name of the Light GBM Model for the Dengue cases prediction.
# This is a pickle object.
MODEL_LT_GBM = Path.joinpath(MODELS_DIR, 'lightGBM_APR_2021')

# The path name of the pkl model for the Dengue cases prediction.
MODEL_PKL = Path.joinpath(MODELS_DIR, 'model.pkl')

# The path name of the forecasted westher data for Dengue case prediction.
# FORECAST_WEATHER_CSV = Path.joinpath(PROCESSED_DATA_DIR, 'forecastedWeatherInfo.csv')
FORECAST_WEATHER_CSV = Path.joinpath(PROCESSED_DATA_DIR, 'forecastedWeatherInfoFull.csv')

# The path name to the cleaned csv data for the model training.
PROCESSED_TRAIN_DATA = Path.joinpath(PROCESSED_DATA_DIR, 'cleaned.csv')
ACTUAL_DATA_CSV = PROCESSED_TRAIN_DATA

# The path name where the definitions reside or the path name of the root package
SRC_ROOT = Path(__file__).parent

# Tha path name of the visualization package
SRC_VIS_ROOT = Path.joinpath(SRC_ROOT, 'visualization')

#
# Use below if you want to import definitions at the module package path level.
#
# import os.path
# import sys

# # Insert the SRC root path to the python system in order to get the definitions 
# # pacakge.
# current_dir = os.path.dirname(__file__)
# parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
# sys.path.insert(0, parent_dir)
# from definitions import SRC_VIS_ROOT
