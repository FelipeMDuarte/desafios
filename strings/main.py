def text_formating(text: str, line_length: int = 41, justify: bool = False):
    try:
        formated_line = []
        split_paragraphs = text.split("\n\n")
        with open('strings/outputs/output-file.txt', "w") as file:
            for paragraph in split_paragraphs:
                words = paragraph.split(" ")
                first_next_line = None
                formated_line, first_next_line = make_line(
                    words, line_length, file, justify, first_next_line)
                left_out_to_insert = formated_line or [first_next_line]
                insert_line(file, left_out_to_insert, line_length, justify)
                formated_line = []
                file.write("\n")
    except BaseException as e:
        print(f'Unknown error running text formating: {str(e)}')
        raise e


def make_line(words, line_length, file, justify=False, first_next_line=None):
    formated_line = []
    for word in words:
        if first_next_line:
            formated_line.append(first_next_line)
            first_next_line = None
        if len(" ".join(formated_line + [word])) < line_length:
            formated_line.append(word)
        else:
            first_next_line = word
            insert_line(file, formated_line, line_length, justify)
            formated_line = []
    return formated_line, first_next_line


def insert_line(file, formated_line: list, line_length: int, justify: bool):
    formated_line[-1] = formated_line[-1] + "\n"
    line_to_insert = " ".join(formated_line)
    if justify:
        line_to_insert = justifying_line(" ".join(formated_line), line_length)
    file.write(line_to_insert)


def justifying_line(line: str, line_length: int):
    len_line = len(line) if line[-1] != '\n' else len(line)
    if len_line < line_length:
        spaces_to_add = line_length-len_line
        new_line = ""
        while spaces_to_add > 0:
            new_line, spaces_to_add = add_spaces(line, spaces_to_add)
            line = new_line
        return new_line
    return line


def add_spaces(line: str, spaces_to_add: int):
    new_line = ""
    if line.count(' ') == 0:
        new_line = " "*spaces_to_add+line
        spaces_to_add = 0
        return new_line, spaces_to_add
    for x in line:
        if x == " " and spaces_to_add > 0:
            new_line = new_line + "  "
            spaces_to_add = spaces_to_add - 1
        else:
            new_line = new_line + x
    return new_line, spaces_to_add


text_input = """In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.

And God said, 'Let there be light,' and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light 'day,' and the darkness he called 'night.' And there was evening, and there was morning - the first day."""


def testing():
    errors = []
    for x in range(10, 60):
        try:
            text_formating(text_input, x, justify=False)
        except BaseException as e:
            errors.append(f"error with line lenght = {x}")
    print(errors)


text_formating(text_input, 41, justify=True)
