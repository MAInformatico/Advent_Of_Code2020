#include <vector>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main(){
    vector<int> values;
    int cre = 0;
    int flag = 0;
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
            if(values[i]+values[j] == 2020){ cout << values[i] * values[j] << endl;
                flag++;
                break;
            }
        }
    if(flag >0) break;
    }
    return 0;
}
