class Year:
    regex = '[0-9]{4}'
    def to_python(self,value):
        return int(value)

    def to_url(self,value):
        return f'{value:4d}'