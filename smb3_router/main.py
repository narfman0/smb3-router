import argparse

from smb3_router.parser import parse


def main():
    parser = argparse.ArgumentParser(description="Compute expected times for routes.")
    parser.add_argument(
        "--graph_name",
        default="Warpless",
        help="category or route to compute (default: Warpless)",
    )
    args = parser.parse_args()
    graph = parse(graph_name=args.graph_name)
    print(f"Graph with {len(graph.nodes)} nodes computed")


if __name__ == "__main__":
    main()