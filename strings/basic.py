def text_formating(text, line_length=41, justified=False):
    formatted_text = []
    split_paragraphs = text.split("\n\n")
    with open('strings/output-file.txt', "w") as file:
        for paragraph in split_paragraphs:
            split_text = paragraph.split(" ")
            first_next_line = None
            for x in split_text:
                if first_next_line:
                    formatted_text.append(first_next_line)
                    first_next_line = None
                if len(" ".join(formatted_text+[x])) < line_length:
                    formatted_text.append(x)
                else:
                    first_next_line = x
                    formatted_text[-1] = formatted_text[-1]+"\n"
                    file.write(" ".join(formatted_text))
                    formatted_text = []
            file.write(" ".join(formatted_text))
            formatted_text = []
            file.write("\n\n")


text_input = """In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, 'Let there be light,' and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light 'day,'and the darkness he called 'night.' And there was evening, and there was morning - the first day.
"""

text_formating(text_input)
