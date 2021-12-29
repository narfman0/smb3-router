import logging

from smb3_router.models import Item, PathNode
from smb3_router.timing import frames_to_duration_string

USE_ITEM_COST = 40  # this shouldnt be static, but using for simplicity


def compute_path(graph, start_level_name="1-1", end_level_name="BC", max_difficulty=7):
    """ Create a path completing all required levels """
    # TODO add HBs and music boxes
    # TODO add edge costs like overworld movement, pipe transitions
    # TODO add constraints e.g. no powerups
    cost_paths = []
    start_node = graph.find_start_node()
    end_node = graph.find_end_node()
    create_path_permutations(
        start_node, end_node, [], 0, [], cost_paths, "small", None, max_difficulty
    )
    if not cost_paths:
        raise Exception("No valid paths given constraints!")
    return sorted(cost_paths, key=lambda cost_path: cost_path[0])[0]


def create_path_permutations(
    node, end_node, path, cost, items, cost_paths, enter, item_used, max_difficulty
):
    logging.debug(
        f"Creating permutation with level {node.level.name} with len(path) {len(path)} items {items} enter {enter} item_used {item_used}"
    )
    # TODO observe star usage
    if node.level.enter != enter or node.level.difficulty > max_difficulty:
        return
    # TODO item_used multiple items (e.g. star)
    path.append(PathNode(level=node.level, enter=enter, item_used=item_used))
    cost += node.level.frames
    if node == end_node:
        # TODO make sure all required nodes are complete
        duration = frames_to_duration_string(cost)
        path_str = ", ".join([node.level.name for node in path])
        logging.debug(f"Candidate path found {path_str} of duration ({duration})")
        cost_paths.append((cost, path.copy()))
    if node.level.granted_item:
        items.append(node.level.granted_item)
    for next_node in node.next_nodes:
        create_path_permutations(
            next_node,
            end_node,
            path,
            cost,
            items,
            cost_paths,
            node.level.exit,
            None,
            max_difficulty,
        )
        for i, item in enumerate(items):
            if item == Item.CLOUD:
                continue
            # TODO use other items e.g. star
            if item == Item.PWING:
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
                        item,
                        max_difficulty,
                    )
                items.insert(i, item)
                break
    del path[-1]
    if node.level.granted_item:
        del items[-1]
    cost -= node.level.frames
    for i, item in enumerate(items):
        if node.required and item == Item.CLOUD:
            continue
        # TODO use other items e.g. star
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
                    item,
                    max_difficulty,
                )
            items.insert(i, item)
            break
