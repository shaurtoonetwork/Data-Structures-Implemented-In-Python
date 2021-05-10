class SUM:
    def add(self,datatype, *args):
        if datatype == 'int':
            answer = 0

        if datatype == 'str':
            answer = ''

        for x in args:
            answer = answer+x
        
        print(answer)

a = SUM()
a.add('int',2,3,4)
a.add('str','Hi ','Geeks')
