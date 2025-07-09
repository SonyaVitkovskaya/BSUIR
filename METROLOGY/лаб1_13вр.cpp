//Вводится целочисленный массив длины N. Найти и вывести среднее арифметическое квадратов его элементов.

#include <iostream>
#include <vector>
using namespace std;

int main()
{
	vector<int> massiv;
	int n;
	cin >> n; //ввод длины массива
	int s = 0;
	for (int i = 0; i < n; i++) 
	{	
		int k;
		cin >> k;//ввод i-того элемента массива
		s += k*k;
		massiv.push_back(k);//заполение массива
	}
	float r = round(s*10 /n)/10;//вычисление среднего арифметического квадратов элементов массива
	cout << r;
}
