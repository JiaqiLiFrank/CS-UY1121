def int_extractor(*strs):
    final_lst = []
    for str in strs:
        words_lst = str.split()
        for words in words_lst:
            if (words.isdigit()):
                final_lst.append(int(words))
    return final_lst