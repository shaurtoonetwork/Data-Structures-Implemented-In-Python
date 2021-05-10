class GFG1: 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG1)') 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG1:', b) 
    
    
class GFG2(GFG1): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG2)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG2:', b) 
        super().sub_GFG(b + 1) 
    
class GFG3(GFG2): 
    def __init__(self): 
        print('HEY !!!!!! GfG I am initialised(Class GEG3)') 
        super().__init__() 
    
    def sub_GFG(self, b): 
        print('Printing from class GFG3:', b) 
        super().sub_GFG(b + 1) 
    

if __name__ == '__main__': 
    gfg = GFG3()  
    gfg.sub_GFG(10)