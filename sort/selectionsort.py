#!/usr/bin/python3
# -*- coding: utf-8 -*-


def findSmallest(array):
    '''
    查找列表中的最小值下标，并将其下标返回
    :param array: list
    :return: index 最小值的下标
    '''
    smallest = array[0]
    smallest_index = 0
    for a in range(1, len(array)):
        if smallest < array[a]:
            smallest = array[a]
            smallest_index = a
    return smallest_index


def selectionSort(array):
    newArray = []
    for i in range(len(array)):
        smallest_index = findSmallest(array)
        newArray.append(array.pop(smallest_index))
    return newArray


if __name__ == '__main__':
    array = [12, 9, 5, 21, 33, 25, 92, 88]
    print(selectionSort(array))