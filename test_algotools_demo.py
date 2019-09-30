"""
Created on Sun Sep 29 21:44:54 2019

@author: BeBlob
"""
import S1_algotools_teacherdemo as algotools
import pytest

def inc_(x):
    return x+1

def test_inc():
    assert inc_(3)==5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1/0

"""Exo 1
print('Exercice 1, La moyenne est : {moy}'.format(moy = average_above_zero([1,2,3,4,5])))
"""
def test_average_above_zero_divide_by_zero():
        with pytest.raises(ZeroDivisionError):
                algotools.average_above_zero([])

def test_average_above_zero_expected_a_list():
        with pytest.raises(TypeError):
                algotools.average_above_zero('bonjour')

def test_average_above_zero_expected_a_list_of_numbers():
        with pytest.raises(ValueError):
                algotools.average_above_zero([1,2,3,'bonjour'])

def test_average_above_zero_expected_positive_numbers():
        with pytest.raises(ValueError):
                algotools.average_above_zero([-1,-2,-3,-4,-5])
        
def test_average_above_zero():
        assert algotools.average_above_zero([-1, 1, 2, 3, 4, 5]) == 3

"""Exo 1.2
print('Exercice 1.1, La valeur maximale est : {max}'.format(max = max_value_of_table([1,2,3,4,5])))
"""

