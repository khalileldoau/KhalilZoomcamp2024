import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    li = []
    for i in range(1, 10):
        url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-0'+str(i)+'.parquet'
        df = pd.read_parquet(url)
        li.append(df)
    for i in [10, 11, 12]:
        url ='https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-'+str(i)+'.parquet'
        df = pd.read_parquet(url)
        li.append(df)
    
    return pd.concat(li, axis=0, ignore_index=True)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
