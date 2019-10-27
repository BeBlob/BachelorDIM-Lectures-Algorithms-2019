"""
Created on Sun Sep 29 21:44:54 2019

@author: BeBlob
"""
import S1_algotools as algotools
import pytest

"""Exo 1
print('Exercice 1, La moyenne est : {moy}'.format(moy = average_above_zero([1,2,3,4,5])))
"""
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

def test_average_above_zero_void_input():
        with pytest.raises(ValueError):
                algotools.average_above_zero([])

"""Exo 1.1
print('Exercice 1.1, La valeur maximale est : {max}'.format(max = max_value_of_table([1,2,3,4,5])))
"""
def test_max_value_of_table_expected_a_list():
        with pytest.raises(TypeError):
                algotools.max_value_of_table('bonjour')

def test_max_value_of_table_expected_a_list_of_numbers():
        with pytest.raises(ValueError):
                algotools.max_value_of_table([1,2,3,'bonjour'])

def test_max_value_of_table():
        assert algotools.max_value_of_table([-1, 1, 2, 3, 4, 5]) == 5 

"""Exo 1.2
print('Exercice 1.2, L\'index de la valeur max est : {max_index} et la valeur max est : {max_value}'.format(max_index = max[1], max_value = max[0]))
"""
def test_max_of_table_expected_a_list():
        with pytest.raises(TypeError):
                algotools.max_of_table('bonjour')

def test_max_of_table_expected_a_list_of_numbers():
        with pytest.raises(ValueError):
                algotools.max_of_table([1,2,3,'bonjour'])

def test_max_of_table():
        assert algotools.max_of_table([-1, 1, 2, 3, 4, 5]) == [5,5]
          
