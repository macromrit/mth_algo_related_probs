def bubble_sort(a: list, order : 'str')->None:
    """sorting an array as per the given order using bubble sort algo. Thus doesn't focus on returning stuff.

    constraints:
            ->order should be in ["asc", "dsc"] # not case sensitive 
            
    Args:
        a (list): array to be sorted
        order (str): order in which the array's supposed to be sorted ["asc" - ascending, "desc" - descending
    """
    
    order = order.casefold()
    
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if (a[j]>a[j+1] if order=="asc" else a[j]<a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
