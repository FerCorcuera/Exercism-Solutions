from itertools import zip_longest

def transpose(text):
    if text == "":
        return ""

    rows = text.split("\n")
    result = []

    max_len = max(len(row) for row in rows)

    for col in range(max_len):
        new_row = []
        last_real_row = 0

        for r, row in enumerate(rows):
            if col < len(row):
                new_row.append(row[col])
                last_real_row = r
            else:
                new_row.append(" ")

        result.append("".join(new_row[:last_real_row + 1]))

    return "\n".join(result)

    
# from itertools import zip_longest
# def transpose(text):
#     t_matrix = []
#     if text == '':
#         return ''

#     s = '\n'

#     if s not in text:
#         return s.join(text)
    
    
#     mtrx = text.split(s)

#     mx = max([len(x) for x in mtrx])

#     for i in range(len(mtrx)):
#         if len(mtrx[i]) < mx:
#             tail = ' ' * (mx - len(mtrx[i]))
#             mtrx[i] = mtrx[i] + tail


#     for x in zip(*mtrx):
#         # print(x)
#         t_matrix.append(''.join(x))


#     # for x in range(len(t_matrix)):
#     #     t_matrix[x] = t_matrix[x].rstrip()

#     return mtrx
# # s.join(t_matrix)