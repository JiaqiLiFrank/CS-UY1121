def has_punctuation(sentence):
    has_punctuation = (("'" in sentence) or ("." in sentence) or ("," in sentence) or (";" in sentence) or (":" in sentence) or ("?" in sentence) or ("!" in sentence))
    if (has_punctuation):
        return True
    else:
        return False
