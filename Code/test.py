import re
import templates_user
import readJSON
from templates_user import match_the_following
from readJSON import reader

search_pattern = r"%insert problem"
search_question = r"QUESTION 0"
topic = "SEASONS"
question_type = "MATCH THE FOLLOWING"
path = "./json_outputs/1.txt"
data, name, desc = reader.read(path)
replacement = match_the_following.generate_mtf(data, desc)

with open("test.tex", "r") as file:
    with open("./worksheets/1.tex", "w") as file2:
        content = file.read()
        content = content.replace(search_pattern, replacement)
        content = content.replace(search_question, topic)
        file2.write(content)
