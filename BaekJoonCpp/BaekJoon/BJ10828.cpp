/*
#include<iostream>
#include<string.h>
using namespace std;

class Stack {

private:
	int len = 0;
	int ar[10000] = { -1 };

public:
	void push(int x) {
		ar[len] = x;
		len++;
	}

	void pop() {
		if (len == 0) {
			cout << -1 << endl;
		}
		else {
			len--;
			cout << ar[len] << endl;
		}
	}

	void size() {
		cout << len << endl;
	}

	void empty() {
		cout << (len == 0) << endl;
	}

	void top() {
		if (len == 0) {
			cout << -1 << endl;
		}
		else {
			cout << ar[len - 1] << endl;
		}
	}

};

int main() {

	int n;
	cin >> n;
	Stack stk;
	char input[10];
	int j;

	for (int i = 0; i < n; i++) {
		cin >> input;
		if (strcmp(input, "push") == 0) {
			cin >> j;
			stk.push(j);
		}
		else if (strcmp(input, "pop") == 0) {
			stk.pop();
		}
		else if (strcmp(input, "size") == 0) {
			stk.size();
		}
		else if (strcmp(input, "empty") == 0) {
			stk.empty();
		}
		else if (strcmp(input, "top") == 0) {
			stk.top();
		}
	}


	return 0;
}
*/