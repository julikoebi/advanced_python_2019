
def find_peaks(list_of_intensities):
    """Find peaks

    Find local maxima for a given list of intensities. 
    Intensities are defined as local maxima if the 
    intensities of the elements in the list before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    max_value = 0
    list_of_maxima = []
    for pos, element in enumerate(list_of_intensities):
        if pos == 0:
            continue
        if pos == len(list_of_intensities) - 1:
            continue
        if list_of_intensities[pos - 1] < element > list_of_intensities[pos + 1]:
            max_value = element
            list_of_maxima.append(max_value)
    return list_of_maxima


def find_lows(list_of_colors):
    """Find lows

    Find local minima for a given list of tupels of intensities. 
    Tupels of Intensities are defined as local minima if the 
    intensities of the elements in the tupel before and after 
    are smaller than the peak we want to determine.

    Args:
        list_of_intensities (list of floats or ints): a list of
            numeric values

    Returns:
        list of floats: list of the identified local maxima

    Note:
        This is just a place holder for the TDD part :)
    """
    list_of_sums = []
    for tupel in list_of_colors:
        summed_up = 0
        for element in tupel:
            summed_up += element
        list_of_sums.append(summed_up)

    min_value = 0
    list_of_minima = []
    for pos, element in enumerate(list_of_sums):
        if pos == 0:
            continue
        if pos == len(list_of_sums) - 1:
             continue
        if list_of_sums[pos - 1] > element < list_of_sums[pos + 1]:
            min_pos = pos
            minima = list_of_colors[min_pos]
            list_of_minima.append(minima)
    
    return list_of_minima