from collections import defaultdict
from typing import List, Tuple
import random
from itertools import combinations

import numpy as np
from ete3 import PhyloTree


def get_farthest_leaf(tree: PhyloTree, target_leaf: PhyloTree, leaves_list: List[PhyloTree]) -> Tuple[float, PhyloTree]:
    """
    Given a target leaf it returns the farthest leave to it from a given list of leaves
    """
    max_dist = 0
    max_leaf: PhyloTree
    for leaf in leaves_list:
        dist = tree.get_distance(target_leaf, leaf)
        if dist > max_dist:
            max_dist = dist
            max_leaf = leaf
    
    return max_dist, max_leaf


def midpoint_rooting_longest_path(tree: PhyloTree, leaves_to_exclude=None) -> Tuple[float, PhyloTree, PhyloTree]:
    """
    given a gene tree and optionally a list of leaves to exclude it find the two
    furthest leave in the tree to be used for midpoint rooting
    """
    leaves_list = tree.get_leaves()
    
    if leaves_to_exclude:
        leaves_set = set(leaves_list)
        leaves_set -= set(leaves_to_exclude)
        leaves_list = list(leaves_set)
        
    random_leaf = random.choice(leaves_list)
    _, first_leaf = get_farthest_leaf(tree=tree, target_leaf=random_leaf, leaves_list=leaves_list)
    _, second_leaf = get_farthest_leaf(tree=tree, target_leaf=first_leaf, leaves_list=leaves_list)
    longest_dist = tree.get_distance(first_leaf, second_leaf)
    
    return longest_dist, first_leaf, second_leaf


def midpoint_rooting_outgroup(tree: PhyloTree, leaves_to_exclude=None) -> PhyloTree:
    """
    Using midpoint rooting algorithm find the outgroup to be used to root the tree.
    you can provide a list of leaves to be ignored for example because of long branch
    """
    distance, first_leaf, second_leaf = midpoint_rooting_longest_path(tree, leaves_to_exclude)
    distance_first = tree.get_distance(first_leaf)
    distance_second = tree.get_distance(second_leaf)
    
    farther_node = first_leaf if distance_first > distance_second else second_leaf
    
    current_distance = 0
    current_node = farther_node
    while current_distance + current_node.dist < distance/2:
        current_distance += current_node.dist
        current_node = current_node.up
        
    return current_node


def find_outlier_leaves(tree: PhyloTree):
    distances = defaultdict(list)

    leaves_name = tree.get_leaves()
    for i, j in combinations(leaves_name, 2):
        distances[i].append(tree.get_distance(i, j))
        distances[j].append(tree.get_distance(j, i))
    
    distances_agg = []
    for leaf in distances.keys():
        distances_agg.append(sum(distances[leaf]))
    q3, q1 = np.percentile(distances_agg, [75 ,25])
    iqr = q3 - q1
    threshold = q3 + (1.5 * iqr)

    outliers = []
    for leaf in distances.keys():
        if sum(distances[leaf]) > threshold:
            outliers.append(leaf)
    
    return outliers