import pytest
import pandas as pd
def test_data_nans():
  data = pd.read_csv('/content/RSE_Juelich/day3/reproducible-research-project_day_3/data/clean/clean.csv')
  assert data.isna().sum().sum()==0,  "Data contains missing values"
    
d