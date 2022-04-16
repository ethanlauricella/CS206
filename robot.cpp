#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <unistd.h>
using namespace std;


// Run pythons files from here
int main(int argc, char* argv[]) {

    string line;

    string numGen = argv[1];

    cout << "<article>  Hello, here we run a simulation "
            "for our robots and receive the resulting evolved neurons"
            "after for x amount of generations."
            "This allows for long computations to be done on"
            "the website rather than your local machine.<br>"
            "Today, you are simulating "+ numGen + " Generations<br>" << endl;


    string command = "python3 search.py " + string(numGen);
    system(command.c_str());

    // Open the Fitness file
    ifstream inFile;
    inFile.open("../Data/Final.txt");

    // Print to an article html element
    cout << "<h3>Fitness Values</h3>" << endl;
    while (inFile) {
        getline(inFile, line);
        // Print the line to the article and put a break tag to go to the next line
        cout << line << "<br>";
    }
    inFile.close();

    cout << "</article>" << endl;


    return 0;
}