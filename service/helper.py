

def object_as_dict(obj):
    if isinstance(obj, list):
        return [an_obj._asdict() for an_obj in obj]
    else:
        return obj._asdict()


def object_as_list(obj):
    if isinstance(obj, list) or isinstance(obj, tuple):
        tmp = []
        for an_obj in obj:
            tmp = tmp + object_as_list(an_obj)
        return tmp
    else:
        return [obj]
