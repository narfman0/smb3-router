def compute_path(nodes):
    """ Create a path completing all required levels """
    # TODO add constraints
    # TODO add items like clouds
    # TODO add HBs and music boxes
    # TODO add edge costs like overworld movement, pipe transitions
    cost_paths = []
    for node in nodes:
        if node.required and node.level.name == "BC":
            create_path_permutations(nodes, [node], node.level.frames, cost_paths)
    return sorted(cost_paths, key=lambda cost_path: cost_path[0])[0]


def create_path_permutations(nodes, path, cost, cost_paths):
    current_level = path[-1]
    if not current_level.prerequisites:
        cost_paths.append((cost, list(reversed(path))))
        return
    for prerequisite in current_level.prerequisites:
        path.append(prerequisite)
        create_path_permutations(
            nodes, path, cost + prerequisite.level.frames, cost_paths
        )
        del path[-1]