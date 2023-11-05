from pylatex import Document, LongTabu
from pylatex.utils import bold


def test(doc):
    with doc.create(
        LongTabu("X[l] X[2l] X[r] X[r] X[r]", row_height=1.5)
    ) as data_table:
        data_table.add_row(
            ["date", "description", "debits($)", "credits($)", "balance($)"],
            mapper=bold,
            color="lightgray",
        )
        data_table.add_empty_row()
        data_table.add_hline()
        row = ["2016-JUN-01", "Test", "$100", "$1000", "-$900"]
        for i in range(30):
            if (i % 2) == 0:
                data_table.add_row(row, color="lightgray")
            else:
                data_table.add_row(row)
