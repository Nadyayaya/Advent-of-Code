#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main() {
	vector<string> v;
	ifstream file("C:\Users\NXP302\OneDrive - Powerco Limited\Documents\day 1.txt");
	if(file.is_open()) {
		string line;
		while(getline(file, line)) {
			v.push_back(line);
		}
	}
	file.close();
	int numincreased = 1;
	for(int i = 1; i < v.size(); i++) {
		// check item before
		if(v[i] > v[i - 1]) {
			numincreased++;
		}
	}
	std::cout << numincreased << std::endl;
	return 0;
}
