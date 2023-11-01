 #include "lib.h"

#include <vector>
#include <iostream>
#pragma warning(disable : 4996)

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int Number;
    cin >> Number;

    if (Number == 1)
    {
        QuardTree Tree;
        QMatrix Matrix;
        cin >> Matrix.n_size;
       

        for (int i = 0; i < Matrix.n_size; i++)
            for (int j = 0; j < Matrix.n_size; j++)
                cin >> Matrix.matr[i][j];

        Tree = matrix_to_tree(Matrix);

        cout << Tree.k_vert << endl;
        for (int i = 0; i < Tree.k_vert; i++)
            for (int j = 0; j < Tree.number[i].size(); j++)
                cout << i << " " << Tree.number[i][j] << " " << Tree.value[i][j] << endl;
    }
    else
    {   
        QuardTree Tree;
        QMatrix Matrix;

        cin >> Tree.n_size >> Tree.k_vert;
        
        for (int i = 0; i < Tree.k_vert;i++)
        {   vector<int> pod_number;
            vector<int> pod_value;
            Tree.number.push_back(pod_number);
            Tree.value.push_back(pod_value);
            int x, y, z;
            cin >> x >> y >> z;
            Tree.number[x].push_back(y);
            Tree.value[x].push_back(z);
        }

        Matrix = tree_to_matrix(Tree);

        for (int i = 0; i < Matrix.n_size; i++)
        {
            for (int j = 0; j < Matrix.n_size; j++)
                cout << Matrix.matr[i][j] << " ";
            cout << endl;
        }

    }

    return 0;
}