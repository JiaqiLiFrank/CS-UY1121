def multiply_matrix(mtx1, mtx2):
    mtx1_cl = 0
    mtx2_cl = 0
    mtx2_rw = 0
    mtx1_rw = 0
    mtx3 = []
    mtx3_cl = 0
    mtx3_rw = 0
    final_mtx = [[0]*len(mtx2[0]) for i in range(len(mtx1))]
    mtx4 = []
    for num in mtx1[0]:
        mtx1_cl += 1
    for lsts in mtx2:
        mtx2_rw += 1
    for num in mtx1:
        mtx1_rw += 1
    for lsts in mtx2[0]:
        mtx2_cl += 1
    if mtx1_cl == mtx2_rw:
        for index1 in range(mtx1_rw):
            for index2 in range(mtx2_cl):
                for index3 in range(mtx2_rw):
                    final_mtx[index1][index2] += mtx1[index1][index3]*mtx2[index3][index2]
        return final_mtx
    else:
        return "ERROR"