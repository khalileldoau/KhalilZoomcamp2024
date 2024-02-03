if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = (data.columns.str.replace(' ', '_').str.lower())
    print('Rows with zero passengers: ',data['passenger_count'].isin([0]).sum(),
    ' Rows with zero trip distance: ', data['trip_distance'].isin([0]).sum()
     ) 
    return data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0) ]


@test
def test_output(output, *args):
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passangers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'
    assert output['vendorid'].isin([1,2]).sum() == len(output)


