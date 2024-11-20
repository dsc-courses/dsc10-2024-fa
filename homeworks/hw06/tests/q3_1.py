test = {   'name': 'q3_1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> label_sweet("fruit, sweet, nutty") == \'Sweet\'\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> label_sweet("creamy, semisweet, caramel") == \'Not Sweet\'\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> labeled.shape == (2693, 10)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> list(labeled.columns) == ['Company (Manufacturer)', 'Company Location', 'Review Date', 'Country of Bean Origin', 'Specific Bean Origin or Bar "
                                               "Name', 'Cocoa Percent', 'Ingredients', 'Characteristics', 'Rating', 'Sweetness'] # Name the new column 'Sweetness'\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(labeled.get('Sweetness').unique() == np.array(['Not Sweet', 'Sweet'])) # Make sure the new column's values are either `Sweet` or `Not "
                                               'Sweet`\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
