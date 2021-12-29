from smb3_router.models import Item, PathNode

USE_ITEM_COST = 40  # this shouldnt be static, but using for simplicity


def compute_path(graph, start_level_name="1-1", end_level_name="BC"):
    """ Create a path completing all required levels """
    # TODO add HBs and music boxes
    # TODO add edge costs like overworld movement, pipe transitions
    # TODO add constraints e.g. no powerups
    cost_paths = []
    start_node = graph.find_start_node()
    end_node = graph.find_end_node()
    create_path_permutations(start_node, end_node, [], 0, [], cost_paths, "small", None)
    return sorted(cost_paths, key=lambda cost_path: cost_path[0])[0]


def create_path_permutations(
    node, end_node, path, cost, items, cost_paths, enter, item_used
):
    if node.level.enter != enter:
        pass  # TODO observe enter powerup state
    path.append(PathNode(level=node.level, enter=enter, item_used=item_used))
    cost += node.level.frames
    if node == end_node:
        # TODO make sure all required nodes are complete
        cost_paths.append((cost, path.copy()))
    if node.level.granted_item:
        items.append(node.level.granted_item)
    for next_node in node.next_nodes:
        # TODO use items
        create_path_permutations(
            next_node, end_node, path, cost, items, cost_paths, node.level.exit, None
        )
    del path[-1]
    if node.level.granted_item:
        del items[-1]
    cost -= node.level.frames
    if not node.required:
        for i, item in enumerate(items):
            if item == Item.CLOUD:
                del items[i]
                for next_node in node.next_nodes:
                    create_path_permutations(
                        next_node,
                        end_node,
                        path,
                        cost + USE_ITEM_COST,
                        items,
                        cost_paths,
                        node.level.exit,
                        Item.CLOUD,
                    )
                items.insert(i, Item.CLOUD)
