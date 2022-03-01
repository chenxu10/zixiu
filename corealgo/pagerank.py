import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def pagerank():
    """
    Returns the PageRank of Nodes in a Graph

    >>> pagerank()

    Args: 


    Returns:
        pagerank: A dictionary of nodes with PageRank as Value

    Examples: 
        >>> G = nx.DiGraph(nx.path_graph(4))
        >>> pr = pagerank(G)

    Notes:

    Raises:
        
    References:

    """

    return pagerank_scipy(G, alpha, personalization, max_iter, tol, nstart, weight, dangling)


def pagerank_scipy(G, alpha=0.05, personalization=None, max_iter=100, tol=1.0e6, weight="weight"):
    """

    
    """
    # edge cases
    # convert G graph into a numpy sparse matrix
    # init a vector
    # personalization
    # power iteration

    # if len(G) == 0:
    #     return {}

    # nodelist = list(G)
    # M = nx.to_scipy_sparse_matrix(G, nodelist=nodelist, weight=weight, dtype=float)
    # S = np.array(M.sum(axis=1)).flatten()
    # return S




    # choose start vector


    # power_iteration


if __name__ == "__main__":
    DG = nx.DiGraph()
    DG.add_weighted_edges_from([
        ("A","B",1/3),
        ("A","C",1/3),
        ("A","D",1/3),
        ("B","D",0.5),
        ("B","A",0.5),
        ("C","A",1),
        ("D","C",0.5),
        ("D","B",0.5)])
    nx.draw(DG, with_labels=True)
    # plt.title(r'$G({},{})$'.format(n,p))
    plt.show()

    S = pagerank_scipy(DG)
    print(S)
