test = {   'name': 'q1_3',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> isinstance(avg_age,bpd.DataFrame) and avg_age.shape == (502, 3) and 'Average_Age' in avg_age.columns and baby.shape == (371890, 5) # Don't change "
                                               'the original baby DataFrame.\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.isclose(avg_age[(avg_age.get('Name') == 'John') & (avg_age.get('Gender') == 'F')].get('Average_Age').iloc[0], 69.84475534939398)\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
