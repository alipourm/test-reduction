
class IllegalOperation(Exception):
    def __init__(self):
        pass


import math

class Coverage():
    
    def __init__(self, coverage):
        if type(coverage) is not list:
            raise IllegalOperation('it must be a list')
        self.coverage = coverage


    def __str__(self):
        return ''.join(map(str, self.coverage))
        

    def isSimilar(self, other, percentage):
        pairs = zip(self.coverage, other.coverage)
        result = map(lambda (fst,snd): 1 if fst == 1 and snd == 1 else 0, pairs)
        p = sum(result)*100./sum(other.coverage)  
        if p >= percentage:
            return True
        else:
            return False

        
    def contains(self, other):
        if len(self.coverage) != len(other.coverage):
            raise IllegalOperation("Illegal operation: subtraction of lists with different sizes")
        for i in range(len(self.coverage)):
            if other.coverage[i] == 1 and self.coverage[i] == 0:
                return False
        return True

    """
    def diff_percent(self, other):
        diff = self - other
        diffTotal = sum(diff.coverage)
        return float(diffTotal)*100. / sum(self.coverage)

    def diff_val(self, other):
        diff = self - other
        diffTotal = sum(diff.coverage)
        return diffTotal
    """
    def __add__(self, other):
        if len(self.coverage) != len(other.coverage):
            raise IllegalOperation("Illegal operation: subtraction of lists with different sizes")
        pairs = zip(self.coverage, other.coverage)
        result = map(lambda (fst,snd): 1 if fst == 1 or snd == 1 else 0, pairs)
        return Coverage(result)

    def __sub__(self, other):
        if len(self.coverage) != len(other.coverage):
            raise IllegalOperation("Illegal operation: subtraction of lists with different sizes")
        pairs = zip(self.coverage, other.coverage)
        result = map(lambda x: 1 if x[0] == 1 and x[1] == 0 else 0, pairs)
        return Coverage(result)


