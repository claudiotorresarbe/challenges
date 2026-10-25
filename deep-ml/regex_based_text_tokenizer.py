import re

def tokenize_text(text: str) -> list:
    txt = text.replace('--',' --')
    txt = txt.replace('\n',' ').replace('\t',' ')
    txt = re.findall(r"""[,. :;?!_"()']|[^,. :;?!_"()']+""", txt)
    for x in txt:
        if x == ' ':
            ind = txt.index(x)
            txt.pop(ind)
    return txt
