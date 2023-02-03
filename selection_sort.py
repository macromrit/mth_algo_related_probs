def selection_sort(a : list, order : 'str')->None:
    """This function potentially aims on sorting a list as per the given order. Thus doesn't focus on returning stuff.

    Args:
        a (list): array to be sorted
        order (str): order in which the array's supposed to be sorted ["asc" - ascending, "desc" - descending
    """
    order = order.casefold()
    
    for i in range(0, len(a)):
        holder = i
        for j in range(i, len(a)):
            if (a[holder]>a[j] if order=="asc" else a[holder]<a[j]):
                holder = j
        
        a[i], a[holder] =  a[holder], a[i]
