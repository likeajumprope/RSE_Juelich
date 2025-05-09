import pytest
import pandas as pd
def test_number_of_rows(input):
    data = pd.read_csv(input)
    assert len(data) == 909, "Data does not have the expected number of rows"