from smb3_router.models import Item

USE_ITEM_COST = 40  # this shouldnt be static, but using for simplicity


def compute_path(graph, start_level_name="1-1", end_level_name="BC"):
    """ Create a path completing all required levels """
    # TODO add constraints
    # TODO add items like clouds
    # TODO add HBs and music boxes
    # TODO add edge costs like overworld movement, pipe transitions
    cost_paths = []
    start_node = graph.find_start_node()
    end_node = graph.find_end_node()
    items = [start_node.level.granted_item] if start_node.level.granted_item else []
    create_path_permutations(
        end_node, [start_node], start_node.level.frames, items, cost_paths
    )
    return sorted(cost_paths, key=lambda cost_path: cost_path[0])[0]


def create_path_permutations(end_node, path, cost, items, cost_paths):
    current_node = path[-1]
    if current_node == end_node:
        # TODO make sure all required nodes are complete
        cost_paths.append((cost, list(path)))
        return
    for next_node in current_node.next_nodes:
        path.append(next_node)
        if next_node.level.granted_item:
            items.append(next_node.level.granted_item)
        create_path_permutations(
            end_node, path, cost + next_node.level.frames, items, cost_paths
        )
        del path[-1]
        if not next_node.required:
            for i, item in enumerate(items):
                if item == Item.CLOUD:
                    cloud_items = items.copy()
                    del cloud_items[i]
                    # TODO use clouds
                    # create_path_permutations(
                    #   end_node, path, cost + USE_ITEM_COST, cloud_items, cost_paths
                    # )
