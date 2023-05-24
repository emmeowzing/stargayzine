# import elkplot
# import numpy as np
# import shapely
# from shapely import *
# import csv
# import json





# def main():
#     size = (11.5, 9)
#     page_width, page_height = size[0] / 4, size[1] / 2
#     constellations = {}
#     with open('constellations.csv', newline='\n') as csvfile:
#         starreader = csv.reader(csvfile, delimiter=',', quotechar='"')
#         for row in list(starreader)[1:]:
#             raw_points = zip(json.loads(row[1]), json.loads(row[2]))
#             points = []
#             for (ra, dec) in raw_points:
#                 points.append([ra, dec])
#             constellations[row[0]] = MultiPoint(points).buffer(0.1)
#     c = constellations
#     pages = [c["CAS"], c["COM"], c["COM"], c["COM"], c["COM"], c["COM"], c["COM"], c["COM"]]
#     out = zine(pages, *size, 0.2)
#     out = elkplot.optimize(out, 0.01)
#     elkplot.draw(out, preview_dpi=80)
