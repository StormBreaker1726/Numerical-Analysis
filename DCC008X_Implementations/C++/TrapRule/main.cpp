#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <fstream>
#include <chrono>
using namespace std;

#include "TrapRule.h"

int main(void){

    fstream file;

    file.open("results.txt", ios::app|ios::out);

    file<<"\n\n"<<endl;

    double h, x, soma, R, a, b, greater, smaller;
    long int i, n;
    double original = 1.51592;
    int tam = 1000000;
    double bError[2];
    double sError[2];
    n = 1;
    a = 1;
    b = 2;
    i = 0;
    double error;
    file<<"-----------------------------------------------------------------------------------------------------------------"<<endl;
    auto start = std::chrono::steady_clock::now();
    for(; n <= tam; n++){
        R = TrapRule(a, b, n);
        file<<"Value found was "<<setprecision(30)<<R<<
        ", with pass "<<n<<" "<<endl;
        error = abs((R-original)/original);
        if(n == 1){
            greater = smaller = R;
            bError[0] = sError[0] = error;
            bError[1] = sError[1] = n; 
        }
        if(R < smaller){
            smaller = R;
        }
        if(R > greater){
            greater = R;
        }
        if(error > bError[0]){
            bError[0] = error;
            bError[1] = n;
        }
        if(error < sError[0]){
            sError[0] = error;
            sError[1] = n;
        }

    }
    auto end = std::chrono::steady_clock::now();
    file<<"-----------------------------------------------------------------------------------------------------------------"<<endl;

    std::chrono::duration<double> elapsed_seconds = end-start;

    file<<"Difference between the smaller and the greater:  "<<setprecision(30)<<(greater - smaller)<<endl;
    file<<"The biggest error found was with pass "<<bError[1]<<", and was "<<setprecision(50)<<bError[0]<<" "<<endl;
    file<<"The smallest error found was with pass "<<sError[1]<<", and was "<<setprecision(50)<<sError[0]<<" "<<endl;
    file<<"Time to calculate the "<<tam<<" values: "<<elapsed_seconds.count()<<" seconds "<<endl;

    file.close();

    return 0;
}