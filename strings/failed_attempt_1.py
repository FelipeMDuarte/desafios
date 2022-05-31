def text_formating(text, line_length=40, justified=False):
    formatted_text = ''
    break_line = 0
    for x in range(0, len(text), line_length):
        start_line = x + break_line
        break_line = line_length
        if text[line_length+1] != " ":
            for y in range(line_length, line_length-x, -1):
                if text[y] == " ":
                    break_line = y
                    break
        formatted_text = formatted_text + text[start_line:start_line+break_line] + "\n"

    with open('strings/output-file.txt', "w") as file:
        file.write(formatted_text)


text_input = """In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.
And God said, 'Let there be light,' and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light 'day,'and the darkness he called 'night.' And there was evening, and there was morning - the first day.
"""

text_formating(text_input)
