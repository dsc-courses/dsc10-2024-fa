test = {   'name': 'q0_3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> 'Year' in tswift.columns and 'Release Date' not in tswift.columns # Make sure you are adding just a Year column, not a Release Date column.\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> isinstance(tswift.iloc[0].get('Year'), numbers.Integral) # Make sure years are stored as ints, not strings!\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}