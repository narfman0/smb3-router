import argparse

from smb3_router.parser import parse
from smb3_router.traversal import compute_path


def main():
    parser = argparse.ArgumentParser(description="Compute expected times for routes.")
    parser.add_argument(
        "--graph_name",
        default="Warpless",
        help="category or route to compute (default: Warpless)",
    )
    args = parser.parse_args()
    graph = parse(graph_name=args.graph_name)
    cost, path = compute_path(graph)
    path_str = ", ".join([node.level.name for node in path])
    seconds = cost // 60.09
    print(
        f"{args.graph_name} computed path {path_str} will take {cost} frames ({int(seconds // 60)}:{int(seconds % 60)})"
    )


if __name__ == "__main__":
    main()