from exception.validation_exception import MaximumValueExection, NotNullExection


def is_not_null(fild,fild_verbose_name:str):
    if not fild:
        raise NotNullExection(fild_verbose_name)


def is_maximum_value(fild,numer_max:int):
    if fild > numer_max:
        raise MaximumValueExection(fild_verbose_name)