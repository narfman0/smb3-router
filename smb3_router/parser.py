from openpyxl import load_workbook

from smb3_router.models import Graph, Level, Node


def parse(path="data/times.xlsx", graph_name="Warpless"):
    workbook = load_workbook(path)
    levels = parse_levels(workbook)
    return parse_graph(workbook[graph_name], levels)


def parse_graph(sheet, levels):
    """ Parse a graph, which represents a route for a specific category """
    nodes = {
        level_name: Node(level=level, previous_nodes=[], next_nodes=[])
        for level_name, level in levels.items()
    }
    for row in sheet.rows:
        level_name = row[0].value
        if level_name == "level":
            continue
        if level_name is None:
            break
        node = nodes[level_name]
        node.required = bool(row[2].value)
        for previous_node_name in row[1].value.split(","):
            previous_node = nodes[previous_node_name]
            node.previous_nodes.append(previous_node)
            previous_node.next_nodes.append(node)
    return Graph(nodes=nodes.values())


def parse_levels(workbook):
    levels = {}
    for world_number in range(1, 9):
        sheet = workbook[f"World{world_number}"]
        for row in sheet.rows:
            level_name = row[0].value
            if level_name == "level":
                continue
            if level_name is None:
                break
            mssff = str(int(row[4].value))
            level = Level(
                name=level_name,
                difficulty=int(row[1].value),
                enter=row[2].value,
                exit=row[3].value,
                frames=frames_from_mssff(mssff),
                notes=row[5].value,
                granted_item=row[6].value,
            )
            levels[level.name] = level
    return levels


def frames_from_mssff(mssff):
    if len(mssff) <= 2:
        return int(mssff)
    frames = int(mssff[-2:])
    mss = mssff[:-2]
    frames += int(mss[-2:]) * 60
    frames += (int(mss) // 60) * 3600
    return frames
