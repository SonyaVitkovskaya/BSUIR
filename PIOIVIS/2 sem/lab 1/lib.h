#pragma once
#include <vector>
using namespace std;

struct QuardTree
{
    vector < vector<int>> number;
    vector <vector < int >> value;
    int n_size, k_vert;
};

struct QMatrix
{
    int n_size;
    int matr[100][100];
};

QuardTree matrix_to_tree(QMatrix Matrix);
QMatrix tree_to_matrix(QuardTree Tree);

void to_tree(int x, int y, int n_size, int pred, QuardTree& Tree, QMatrix& Matrix);
void to_matrix(int x, int y, int n_size, int v, QuardTree& Tree, QMatrix& Matrix);
 