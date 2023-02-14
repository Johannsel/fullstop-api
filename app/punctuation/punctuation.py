# DEPS:
import re
from .deepmultilingualpunctuation import PunctuationModel

# Custom methods:
from .sanitizers import pre_sanitizer, post_sanitizer

# Code:
class Punctuation:
    # Sanitize input and process with own hybrid solution
    def hybrid(i, fstop_threshold):
        i = pre_sanitizer(i)
        model = PunctuationModel()
        stt_split = re.split('\s+', i)
        
        stt = []
        for j in stt_split:
            list = re.split(r'(?=\.|\,|\?|\:|\!)', j)[:2]
            if len(list)==2:
                stt.append(list)
            else:
                list.append("0")
                stt.append(list)

        fstop = model.predict(model.preprocess(i))

        proc = []
        for c, j in enumerate(fstop):
            if j[2]<fstop_threshold:
                x = stt[c]
                j[1]=x[1]
            proc.append(j)

        o = ""
        for j in proc:
            if j[1]=="0":
                o = str(o) + str(j[0]) + " "
            if j[1]==".":
                o = str(o) + str(j[0]) + ". "
            if j[1]==",":
                o = str(o) + str(j[0]) + ", "
            if j[1]=="?":
                o = str(o) + str(j[0]) + "? "
            if j[1]=="-":
                o = str(o) + str(j[0]) + "- "
            if j[1]==":":
                o = str(o) + str(j[0]) + ": "

        o = o.strip()

        return post_sanitizer(o)

    # Sanitize input and process with fullstop
    def fstop(i):
        i = pre_sanitizer(i)
        model = PunctuationModel()
        o = model.restore_punctuation(i)
        return post_sanitizer(o)

    # Keep the STT punctuation but sanitize input
    def stt(i):
        o = i
        return o