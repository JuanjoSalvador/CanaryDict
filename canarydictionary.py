'''
    Pysarao - TDD
    author: Juanjo Salvador
'''

class canarydictionary():  
    '''
        Busca el término 'word' dentro del diccionario y devuelve su resultado
    '''
    def searchword(self, word):
        dictionary = {
            'millo': 'maiz',
            'papa': 'patata',
            'baifo': 'cabra',
            'godo': 'miguel',
        }

        if word in dictionary:
            return dictionary[word]

pass