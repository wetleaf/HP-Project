import random


def getElem(data, i):
    return_data = [data[k][i] if i < len(data[k]) else "" for k in range(len(data))]
    print(return_data)
    return return_data


def generate_mtf(data, desc, sol_left, sol_right):
    cols = data
    num_cols = len(cols)
    width = 1 / num_cols - 0.05
    col_str = (
        "\\begin{adjustwidth}{1cm}{0cm}\n\\textbf{\\Large "
        + desc
        + "}\\\\\\normalsize\n"
    )
    col_desc = f"p{{{width}\\textwidth}} " * num_cols
    col_str += (
        "\\renewcommand{\\arraystretch}{2.5}\n\\large \\begin{tabular}{@{}"
        + col_desc
        + "@{}}\n"
    )
    # shuffling right column
    right = cols[1]
    lim = len(right)
    extra = 0
    if "" in right:
        lim = right.index("")
        extra = len(right) - lim
    old_indexes = list(range(0, lim))
    print(right)
    combined_lists = list(zip(right[1:lim], old_indexes[1:lim]))
    random.shuffle(combined_lists)
    right_new, old_indexes = zip(*combined_lists)
    right_new = [item for item in right_new]
    # print(combined_lists)
    # print(old_indexes)
    old_indexes = [item for item in old_indexes]
    # print(right_new)
    empty = [""] * extra
    start = [cols[1][0]]
    # print(empty)
    cols[1] = start + right_new + empty
    # changing solution accordingly

    for i in range(len(sol_right)):
        sol_right[i] = chr(old_indexes.index(ord(sol_right[i]) - 96) + 97)

    print(sol_right)
    print(old_indexes)
    print(cols[1])

    # handling indexes of first and second column
    start = 1
    charac = 97
    for i in range(len(max(cols, key=len))):
        ele = getElem(cols, i)
        for j in range(len(ele)):
            if i == 0 and j == 0:
                col_str += f"\\textbf{{{ele[j]}}}"
            elif i == 0:
                col_str += f" & \\textbf{{{ele[j]}}}"
            elif j == 0:
                if len(ele[j]) and ele[j].startswith("<Text>"):
                    col_str += f"\\normalsize({start}) {ele[j][6:-7]}"
                    start += 1
                elif len(ele[j]):
                    col_str += f"\\normalsize({start}) [\\textbf{{{ele[j][7:-8]}}}]"
                    start += 1
            else:
                if len(ele[j]) and ele[j].startswith("<Text>"):
                    col_str += f" & \\normalsize({chr(charac)}) {ele[j][6:-7]}"
                    charac += 1
                elif len(ele[j]):
                    col_str += (
                        f" & \\normalsize({chr(charac)}) [\\textbf{{{ele[j][7:-8]}}}]"
                    )
                    charac += 1
                else:
                    col_str += " & "
        col_str += " \\\\ \n"
    sol_str = ""
    for i in range(len(sol_left)):
        if i != len(sol_left) - 1:
            sol_str += f" \\textbf{{{sol_left[i]}}}:\\textbf{{{sol_right[i]}}} , "
        else:
            sol_str += f" \\textbf{{{sol_left[i]}}}:\\textbf{{{sol_right[i]}}}"

    col_str += (
        "\\end{tabular}\n\\end{adjustwidth}\n\\vfill\n\\begin{flushright}\n\\reflectbox{"
        + sol_str
        + "}\n\\end{flushright}"
    )
    return col_str
