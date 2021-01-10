

def object_as_dict(obj):
    if isinstance(obj, list):
        return [an_obj._asdict() for an_obj in obj]
    else:
        return obj._asdict()
