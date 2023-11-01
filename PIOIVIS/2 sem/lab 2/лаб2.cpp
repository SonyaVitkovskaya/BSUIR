#include <iostream>
#include <vector>
#include <string>
#include <fstream>

#include <algorithm>
#include <sstream>
#pragma warning(disable : 4996)
using namespace std;

void delete_zeros(vector<vector<char>>& a)
{
    for (int i = 0; i < a.size() - 1; ++i) 
    {
        int sum = 0;
        for (int j = 0; j < a[i].size() - 2; ++j) 
        {
            sum += a[i][j];
        }
        if (!sum)
            a.erase(a.begin() + i--);
    }
}

void delete_used(int x, int y, vector<vector<char>>& matr)
{
    matr.erase(matr.begin() + x);
    for (int i = 0; i < matr.size() - 1; ++i) {
        if (matr[i][y])
            --matr[i][matr[i].size() - 2];
        if (!matr[i][matr[i].size() - 2])
            matr.erase(matr.begin() + i);
        else
            matr[i].erase(matr[i].begin() + y);
    }
    matr[matr.size() - 1].erase(matr[matr.size() - 1].begin() + y);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int numb_of_cubes;
    cin >> numb_of_cubes;
    string name;
    cin >> name;
    vector<vector<char>> matrix_of_coincidences;
    vector<string> cubes;
    vector<char> temp_vect;
    vector<int> result(name.size());
    string cube;
    for (int i = 0; i < numb_of_cubes; ++i)
    {
        cin >> cube;
        cubes.push_back(cube);
    }
    for (int i = 0; i < numb_of_cubes; ++i) {
        temp_vect.clear();
        int coincidences = 0;
        for (int j = 0; j < name.size(); ++j)
        {
            if (find(cubes[i].begin(), cubes[i].end(), name[j]) != cubes[i].end())
            {
                temp_vect.push_back(1);
                ++coincidences;
            }
            else
                temp_vect.push_back(0);
        }
        temp_vect.push_back(coincidences);
        temp_vect.push_back(i);
        matrix_of_coincidences.push_back(temp_vect);
    }
    temp_vect.clear();
    for (int j = 0; j < name.size(); ++j)
        temp_vect.push_back(j);
    matrix_of_coincidences.push_back(temp_vect);
    delete_zeros(matrix_of_coincidences);

     bool condition_of_necessity = true;
    while (matrix_of_coincidences.size() - 1 && matrix_of_coincidences.size() - 1 >= matrix_of_coincidences[0].size() - 2 && condition_of_necessity)
    {
        int x = 0, y = 0;
        for (int i = 1; i < matrix_of_coincidences.size() - 1; ++i)
        {
            if (matrix_of_coincidences[x][matrix_of_coincidences[x].size() - 2] > matrix_of_coincidences[i][matrix_of_coincidences[i].size() - 2])
            {
                x = i;
            }
        }
        for (int j = 0; j < matrix_of_coincidences[x].size(); ++j) {
            if (matrix_of_coincidences[x][j])
            {
                y = j;
                break;
            }
        }
        result[matrix_of_coincidences[matrix_of_coincidences.size() - 1][y]] = matrix_of_coincidences[x][matrix_of_coincidences[x].size() - 1] + 1;
        delete_used(x, y, matrix_of_coincidences);

        bool need = false;
        for (int i = 0; i < result.size(); ++i)
            if (!result[i])
                need = true;
        condition_of_necessity = need;
    }
    bool full_result = true;
    for (int i = 0; i < result.size(); ++i)
        if (!result[i]) 
        {
            full_result = false;
            break;
        }
    if (full_result)
    {
        cout << "Yes" << endl;
        for (int i = 0; i <result.size(); i++)
            cout << result[i] << " ";
    }
    else
        cout << "No";
    return 0;
}
