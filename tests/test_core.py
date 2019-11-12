
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


# Eigentlicher Test

def test_find_peaks():
    peaks = playground.core.find_peaks([0, 2, 1])
    assert peaks == [2]  

def test_find_two_peaks():
    peaks = playground.core.find_peaks([0, 2, 1, 0, 2, 1])
    assert peaks == [2, 2] 

def test_find_peaks_max_edge():
    peaks = playground.core.find_peaks([2, 1, 1])
    assert peaks == [] 
    
def test_find_peaks_empty_list():
    peaks = playground.core.find_peaks([])
    assert peaks == []  
    
def test_find_lowest_tupel():
    lows = playground.core.find_lows([(20, 0, 0), (0, 0, 5), (10, 0, 11), (0, 19, 0), (22, 3, 0)])
    assert lows == [(0, 0, 5), (0, 19, 0)]  