"""
@date: 26/09/2019 - 15h
@author: BeBlob
"""

"""Documentation for average_above_zero
@param table:list
@return moy:float
@error can't divide by zero, can't give another type than list as input, can't give a table with cells of another type than number
get the average of a table above zero
"""
def average_above_zero(table):

    if not(isinstance(table, list)):
        raise ValueError('average_above_zero, expected a list as input')

    nb_elem = len(table)

    if nb_elem == 0 :
        raise ValueError('average_above_zero, can\'t divide by zero')
    if not(isinstance(table[0], (int,float))):
        raise ValueError('average_above_zero, expected a list of numbers')

    sum = 0
    cmpt_elem = 0

    for cmpt in range(nb_elem) :
        if table[cmpt] > 0 :
            sum = sum + table[cmpt]
            cmpt_elem = cmpt_elem + 1

    moy = sum/cmpt_elem

    return moy

"""Documentation for max_value_of_table
@param table: list
@return max: float
@error can't give another type than list as input, can't give a table with cells of another type than number
get the max of a table
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
get the max of a table
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

"""Exo 1.3
"""
