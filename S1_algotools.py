"""
@date: 26/09/2019 - 15h
@author: BeBlob
"""
import numpy as np

"""Documentation for average_above_zero
@param table:list
@return moy:float
@error can't divide by zero, can't give another type than list as input, can't give a table with cells of another type than number
get the average of a table above zero
"""
def average_above_zero(table):

    if not(isinstance(table, list)):
        raise TypeError('average_above_zero, expected a list as input')

    nb_elem = len(table)

    if nb_elem == 0 :
        raise ValueError('average_above_zero, void table')

    sum = 0
    diviseur = 0

    for cmpt in range(nb_elem) :
        if not(isinstance(table[cmpt], (int,float))):
            raise ValueError('average_above_zero, expected a list of numbers')
        if table[cmpt] > 0 :
            sum = sum + table[cmpt]
            diviseur = diviseur + 1

    if sum == 0 :
        raise ValueError('average_above_zero, no positive number')

    moy = sum/(diviseur)

    return moy

"""Documentation for max_value_of_table
@param table: list
@return max: float
@error can't give another type than list as input, can't give a table with cells of another type than number
get the max value of a table
"""
def max_value_of_table(table):

    if not(isinstance(table, list)):
        raise ValueError('max_value_of_table, expected a list as input')
    if not(isinstance(table[0], (int,float))):
        raise ValueError('max_value_of_table, expected a list of numbers')

    nb_elem = len(table)
    max_elem = 0

    for cmpt in range(nb_elem) :
        if table[cmpt] > max_elem :
            max_elem = table[cmpt]
            
    return max_elem

"""Documentation for max_of_table
@param table: list
@return max: tuple
@error can't give another type than list as input, can't give a table with cells of another type than number
get the max value of a table and its index
"""
def max_of_table(table):

    if not(isinstance(table, list)):
        raise ValueError('max_of_table, expected a list as input')
    if not(isinstance(table[0], (int,float))):
        raise ValueError('max_of_table, expected a list of numbers')

    nb_elem = len(table)
    max_elem = 0
    max_elem_index = 0

    for cmpt in range(nb_elem) :
        if table[cmpt] > max_elem :
            max_elem = table[cmpt]
            max_elem_index = cmpt
            
    return max_elem,max_elem_index

"""Documentation for reverse_table
@param table: list
@return table_reversed: list
@error can't give another type than list as input
get the table input reversed
"""
def reverse_table(table):

    if not(isinstance(table, list)):
        raise ValueError('max_of_table, expected a list as input')

    nb_elem = len(table)
    cmpt = 1

    while cmpt < nb_elem+1 :
        table.append(table[nb_elem-cmpt])
        cmpt = cmpt + 1
            
    return table[nb_elem:]

"""Documentation for roi_bbox
@param input_image: numpy array
@return output_matrix: numpy array
get a bounding box from a 2D image
"""

"""TODO
def roi_bbox(table):

    matrix = np.zeroes((10,10), dtype = np.int32)
    matrix[3:6, 4:8] = np.ones((3,4), dtype = np.int32)
    for idrow in range(matrix.reshape[0]):
        for idcol in range(matrix.reshape[1])
            pixVal = matrix[idrow, idcol]

    for row in range(matrix.reshape[0])
        if matrix[row]
"""

'''TESTS'''

"""Exo 1
"""
print('Exercice 1, La moyenne est : {moy}'.format(moy = average_above_zero([1,2,3,4,5])))

"""Exo 1.1
"""
print('Exercice 1.1, La valeur maximale est : {max}'.format(max = max_value_of_table([1,2,3,4,5])))

"""Exo 1.2
"""
max = max_of_table([1,2,3,4,5])
print('Exercice 1.2, L\'index de la valeur max est : {max_index} et la valeur max est : {max_value}'.format(max_index = max[1], max_value = max[0]))

"""Exo 2
"""
print('Exercice 2, Le tableau inversé est : {table}'.format(table = reverse_table([1,2,3,4,5])))

"""Exo 3
"""
