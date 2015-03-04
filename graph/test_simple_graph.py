import pytest
from simple_graph import Graph
from collections import OrderedDict

@pytest.fixture(scope="function")
def test_graph():
    test_graph = Graph()
    test_graph.add_node(5)
    test_graph.add_node(42)
    test_graph.add_node("test")
    test_graph.add_edge(5, 42)
    test_graph.add_edge(42, "test", 1000)
    test_graph.add_edge("test", 5)

    return test_graph


@pytest.fixture(scope="function")
def test_depth_traversal_graph():
    test_graph = Graph()
    for i in range(10):
        test_graph.add_node(i)
    test_graph.add_edge(0, 1)
    test_graph.add_edge(0, 2)
    test_graph.add_edge(0, 3)
    test_graph.add_edge(1, 4)
    test_graph.add_edge(1, 5)
    test_graph.add_edge(1, 8)
    test_graph.add_edge(5, 6)
    test_graph.add_edge(6, 7)
    test_graph.add_edge(2, 9)

    return test_graph


@pytest.fixture(scope="function")
def test_breadth_traversal_graph():
    test_graph = Graph()
    for i in range(1, 10):
        test_graph.add_node(i)
    test_graph.add_edge(1, 2)
    test_graph.add_edge(1, 3)
    test_graph.add_edge(1, 4)
    test_graph.add_edge(2, 5)
    test_graph.add_edge(2, 6)
    test_graph.add_edge(4, 7)
    test_graph.add_edge(4, 8)
    test_graph.add_edge(5, 9)

    return test_graph


def test_constructor():
    test = Graph()
    assert test.graph_dict == {}


def test_add_node():
    test = Graph()
    test.add_node(5)
    assert 5 in test.graph_dict


def test_add_node_if_already_present(test_graph):
    test_graph.add_node(5)
    assert 42 in test_graph.graph_dict[5]


def test_add_edge():
    test = Graph()
    test.add_node(5)
    test.add_node(42)
    test.add_edge(5, 42)

    assert 42 in test.graph_dict[5]


def test_add_edge_first_node_new():
    test = Graph()
    test.add_node(55)
    test.add_edge("test", 55)
    assert "test" in test.graph_dict
    assert 55 in test.graph_dict["test"]


def test_add_edge_second_node_new():
    test = Graph()
    test.add_node(55)
    test.add_edge(55, "test")
    assert "test" in test.graph_dict
    assert "test" in test.graph_dict[55]


def test_add_edge_with_default_weight():
    test = Graph()
    test.add_edge(1, 2)
    assert test.graph_dict[1] == OrderedDict([(2, 1)])


def test_add_edge_with_weight_parameter():
    test = Graph()
    test.add_edge(1, 2, 10000)
    assert test.graph_dict[1] == OrderedDict([(2, 10000)])


def test_nodes(test_graph):
    assert test_graph.nodes() == ["test", 42, 5]


def test_edges(test_graph):
    assert test_graph.edges() == [("test", 5, 1), (42, "test", 1000), (5, 42, 1)]


def test_del_node(test_graph):
    test_graph.add_edge("test", "purple")
    assert 42 in test_graph.nodes()
    test_graph.del_node(42)
    assert 42 not in test_graph.nodes()
    for edge_list in test_graph.graph_dict.values():
        assert 42 not in edge_list


def test_del_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.del_node("test2")
    assert "Node not found" in str(e.value)


def test_del_edge(test_graph):
    test_graph.del_edge(5, 42)
    assert 42 not in test_graph.graph_dict[5]


def test_del_edge_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.del_edge(5, "test")
    assert "Edge not found" in str(e.value)


def test_del_edge_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.del_edge(8, "test")
    assert "Edge not found" in str(e.value)


def test_has_node_true(test_graph):
    assert test_graph.has_node(5)


def test_has_node_false(test_graph):
    assert not test_graph.has_node(6)


def test_neighbors(test_graph):
    assert test_graph.neighbors(5) == [42]


def test_neighbors_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.neighbors(6)
    assert 'Node not found' in str(e.value)


def test_adjacent(test_graph):
    assert test_graph.adjacent(42, "test")


def test_adjacent_first_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.adjacent("test2", 42)
    assert 'First node not found' in str(e.value)


def test_adjacent_second_node_not_found(test_graph):
    with pytest.raises(KeyError) as e:
        test_graph.adjacent("test", 47)
    assert 'Second node not found' in str(e.value)


def test_depth_first_from_node_0(test_depth_traversal_graph):
    assert test_depth_traversal_graph.depth_first_traversal(0) == [
        0, 1, 4, 5, 6, 7, 8, 2, 9, 3]


def test_depth_first_from_node_1(test_depth_traversal_graph):
    assert test_depth_traversal_graph.depth_first_traversal(1) == [
        1, 4, 5, 6, 7, 8]


def test_depth_first_no_edges():
    test = Graph()
    test.add_node(55)
    test.add_node("test")
    test.add_node(2)
    assert test.depth_first_traversal(55) == [55]


def test_depth_multiple_edges():
    test = Graph()
    for i in range(5):
        test.add_node(i)
    test.add_edge(0, 1)
    test.add_edge(0, 2)
    test.add_edge(1, 2)
    test.add_edge(1, 3)
    test.add_edge(2, 3)
    test.add_edge(3, 4)

    assert test.depth_first_traversal(0) == [0, 1, 2, 3, 4]


def test_depth_cyclic(test_graph):
    assert test_graph.depth_first_traversal(5) == [5, 42, "test"]


def test_breadth_first(test_breadth_traversal_graph):
    assert test_breadth_traversal_graph.breadth_first_traversal(1) == range(1, 10)
