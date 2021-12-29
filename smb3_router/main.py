import argparse
import logging

from smb3_router.parser import parse
from smb3_router.timing import frames_to_duration_string
from smb3_router.traversal import compute_path


DEFAULT_GRAPH_NAME = "Warpless"


def main():
    initialize_logging()
    parser = argparse.ArgumentParser(description="Compute expected times for routes.")
    parser.add_argument(
        "--graph_name",
        default=DEFAULT_GRAPH_NAME,
        help="category or route to compute (default: Warpless)",
    )
    args = parser.parse_args()
    compute(args.graph_name)


def compute(graph_name=DEFAULT_GRAPH_NAME):
    graph = parse(graph_name=graph_name)
    cost, path = compute_path(graph)
    path = ", ".join([node.level.name for node in path])
    duration = frames_to_duration_string(cost)
    logging.info(
        f"{graph_name} computed path {path} will cost {cost} frames ({duration})"
    )


def initialize_logging():
    # set up logging to file
    logging.basicConfig(
        filename="router.log",
        level=logging.INFO,
        format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger("").addHandler(console)


if __name__ == "__main__":
    main()