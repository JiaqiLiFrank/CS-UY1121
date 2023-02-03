def create_prefix_lists(list):
    final_lst = []
    for index in range(len(list)):
        intermediate_lst = list[0:index+1]
        final_lst.append(intermediate_lst)
    return final_lst