"""
Plot a thing!
"""


import shapely


def main() -> None:
    """
    Example
    """
    size = (11.5, 9)
    page_width, page_height = size[0] / 4, size[1] / 2
    # pages = [shapely.GeometryCollection([hitomezashi(p, 20, 40)]) for p in np.linspace(0, 0.5, 8)]
    # out = zine(pages, *size, 0.2)
    # out = elkplot.optimize(out, 0.01)
    # elkplot.draw(out)


if __name__ == '__main__':
    main()