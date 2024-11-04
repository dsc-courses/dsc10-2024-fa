test = {   'name': 'q4_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> isinstance(city_means, bpd.DataFrame) and set(city_means.columns) == set(['price'])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> list(city_means.index) == ['Saint Louis', 'Jacksonville', 'Tucson', 'Dallas', 'Atlanta', 'San Diego', 'Los Angeles', 'New York City']\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(city_means.get('price') <= city_means.loc['New York City'].get('price')) # Make sure that New York City has the highest average listing "
                                               'price!\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
