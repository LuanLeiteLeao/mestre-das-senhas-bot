from exception.validation_exception import MaximumValueExection, NotNullExection


def is_not_null(fild:str,fild_verbose_name:str):
    if not fild or fild.isspace():
        raise NotNullExection(fild_verbose_name)


def is_maximum_value(fild,fild_verbose_name:str,numer_max:int):
    if len(fild) > numer_max:
        raise MaximumValueExection(fild_verbose_name,numer_max)