"""
2097: Valid Arrangement of Pairs

https://leetcode.com/problems/valid-arrangement-of-pairs/description/

You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement of pairs.

Example 1:

Input: pairs = [[5,1],[4,5],[11,9],[9,4]]
Output: [[11,9],[9,4],[4,5],[5,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 9 == 9 = start1 
end1 = 4 == 4 = start2
end2 = 5 == 5 = start3
Example 2:

Input: pairs = [[1,3],[3,2],[2,1]]
Output: [[1,3],[3,2],[2,1]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 3 == 3 = start1
end1 = 2 == 2 = start2
The arrangements [[2,1],[1,3],[3,2]] and [[3,2],[2,1],[1,3]] are also valid.
Example 3:

Input: pairs = [[1,2],[1,3],[2,1]]
Output: [[1,2],[2,1],[1,3]]
Explanation:
This is a valid arrangement since endi-1 always equals starti.
end0 = 2 == 2 = start1
end1 = 1 == 1 = start2
 

Constraints:

1 <= pairs.length <= 105
pairs[i].length == 2
0 <= starti, endi <= 109
starti != endi
No two pairs are exactly the same.
There exists a valid arrangement of pairs.
"""

from collections import defaultdict


def valid_arrangement(pairs: list[list[int]]) -> list[list[int]]:
    """Return any valid arrangement of pairs."""
    graph: dict[int, list[int]] = defaultdict(list)
    incoming_edges_map: dict[int, int] = defaultdict(int)

    for i, pair in enumerate(pairs):
        node, edge = pair
        graph[node].append(edge)
        incoming_edges_map[edge] += 1

    start_node: int | None = None
    for node, edges in graph.items():
        if len(edges) > incoming_edges_map[node]:
            start_node = node
            break

    if start_node is None:
        start_node = next(iter(graph))

    node_stack: list[int] = [start_node]
    edge_list: list[list[int]] = []
    last_popped_node: int | None = None
    while node_stack:
        current_node = node_stack[-1]
        if not graph[current_node]:
            edge_list.append([current_node, last_popped_node])  # type: ignore[list-item]
            last_popped_node = node_stack.pop(-1)
            continue
        node_stack.append(graph[current_node].pop(0))

    return list(reversed(edge_list[1:]))


def test() -> None:
    """Test valid arrangement."""
    pairs = [
        [5, 13],
        [10, 6],
        [11, 3],
        [15, 19],
        [16, 19],
        [1, 10],
        [19, 11],
        [4, 16],
        [19, 9],
        [5, 11],
        [5, 6],
        [13, 5],
        [13, 9],
        [9, 15],
        [11, 16],
        [6, 9],
        [9, 13],
        [3, 1],
        [16, 5],
        [6, 5],
    ]
    print(valid_arrangement(pairs))
    assert False
