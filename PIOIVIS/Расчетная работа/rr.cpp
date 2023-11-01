#include <iostream>
#include <fstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

void closure(const string& file_name);

int main()
{
    cout << "1)" << endl;
    closure("input_graph1.txt");
    cout << "2)" << endl;
    closure("input_graph2.txt");
    cout << "3)" << endl;
    closure("input_graph3.txt");
    cout << "4)" << endl;
    closure("input_graph4.txt");
}
void closure(const string& file_name)
{   vector<vector<int>> list;
    ifstream file;
    file.open(file_name);
    if (!file.is_open())
    {
        cout << "the attempt to open the file failed" << endl;
    }
    else
    {
        string str, ch;
        while (!file.eof())
        {
            getline(file, str);
            stringstream sstr(str);
            vector<int> vector_str;

            while (getline(sstr, ch, ' '))
            {
                vector_str.push_back(stoi(ch));
            }
            list.push_back(vector_str);
        }
    }
    file.close();
   
    vector<int> vertices;
    for (int v = 0; v < list.size(); v++)
    {
        vertices.push_back(list[v][0]);
    }
    for (vector<int> i : list) 
    {
        for (vector<int> j : list)
        {
            vector<int> vec1;
            copy(i.begin(), i.end(), back_inserter(vec1));
            vector<int> vec2;
            copy(j.begin(), j.end(), back_inserter(vec2));
            sort(vec1.begin(), vec1.end());
            sort(vec2.begin(), vec2.end());
            if (i != j && vec1==vec2)
            {
                if (find(vertices.begin(), vertices.end(), i[0])!=vertices.end() && find(vertices.begin(), vertices.end(), j[0]) != vertices.end())
                {
                    vector<int> del;
                    del.push_back(i[0]);
                    del.push_back(j[0]);
                    string k = to_string(i[0]) + to_string(j[0]);
                    int f = stoi(k);
                    vector<int> new_v = { f };
                    copy(i.begin(), i.end(), back_inserter(new_v));
                    for(int t=0; t<j.size(); t++ )
                    {
                        if (find(new_v.begin(), new_v.end(), j[t]) == new_v.end())
                        {
                            new_v.push_back(j[t]);
                        }
                    }
                    list.push_back(new_v);

                    vector<int> p,o;
                    copy(j.begin(), j.end(), back_inserter(p));
                    for (int k = 0; k < list.size(); k++)
                    {
                        if (list[k] == i)
                        {
                            list.erase(list.begin() + k);
                            break;
                        }
                    }
                    for (int k = 0; k < list.size(); k++)
                    {
                        if (list[k] == p)
                        {
                            list.erase(list.begin() + k);
                            break;
                        }
                    }
                    for (int x = 0; x < list.size(); x++)
                    {
                        for (int j = 0; j < list[x].size(); j++)
                        {
                            if (find(del.begin(), del.end(), list[x][j]) != del.end())
                            {
                                list[x].erase(list[x].begin() + j);

                                if (find(list[x].begin(), list[x].end(), new_v[0]) == list[x].end())
                                {
                                    list[x].push_back(new_v[0]);
                                }
                                j--;
                            }
                        }
                    }
                    
                }
            }
        }
    }
    
    for (int i = 0; i < list.size(); i++)
    {
       for (int j = 0; j < list[i].size(); j++)
       {
            cout << list[i][j] << " ";
       }
       cout << endl;
    }
   
}
