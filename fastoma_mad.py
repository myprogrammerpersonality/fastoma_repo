import os
from ete3 import PhyloTree


def mad_rooting(input_tree_file_path: str, mad_executable_path: str = "./mad") -> PhyloTree:
    """
    Rooting a tree using MAD algorithm.
    :param input_tree_file_path: path to the input tree file.
    :param mad_excutable_path: path to the MAD executable.
    :return: rooted tree as PhyloTree object.
    """
    # Create the command to run MAD.
    mad_command = f"{mad_excutable_path} -i {input_tree_file_path}"

    # Run MAD and ignore the output.
    os.system(mad_command)

    # Read the output file in input_tree_file_path + ".rooted" using ete3.
    rooted_tree = PhyloTree(input_tree_file_path + ".rooted")

    return rooted_tree

# Example usage:

# Path to the input tree file.
input_tree_file_path = "./test_data/zero_tree_1.tree"

# Path to the MAD executable.
mad_executable_path = "./mad"

# Root the tree using MAD.
rooted_tree = mad_rooting(input_tree_file_path, mad_executable_path)
