from python_template.basic.bit_full_search import bit_full_search


def test_bit_full_search():
    answer_list = []
    answer_list.append([[0], [1]])
    answer_list.append([[0, 0], [0, 1], [1, 0], [1, 1]])
    answer_list.append(
        [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1],
        ]
    )

    assert list(bit_full_search(1)) == answer_list[0]
    assert list(bit_full_search(2)) == answer_list[1]
    assert list(bit_full_search(3)) == answer_list[2]
