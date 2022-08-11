import main

X = "x"
Y = "y"
C = "c"
GREEN = "G"
RED = "R"
EXPECTED = "expected"
CENTER = {X: 0, Y: 0}


def test_euclidean_distance():
    assert main.euclidean_distance({X: 3, Y: 4}, CENTER) == 5


def test_get_points_from_lists():
    assert main.get_points_from_lists([1, 2], [3, 4], "GR") == [
        {X: 1, Y: 3, C: "G"},
        {X: 2, Y: 4, C: "R"},
    ]


def test_sort_by_distance():
    assert main.sort_by_distance_descending([{X: 1, Y: 1}, {X: 2, Y: 2}], CENTER) == [
        {X: 2, Y: 2},
        {X: 1, Y: 1},
    ]


def test_greens_vs_reds_scala():
    assert main.get_greens_vs_reds_scala([{C: GREEN}, {C: RED}, {C: RED}]) == 1


def test_solution():
    assert main.solution([4, 0, 2, -2], [4, 1, 2, -3], "RGRR", CENTER) == 2
    assert main.solution([1, 1, -1, -1], [1, -1, 1, -1], "RGRG", CENTER) == 4
    assert main.solution([1, 0, 0], [0, 1, -1], "GGR", CENTER) == 0
    assert main.solution([5, -5, 5], [1, -1, -3], "GRG", CENTER) == 2
    assert (
        main.solution(
            [3000, -3000, 4100, -4100, -3000],
            [5000, -5000, 4100, -4100, 5000],
            "RRGRG",
            CENTER,
        )
        == 2
    )
