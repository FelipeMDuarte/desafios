def text_formating(text, line_length=41):
    formated_line = []
    split_paragraphs = text.split("\n\n")
    with open('strings/output-file.txt', "w") as file:
        for paragraph in split_paragraphs:
            split_text = paragraph.split(" ")
            first_next_line = None
            for x in split_text:
                if first_next_line:
                    formated_line.append(first_next_line)
                    first_next_line = None
                if len(" ".join(formated_line+[x])) < line_length:
                    formated_line.append(x)
                else:
                    first_next_line = x
                    insert_line(file, formated_line, line_length)
                    formated_line = []
            left_out_to_insert = formated_line or [first_next_line]
            insert_line(file, left_out_to_insert, line_length)
            formated_line = []
            file.write("\n")


def insert_line(file, formated_line, line_length):
    formated_line[-1] = formated_line[-1] + "\n"
    justified_line = justifying_line(" ".join(formated_line), line_length)
    file.write(justified_line)


def justifying_line(line, line_length):
    len_line = len(line) if line[-1] != '\n' else len(line)
    if len_line < line_length:
        spaces_to_add = line_length-len_line
        new_line = ""
        while spaces_to_add > 0:
            new_line, spaces_to_add = add_spaces(line, spaces_to_add)
            line = new_line
        return new_line
    return line


def add_spaces(line, spaces_to_add):
    new_line = ""
    if line.count(' ') == 0:
        new_line = " "*spaces_to_add+line
        spaces_to_add = 0
    for x in line:
        if x == " " and spaces_to_add > 0:
            new_line = new_line + "  "
            spaces_to_add = spaces_to_add - 1
        else:
            new_line = new_line + x
    return new_line, spaces_to_add


text_input = """In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, 'Let there be light,' and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light 'day,' and the darkness he called 'night.' And there was evening, and there was morning - the first day."""

text_formating(text_input, 60)
