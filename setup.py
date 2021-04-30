from setuptools import find_packages, setup

requires = [
    "setuptools~=51.3.3",
    "pandas~=1.2.3",
    "matplotlib~=3.3.4",
    "numpy~=1.19.5",
    "scikit-learn~=0.23.2",
    "click~=7.1.2",
    "lightgbm~=3.2.1",
    "flask~=1.1.2",
    "datetime~=4.3",
    "bokeh~=2.3.1",
    "typing~=3.7.4.3",
    "pathlib~=1.0.1"
]

setup (
    name='DenguePredictor',
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
