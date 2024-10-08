test = {   'name': 'q3_2_2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': ">>> seconds_in_a_decade != 60 * 60 * 24 * 10 * 365 # Close, but not quite! It looks like you didn't account for leap years. See: "
                                               'https://en.wikipedia.org/wiki/Leap_year\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade != 315532800 # 315532800 is wrong, but close. Make sure to account for leap seconds, which are different than leap years! See: '
                                               'https://en.wikipedia.org/wiki/Leap_second\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> seconds_in_a_decade == 315532802 # Bingo! 315532802 is right, by make sure you know how to work it out as an expression.\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
