//More info: https://adventofcode.com/2020/day/3

#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int countTrees(vector<string> &values, int r, int d){
    int trees = 0;
	int y = 0;
	int x = 0;
	while (y < values.size()){
		if (values[y][x] == '#')
			trees++;
		y += d;
		x += r;
		if (x >= values[y].size()){
			x-=values[y].size();
		}
	}
    return trees;
}


int main(){
    vector<string> values;
    string cre;
    ifstream info ("inputDay3.txt");
    if(info.is_open()){
        while (info >> cre){
            values.push_back(cre);
        }
    }
    info.close();    
    cout << countTrees(values,3,1) << endl;     
    
    return 0;
}
