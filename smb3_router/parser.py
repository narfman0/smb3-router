from openpyxl import load_workbook

from smb3_router.models import Item, Graph, Level, GraphNode


def parse(path="data/times.xlsx", graph_name="Warpless"):
    workbook = load_workbook(path)
    levels = parse_workbook(workbook)
    return parse_graph(workbook[graph_name], levels)


def parse_graph(sheet, levels):
    """ Parse a graph, which represents a route for a specific category """
    nodes = [
        GraphNode(level=level_permutation, previous_nodes=[], next_nodes=[])
        for _name, level_permutations in levels.items()
        for level_permutation in level_permutations
    ]
    for row in sheet.rows:
        level_name = row[0].value
        if level_name == "level":
            continue
        if level_name is None:
            break
        level_permutations = [node for node in nodes if node.level.name == level_name]
        for level_permutation in level_permutations:
            level_permutation.required = bool(row[2].value)
        for previous_node_name in row[1].value.split(","):
            for candidate_previous_node in nodes:
                if candidate_previous_node.level.name == previous_node_name:
                    for level_permutation in level_permutations:
                        if (
                            level_permutation.level.enter
                            != candidate_previous_node.level.exit
                        ):
                            continue
                        level_permutation.previous_nodes.append(candidate_previous_node)
                        candidate_previous_node.next_nodes.append(level_permutation)
    return Graph(nodes=nodes)


def parse_workbook(workbook):
    levels = {}
    for world_number in range(1, 9):
        sheet = workbook[f"World{world_number}"]
        try:
            parse_sheet(sheet, levels)
        except Exception as e:
            raise Exception(f"Failed to parse sheet: {sheet.title} with error: {e}")
    return levels


def parse_sheet(sheet, levels):
    for row in sheet.rows:
        level_name = row[0].value
        try:
            if level_name == "level":
                continue
            if level_name is None:
                break
            mssff = str(int(row[5].value))
            granted_item = row[7].value
            if granted_item:
                granted_item = Item.value_of(granted_item)
            level = Level(
                name=level_name,
                difficulty=int(row[1].value),
                enter=row[2].value,
                star=bool(row[3].value),
                exit=row[4].value,
                frames=frames_from_mssff(mssff),
                notes=row[6].value,
                granted_item=granted_item,
            )
            levels[level.name] = levels.get(level.name, []) + [level]
        except Exception as e:
            raise Exception(f"Failed to parse level: {row[0].value} with error: {e}")


def frames_from_mssff(mssff):
    if len(mssff) <= 2:
        return int(mssff)
    frames = int(mssff[-2:])
    mss = mssff[:-2]
    frames += int(mss[-2:]) * 60
    frames += (int(mss) // 60) * 3600
    return frames
