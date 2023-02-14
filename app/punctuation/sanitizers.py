# Deps:
import re

# Code:
def pre_sanitizer(i):
    o = re.sub(r'(?<=\d)\.',"", i)
    return o

def post_sanitizer(i):
    o = i
    return o