def mean(num_list):
    #assert type(num_list) == list
    #if len(num_list) == 0:
    #    raise Exception("the list has length of 0")
    #assert len(num_list) != 0                                                                                                                                                                         
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError as detail:
        msg = "must have list of numbers"
        raise TypeError(detail.__str__() + "\n" + msg)
