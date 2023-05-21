import elkplot
import numpy as np
import shapely
from shapely import *

def zine(
        pages: list[shapely.GeometryCollection],
        width: float,
        height: float,
        margin: float) -> shapely.GeometryCollection:
    assert len(pages) == 8
    page_width = width / 4
    page_height = height / 2
    pages = [elkplot.scale_to_fit(page, page_width, page_height, margin) for page in pages]
    pages[0] = affinity.translate(pages[0], page_width, page_height)
    pages[1] = affinity.translate(pages[1], 2 * page_width, page_height)
    pages[2] = affinity.translate(pages[2], 3 * page_width, page_height)
    pages[3] = affinity.rotate(pages[3], 180, origin=(page_width / 2, page_height / 2))
    pages[3] = affinity.translate(pages[3], 3 * page_width, 0)
    pages[4] = affinity.rotate(pages[4], 180, origin=(page_width / 2, page_height / 2))
    pages[4] = affinity.translate(pages[4], 2 * page_width, 0)
    pages[5] = affinity.rotate(pages[5], 180, origin=(page_width / 2, page_height / 2))
    pages[5] = affinity.translate(pages[5], page_width, 0)
    pages[6] = affinity.rotate(pages[6], 180, origin=(page_width / 2, page_height / 2))
    pages[7] = affinity.translate(pages[7], 0, page_height)
    layers = []
    for page in pages:
        for i, layer in enumerate(shapely.get_parts(page)):
            if len(layers) < i + 1:
                layers.append([])
            layers[i].append(layer)
    layers = [shapely.union_all(layer) for layer in layers]
    return shapely.GeometryCollection(layers)


def main():
    size = (11.5, 9)
    page_width, page_height = size[0] / 4, size[1] / 2
    pages = [LineString(Point(0, 0), Point(1, 1)) for i in range(0, 8)]
    out = zine(pages, *size, 0.2)
    out = elkplot.optimize(out, 0.01)
    elkplot.draw(out)


if __name__ == "__main__":
    main()
