def compute_path(graph, start_level_name="1-1", end_level_name="BC"):
    """ Create a path completing all required levels """
    # TODO add constraints
    # TODO add items like clouds
    # TODO add HBs and music boxes
    # TODO add edge costs like overworld movement, pipe transitions
    cost_paths = []
    start_node = graph.find_start_node()
    end_node = graph.find_end_node()
    create_path_permutations(
        end_node, [start_node], start_node.level.frames, cost_paths
    )
    return sorted(cost_paths, key=lambda cost_path: cost_path[0])[0]


def create_path_permutations(end_node, path, cost, cost_paths):
    current_node = path[-1]
    if current_node == end_node:
        cost_paths.append((cost, list(path)))
        return
    for next_node in current_node.next_nodes:
        path.append(next_node)
        create_path_permutations(
            end_node, path, cost + next_node.level.frames, cost_paths
        )
        del path[-1]