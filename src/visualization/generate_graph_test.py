
import os.path
import sys
from bokeh.plotting import show

# Insert the SRC root path to the python system in order to get the definitions 
# pacakge.
current_dir = os.path.dirname(__file__)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)
from definitions import SRC_VIS_ROOT, ACTUAL_DATA_CSV

from generate_graph import GenerateGraph

if __name__ == '__main__':

    plot = GenerateGraph(ACTUAL_DATA_CSV)

    path = SRC_VIS_ROOT
    # path = '/home/ai-user/Documents/Demo'
    os.chdir(path)

    predCases=plot.getPredDengueCases('2020-10-01', '2020-10-05') # Simulate Pred cases

    # To show shorter date ranges, we can show weather conditions
    p = plot.generateGraphForActualAndPredictedDengueCases(
        # '2020-10-01',   # startDate YYYY-MM-DD
        # '2020-10-10',   # endDate YYYY-MM-DD
        '2020-10-01',  # startDate YYYY-MM-DD
        '2020-10-05',  # endDate YYYY-MM-DD
        predCases,      # List of Predicted Cases
        bool(True))     # Show weather conditions

    # show(p)

    # To show longer date ranges, it is best to hide weather conditions
    p = plot.generateGraphForActualAndPredictedDengueCases(
        '2020-09-01',   # startDate YYYY-MM-DD
        '2020-10-30',   # endDate YYYY-MM-DD
        #'2020-10-01',  # startDate YYYY-MM-DD
        #'2020-10-05',  # endDate YYYY-MM-DD
        predCases,      # List of Predicted Cases
        bool(True))     # Hide weather conditions

    show(p)

    ####################################################


