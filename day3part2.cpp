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

long checkSlopes(vector<string> &values){
    long result = 1;
	// Check all the slopes and multiply each by the total
	result *= countTrees(values, 1, 1);
	result *= countTrees(values, 3, 1);
	result *= countTrees(values, 5, 1);
	result *= countTrees(values, 7, 1);
	result *= countTrees(values, 1, 2);
	return result;
    
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
    //cout << countTrees(vector<string> &values, 3, 1) << endl;
    cout << checkSlopes(values) << endl;     
    
    return 0;
}
