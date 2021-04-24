from setuptools import find_packages, setup

setup(
    name='DenguePredictor',
    packages=find_packages(),
    version='0.1.0',
    description='Dengue Daily Case Predictor based on daily weather info',
    author='Bai SiHai, Men Jinlong, Ng Kwee Boon',
    license='MIT',
    install_requires=[
        "setuptools~=52.0.0",
        "pandas~=1.2.2",
        "matplotlib~=3.3.4",
        "numpy~=1.19.2",
        "scikit-learn~=0.23.2",
    ]
)
