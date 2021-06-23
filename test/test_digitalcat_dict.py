# Copyright (c) 2017 Thomas Thurman
# See LICENSE.txt for details.

from pathlib import Path

from plover_build_utils.testing import dictionary_test

from plover_digitalcat_dictionary import DigitalCATDictionary


@dictionary_test
class TestDigitalCATDictionary:

    DICT_CLASS = DigitalCATDictionary
    DICT_EXTENSION = 'dct'
    DICT_REGISTERED = True
    DICT_LOAD_TESTS = (
        lambda: (
            'digitalcat-test.dct',
            r'''
            'TKPWHREPB': 'glen',
            'A': 'a',
            # no, I don't know why; it was in the sample dct
            'TK*EB/TK*EB/R-R': '"Debbie \'Do Anything for Hillary\' Wasserman Schultz"',
            'TKEUGZ/AER': 'dictionary',
            'HAOER': 'here',
            'SEZ': 'says',
            'S': 'is',
            'SKW-FRPBLGTS': '{^{A}And}',
            'STKPWHRAEPBG': '{^{Q}What, if anything,^}',
            'SPHAUL': 'small',
            '''
        ),
    )
    DICT_SAMPLE = 'digitalcat-test.dct'

    @staticmethod
    def make_dict(contents):
        path = Path(__file__).parent / contents
        return path.read_bytes()
