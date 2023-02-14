# DEPS:
from jiwer import cer

# Code:
class Helper:
    def cer(i, to_compare):
        o = cer(to_compare, i)
        return o # Value between 0 and 1, smaller is better ;)