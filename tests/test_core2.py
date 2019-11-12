
# Importieren ohne es zu installieren 
import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground


def test_find_lowest_tupel():
    lows = playground.core2.find_lows([(20, 0, 0), (0, 0, 5), (10, 0, 11), (0, 19, 0), (22, 3, 0)])
    assert lows == [(0, 0, 5), (0, 19, 0)]  