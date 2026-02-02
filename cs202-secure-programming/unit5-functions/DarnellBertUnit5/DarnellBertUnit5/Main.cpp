#include "Header.hpp"
char emptyStr[32] = ""; // empty string for pointer in printValues function

int main() {
    generateRandomValues();
	printValues(emptyStr);
	sortValues();
	printValues(emptyStr);
	modValues();
	printValues(emptyStr);
	sortValues();
	printValues(emptyStr);
}