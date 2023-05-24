"""
Helper functions for paging some number of frames.
"""


from typing import List, Any

import shapely


def zine(pages: List[shapely.GeometryCollection], width: float, height: float, margin: float) -> shapely.GeometryCollection:
    """

    Args:
        pages (List[shapely.GeometryCollection]): _description_
        width (float): _description_
        height (float): _description_
        margin (float): _description_

    Returns:
        shapely.GeometryCollection: _description_
    """
    assert len(pages) == 8
    page_width = width / 4
    page_height = height / 2
    # pages = [elkplot.scale_to_fit(page, page_width, page_height, margin) for page in pages]
    # pages[0] = affinity.translate(pages[0], page_width, page_height)
    # pages[1] = affinity.translate(pages[1], 2 * page_width, page_height)
    # pages[2] = affinity.translate(pages[2], 3 * page_width, page_height)
    # pages[3] = affinity.rotate(pages[3], 180, origin=(page_width / 2, page_height / 2))
    # pages[3] = affinity.translate(pages[3], 3 * page_width, 0)
    # pages[4] = affinity.rotate(pages[4], 180, origin=(page_width / 2, page_height / 2))
    # pages[4] = affinity.translate(pages[4], 2 * page_width, 0)
    # pages[5] = affinity.rotate(pages[5], 180, origin=(page_width / 2, page_height / 2))
    # pages[5] = affinity.translate(pages[5], page_width, 0)
    # pages[6] = affinity.rotate(pages[6], 180, origin=(page_width / 2, page_height / 2))
    # pages[7] = affinity.translate(pages[7], 0, page_height)
    layers: List[Any] = []
    for page in pages:
        for i, layer in enumerate(shapely.get_parts(page)):
            if len(layers) < i + 1:
                layers.append([])
            layers[i].append(layer)
    layers = [shapely.union_all(layer) for layer in layers]
    return shapely.GeometryCollection(layers)