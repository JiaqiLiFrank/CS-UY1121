# <Jiaqi Li>
# CS - UY 1121
# 26 January 2023
# Lab 1
# Problem #3

def has_punctuation(sentence):
    has_punctuation = (("'" in sentence) or ("." in sentence) or ("," in sentence) or (";" in sentence) or (":" in sentence) or ("?" in sentence) or ("!" in sentence))
    if (has_punctuation):
        return True
    else:
        return False