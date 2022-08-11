from utils.midpoint import midpoint_rooting_outgroup, find_outlier_leaves
from ete3 import PhyloTree

def test_zero_length_tree_1():
    gene_tree = PhyloTree('test_data/zero_tree_1.tree')
    outliers = find_outlier_leaves(gene_tree)
    outgroup = midpoint_rooting_outgroup(gene_tree)
    assert outgroup == gene_tree.get_midpoint_outgroup()
    outgroup = midpoint_rooting_outgroup(gene_tree, outliers)


def test_zero_length_tree_2():
    gene_tree = PhyloTree('test_data/zero_tree_2.tree')
    outliers = find_outlier_leaves(gene_tree)
    outgroup = midpoint_rooting_outgroup(gene_tree)
    assert outgroup == gene_tree.get_midpoint_outgroup()
    outgroup = midpoint_rooting_outgroup(gene_tree, outliers)


def test_longest_path():
    assert 1 == 1


def test_outgroup():
    assert 1 == 1


def test_outlier():
    assert 1 == 1
