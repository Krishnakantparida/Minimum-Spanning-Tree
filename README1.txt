#Note
-> Please read about graphs and minimum spanning tree (MST) for the internet.
-> Here I'm only explaining about one of the two alogorithms used for making a MST.
-> You are advised to take any one of the algorithms for making video.

Kruskal's algorithm for making MST
----------------------------------
-> Makes an MST edge by edge, for an undirected weighted graph.
-> Edges are considered for inclusion in MST in increasing order of their weights.
-> An edge is considered in MST if it does not form a cycle with edges already in MST.
-> Kruskal's algorithm follows forest concept of making a MST.

In my codes, I have made an MST of this graph

                1__(4)__0__(1)__2
                 \     / \     /
                 (2) (3) (6) (9)
                   \ /     \ /
                    3__(7)__4
                     \     /
                     (8) (5)
                       \ /
                        5

STEP-1> An adjacency list was created from the graph by listing the edges present in the graph
        And the edges are sorted according to the weight of each edge.

          [Node1,Node2,weight]    [Node1,Node2,weight]
                [0,1,4]                 [0,2,1]         1       0       2
                [0,2,1]                 [1,3,2]
                [0,3,3]                 [0,3,3]
                [0,4,6]                 [0,1,4]
                [1,3,2]         =>      [4,5,5]             3       4
                [2,4,9]                 [0,4,6]
                [3,4,7]                 [3,4,7]
                [3,5,8]                 [3,5,8]
                [4,5,5]                 [2,4,9]                 5

STEP-2> Select an edge with minimum weight, or the first edge of the sorted adjacency list.

        Edge Selected           1       0__(1)__2
        [0,2,1]


                                    3       4



                                        5

STEP-3> Select another edge which is second minimum in weight or equal to the weight of the previous one
        Such that no cycle is created (second edge of the sorted adjacency list).

        Edge Selected           1       0__(1)__2
        [0,2,1]                  \
        [1,3,2]                  (2)
                                   \
                                    3       4



                                        5

STEP-4> Similarly, other edges are selected, such that the edges joining them has minimum weight
        And no cycle is created (discard those edges, which are forming cycles).

        Edge selected           1       0__(1)__2               1__(4)__0__(1)__2
        [0,2,1]                  \     /                         \     /
        [1,3,2]                  (2) (3)                         (2) (3)
        [0,3,3]                    \ /                             \ /
        [4,5,5] not [0,1,4]         3       4           NOT         3       4
                (Since it is               /
                forming a                (5)
                cycle)                   /
                                        5                               5

STEP-5> Finally, select the edge such that all the nodes are connected to each other with edges with minimum weight
        Rest all the edges are discarded and minimum weight of the MST created is found.

        Edge Selected           1       0__(1)__2       <- Required MST with total weight = 1+2+3+5+6
        [0,2,1]                  \     / \                                                = 17
        [1,3,2]                  (2) (3) (6)
        [0,3,3]                    \ /     \
        [4,5,5]                     3       4
        [0,4,6]                            /
                                         (5)
                                         /
                                        5

#NOTE
-> There are chances that more than one type of MST is possible for a given graph.
-> For that case, it depends in which order your edges are placed in the adjacency list.
-> If you change the order of edges with same weight, you can get different MSTs.
