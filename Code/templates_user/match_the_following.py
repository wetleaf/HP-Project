def getElem(data, i):
    return_data = [data[k][i] if i < len(data[k]) else "" for k in range(len(data))]
    print(return_data)
    return return_data


def generate_mtf(data, desc):
    cols = data
    num_cols = len(cols)
    width = 1 / num_cols - 0.05
    col_str = (
        "\\begin{adjustwidth}{1cm}{0cm}\n\\textbf{\\Large "
        + desc
        + "}\\\\\\normalsize\n\\vspace{10cm}\n"
    )
    col_desc = f"p{{{width}\\textwidth}} " * num_cols
    col_str += (
        "\\renewcommand{\\arraystretch}{2.5}\n\\large \\begin{tabular}{@{}"
        + col_desc
        + "@{}}\n"
    )
    for i in range(len(max(cols, key=len))):
        ele = getElem(cols, i)
        for j in range(len(ele)):
            if i == 0 and j == 0:
                col_str += f"\\textbf{{{ele[j]}}}"
            elif i == 0:
                col_str += f" & \\textbf{{{ele[j]}}}"
            elif j == 0:
                if ele[j].startswith("<Text>"):
                    col_str += f"\\normalsize {ele[j][6:-7]}"
                else:
                    col_str += f"\\normalsize {ele[j][7:-8]}"
            else:
                if ele[j].startswith("<Text>"):
                    col_str += f" & \\normalsize {ele[j][6:-7]}"
                else:
                    col_str += f" & \\normalsize {ele[j][7:-8]}"
        col_str += " \\\\ \n"

    col_str += "\\end{tabular}\n\\end{adjustwidth}\n"
    print(col_str)
    return col_str
