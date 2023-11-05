from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import templates_user
from templates_user import *


def fill_document(doc):
    """Add a section, a subsection and some text to the document.

    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section("A section")):
        doc.append("Some regular text and some ")
        doc.append(italic("italic text. "))

        with doc.create(Subsection("A subsection")):
            doc.append("Also some crazy characters: $&#{}")


if __name__ == "__main__":
    # Basic document
    doc = Document("work")

    # doc.preamble.append(border)
    doc.preamble.append(Command("usepackage", r"pgf"))
    doc.preamble.append(Command("usepackage", r"pgfpages"))
    doc.preamble.append(
        Command(
            "pgfpagesdeclarelayout",
            r"boxed",
            extra_arguments=[Command("edef"), Command("pgfpageoptionborder", "0pt")],
        )
    )
    doc.generate_pdf()
    doc.generate_tex()
