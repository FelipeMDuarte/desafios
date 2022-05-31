from unittest.mock import MagicMock, patch, call
from strings.main import text_formating, insert_line, justifying_line, add_spaces, text_input


def test_add_spaces():
    new_line, spaces_to_add = add_spaces('aaa bbb ccc', 3)
    assert new_line == 'aaa  bbb  ccc'
    assert spaces_to_add == 1
    new_line, spaces_to_add = add_spaces('aaa bbb ccc', 2)
    assert new_line == 'aaa  bbb  ccc'
    assert spaces_to_add == 0
    new_line, spaces_to_add = add_spaces('aaa bbb ccc', 1)
    assert new_line == 'aaa  bbb ccc'
    assert spaces_to_add == 0
    new_line, spaces_to_add = add_spaces('aaa', 2)
    assert new_line == '  aaa'
    assert spaces_to_add == 0


@patch('strings.main.add_spaces', return_value=('aaa   bbb   ccc', 0))
def test_justifying_line(mock_add_spaces):
    result = justifying_line('aaa bbb ccc', 15)
    assert result == 'aaa   bbb   ccc'
    mock_add_spaces.assert_called_once_with('aaa bbb ccc', 4)


@patch('strings.main.justifying_line', return_value='aaa   bbb   ccc')
def test_insert_line(mock_justifying_line):
    file = MagicMock()
    insert_line(file, ['aaa', 'bbb', 'ccc'], 15, True)
    mock_justifying_line.assert_called_once_with(" ".join(['aaa', 'bbb', 'ccc'])+"\n", 15)
    file.write.assert_called_once_with(mock_justifying_line())


@patch('strings.main.insert_line')
@patch('strings.main.open')
def test_text_formating(mock_open, mock_insert_line):
    text_formating('aaa bbb ccc', 15, True)
    mock_insert_line.assert_called_once_with(
        mock_open().__enter__(), ['aaa', 'bbb', 'ccc'], 15, True)
    text_formating(text_input, 41, True)
    mock_insert_line.assert_has_calls([
        call(mock_open().__enter__(), ['In', 'the', 'beginning', 'God', 'created', 'the', 'heavens'], 41, True),
        call(mock_open().__enter__(), ['and', 'the', 'earth.', 'Now', 'the', 'earth', 'was'], 41, True),
        call(mock_open().__enter__(), ['formless', 'and', 'empty,', 'darkness', 'was', 'over'], 41, True),
        call(mock_open().__enter__(), ['the', 'surface', 'of', 'the', 'deep,', 'and', 'the', 'Spirit'], 41, True),
        call(mock_open().__enter__(), ['of', 'God', 'was', 'hovering', 'over', 'the', 'waters.'], 41, True),
        call(mock_open().__enter__(), ['And', 'God', 'said,', "'Let", 'there', 'be', "light,'", 'and'], 41, True),
        call(mock_open().__enter__(), ['there', 'was', 'light.', 'God', 'saw', 'that', 'the', 'light'], 41, True),
        call(mock_open().__enter__(), ['was', 'good,', 'and', 'he', 'separated', 'the', 'light'], 41, True),
        call(mock_open().__enter__(), ['from', 'the', 'darkness.', 'God', 'called', 'the', 'light'], 41, True),
        call(mock_open().__enter__(), ["'day,'", 'and', 'the', 'darkness', 'he', 'called'], 41, True),
        call(mock_open().__enter__(), ["'night.'", 'And', 'there', 'was', 'evening,', 'and'], 41, True),
        call(mock_open().__enter__(), ['there', 'was', 'morning', '-', 'the', 'first', 'day.'], 41, True)
    ])
