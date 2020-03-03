#Note
-> Please read about graphs and minimum spanning tree (MST) for the internet.
-> Here I'm only explaining about one of the two alogorithms used for making a MST.
-> You are advised to take any one of the algorithms for making video.

Prim's algorithm for making MST
-------------------------------
-> Makes an MST starting from any one vertex, for an undirected weighted graph.
-> Uses an adjacency matrix from which it maintains two set of vertices.
-> from one set, one vertex is selected, which is part of the graph, and included in MST set.
-> all the edges of this vertex are taken, and one edge with minimum weight is selected.
-> Another vertex of that edge is selected, same is done as above and placed in MST set.
-> It is ensured that no vertex is chosen which is already in the MST set, or if it's forming a cycle.

In my codes, I have made an MST of this graph

                1__(5)__3                  0 1 2 3 4 5 6
               / \     / \                 _____________
             (1) (4) (9) (8)            0 |0 4 6 9 2 - -
             /     \ /     \            1 |4 0 - 5 - 1 -
            5       0       6           2 |6 - 0 - 7 3 -
             \     / \     /            3 |9 5 - 0 - - 8        <- Adjacency matrix
             (3) (6) (2) (1)            4 |2 - 7 - 0 - 1
               \ /     \ /              5 |- 1 3 - - 0 -
                2__(7)__4               6 |- - - 8 1 - 0

STEP-1> Select any vertex (say "0"), and take all the edges adjacent to it in dotted lines
        Select the edge with solid lines which has minimum weight (say 0-4)

                1       3
                 .     .
                  .   .
                   . .
            5      [0]      6
                   . \
                  .  (2)
                 .     \
                2       4

STEP-2> Select another vertex (say "4"), and take all other edges adjacent to this vertex and previous one
        Select another edge with solid lines, adjacent to both vertices ("0" and "4")and has minimum weight.

                1       2
                 .     .
                  .   .
                   . .
            5      [0]      6
                   . \     /
                  .  (2) (1)
                 .     \ /
                2 . . .[4]

STEP-3> With more edges are selected with above conditions, more vertices are included in MST
        Ensure that vertices already in MST are not chosen again, or those edges, which are forming a cycle.

                1       3                      [1]. . . 3                      [1]. . . 3
                 \     . .                     / \     . .                     / \     . .
                 (4)  .   .                  (1) (4)  .   .                  (1) (4)  .   .
                   \ .     .                 /     \ .     .                 /     \ .     .
            5      [0]     [6]      =>      5      [0]     [6]      =>     [5]     [0]     [6]
                   . \     /                       . \     /                 \     . \     /
                  .  (2) (1)                      .  (2) (1)                 (3)  .  (2) (1)
                 .     \ /                       .     \ /                     \ .     \ /
                2 . . .[4]                      2 . . .[4]                      2 . . .[4]

STEP-4> Finally, all the vertices are included in the MST, with edges having minimum cost
        And the total weight of the MST is calculated.


               [1]_(5)__3                       1__(5)__3       -> Required MST with total weight = 1+1+2+3+4+5
               / \     . .                     / \                                                = 16
             (1) (4)  .   .                  (1) (4)
             /     \ .     .                 /     \
           [5]     [0]     [6]      =>      5       0       6
             \     . \     /                 \       \     /
             (3)  .  (2) (1)                 (3)     (2) (1)
               \ .     \ /                     \       \ /
                2 . . .[4]                      2       4

#NOTE
-> Here also, more than one MST is possible for a given graph.
-> If different vertices are chosen once at a time, then different MSTs can be obtained.
-> Also, different MSTs can be obtained if the order of the vertices are changed in adjacency matrix.
