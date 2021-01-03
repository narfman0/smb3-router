import argparse

from smb3_router.parser import parse
from smb3_router.traversal import compute_path


DEFAULT_GRAPH_NAME = "Warpless"


def main():
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
    seconds = cost // 60.09
    time = f"{int(seconds // 60)}:{int(seconds % 60)}"
    print(f"{graph_name} computed path {path} will cost {cost} frames ({time})")


if __name__ == "__main__":
    main()