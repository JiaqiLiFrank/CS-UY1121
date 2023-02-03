def string_encoder(string):
    final_lst = []
    for letter in string:
        original_len = len(string)
        string = string.lstrip(letter)
        count = original_len - len(string)
        final_lst.append([letter,count])
        for counts in final_lst:
            if counts[1]==0:
                final_lst.remove(counts)
    return final_lst
def string_decoder(list):
    final_str = ""
    for counts in list:
        final_str += counts[0]*counts[1]
    return final_str