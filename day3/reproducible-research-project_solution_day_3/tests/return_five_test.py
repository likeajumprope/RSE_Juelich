import sys
import os
sys.path.append("content/RSE_Juelich/day3/reproducible-research-project_solution_day_3/src")  # so Python can find your src folder

from my_return import return_five

def test_return_five():
    assert return_five() == 5