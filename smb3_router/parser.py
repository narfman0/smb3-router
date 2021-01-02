from openpyxl import load_workbook

from smb3_router.level import Level, Node, Graph


def parse(path="data/times.xlsx"):
    wb = load_workbook(path)
    levels = parse_levels(wb)
    nodes = []
    return Graph(nodes=nodes)


def parse_levels(workbook):
    levels = {}
    for world_number in range(1, 8):
        sheet = workbook[f"World{world_number}"]
        for row in sheet.rows:
            level_name = row[0].value
            if level_name == "level":
                continue
            if level_name is None:
                break
            try:
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
            except Exception as e:
                print(f"Exception reading level {level_name}: {e}")
    return levels


def frames_from_mssff(mssff):
    if len(mssff) <= 2:
        return int(mssff)
    frames = int(mssff[-2:])
    mss = mssff[:-2]
    frames += int(mss[-2:]) * 60
    frames += (int(mss) // 60) * 3600
    return frames
