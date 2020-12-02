//Info available on: https://adventofcode.com/2020/day/1

#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

bool exists(vector<int> v, int value) {
    return find(v.begin(), v.end(), value) != v.end();
}


int main(){
    vector<int> values;
    int cre = 0;
    int flag = 0;
    int v3 = 0;
    ifstream info ("inputDay1.txt");
    if(info.is_open()){
        while (info >> cre){
            values.push_back(cre);
        }
    }
    info.close();        
    
    sort(values.begin(), values.end());
    for(int i = 0; values.size(); i++){
        for(int j = i+1; j<values.size();j++){
            v3 = 2020 - (values[i] + values[j]);
            if(exists(values,v3) ){
                cout << values[i] * values[j] * v3 << endl;
                flag++;
                break;
            }
        }
    if(flag >0) break;
    }
    return 0;
}
