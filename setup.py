from setuptools import find_packages, setup

requires = [
    "setuptools~=52.0.0",
    "pandas~=1.2.2",
    "matplotlib~=3.3.4",
    "numpy~=1.19.2",
    "scikit-learn~=0.23.2",
    "click~=7.1.2",
    "lightgbm~=3.1.1",
    "flask~=0.12.2"
]
setup(
    name='DenguePredictor',
    packages=find_packages(),
    version='0.1.0',
    description='Dengue Daily Case Predictor based on weather info',
    author='Bai SiHai, Men Jinlong, Ng Kwee Boon, Lu Zhiping',
    author_email='<You actual e-mail address here>',
    license='MIT',
    keywords='DengueCasesPredictor',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
