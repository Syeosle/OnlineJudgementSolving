#include<iostream>
#include<cmath>
#include<string.h>
using namespace std;

int str2biNum(char* msgPiece) {
	return 10000 * (msgPiece[0] - '0') + 1000 * (msgPiece[1] - '0') + 100 * (msgPiece[2] - '0') + 10 * (msgPiece[3] - '0') + (msgPiece[4] - '0');
}

void biNum2Char(int x, char* chr, int ind) {
	int res = 0;
	for (int i = 0; x != 0; i++) {
		res += pow(2, i) * (x % 10);
		x /= 10;
	}

	if (res == 0) {
		chr[ind] = ' ';
	}
	else {
		chr[ind] = 'A' + res - 1;
	}
}

void decode(char* msg, int r, int c, char* res) {
	int ind = 0, resInd = 0;
	
	for (int d = 0; d < r || d < c; d += 2) {

		for (int i = 0; i < c - 1 - d; i++) {
			res[resInd++] = msg[ind++];
		}

		for (int i = 0; i < r - 1 - d; i++) {
			res[resInd++] = msg[ind];
			ind += c;
		}

		for (int i = 0; i < c - 1 - d; i++) {
			res[resInd++] = msg[ind--];
		}

		for (int i = 0; i < r - 1 - d; i++) {
			res[resInd++] = msg[ind];
			ind -= c;
		}
		ind += c + 1;
	}

	if (r * c % 2 == 1) {
		res[resInd++] = msg[r * c / 2];
	}

	for (int i = resInd / 5 * 5; i < resInd; i++) {
		res[i] = '\0';
	}

}

int main() {

	int t;
	cin >> t;

	char msg[450] = "", res[450] = "";
	int r, c, delCnt = 0, len;


	for (int i = 0; i < t; i++) {

		cin >> r >> c >> msg;

		len = r * c / 5;

		decode(msg, r, c, res);

		for (int i = 0; i < len * 5; i += 5) {
			char msgPiece[5] = { res[i], res[i + 1], res[i + 2], res[i + 3], res[i + 4] };
			biNum2Char(str2biNum(msgPiece), msg, i/5);
		}

		for (int i = len - 1; msg[i] == ' '; i--) {
			delCnt++;
		}

		for (int i = 0; i < len - delCnt; i++) {
			cout << msg[i];
		}

		cout << endl;

	}

	return 0;
}