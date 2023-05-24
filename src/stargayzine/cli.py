"""
Call stargayzine with different constellations.
"""


from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def main() -> None:
    """
    Parse arguments.
    """
    parser = ArgumentParser(description=__doc__)