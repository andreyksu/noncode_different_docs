def first(**kwargs):
    listtOfNamedArgs = ["last_name", "first_name", "username"]
    listGotArgs = kwargs.keys()
    
    if len(listGotArgs) != 3:
        raise KeyError()
    
    for i in listtOfNamedArgs:
        if not (i in listGotArgs):
            raise KeyError()
        
    for l in listtOfNamedArgs:
        if not (isinstance(kwargs[l], str)):
            raise TypeError()
        
        
print(first(last_name=1, first_name="Иван", username="ivanych45"))