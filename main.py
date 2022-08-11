# %%
X = "x"
Y = "y"
C = "c"
GREEN = "G"
RED = "R"


# %%
def euclidean_distance(point_1, point_2):
    return ((point_1[X] - point_2[X]) ** 2 + (point_1[Y] - point_2[Y]) ** 2) ** 0.5


# %%
def get_points_from_lists(coordinates_x, coordinates_y, colors):
    return [{X: x, Y: y, C: c} for x, y, c in zip(coordinates_x, coordinates_y, colors)]


# %%
def sort_by_distance_descending(points, center):
    return sorted(
        points, key=lambda point: euclidean_distance(point, center), reverse=True
    )


def get_greens_vs_reds_scala(points):
    greens = sum([1 for point in points if point[C] == GREEN])
    reds = len(points) - greens
    return reds - greens


# %%
def solution(coordinates_x, coordinates_y, colors, center):
    distance = lambda point: euclidean_distance(point, center)
    points = sort_by_distance_descending(
        get_points_from_lists(coordinates_x, coordinates_y, colors), center
    )
    greens_vs_reds_scala = get_greens_vs_reds_scala(points)

    while True:
        if greens_vs_reds_scala == 0:
            break
        elif len(points) == 1:
            points.pop()
            break

        while len(points) >= 2:
            point = points.pop(0)
            greens_vs_reds_scala += 1 if point[C] == GREEN else -1
            if distance(point) != distance(points[0]):
                break
    return len(points)
