"""
@date: 26/09/2019 - 15h
@author: BeBlob
"""

"""Documentation for average_above_zero
@param table:list
get the average of a table above zero
"""
def average_above_zero(table):
    sum = 0
    cmpt_elem = 0
    nb_elem = len(table)

    for cmpt in range(nb_elem) :
        if table[cmpt] > 0 :
            sum = sum + table[cmpt]
            cmpt_elem = cmpt_elem + 1
    moy = sum/cmpt_elem
    return moy

print('La moyenne est : {moy}'.format(moy = average_above_zero([1,2,3,4,5])))