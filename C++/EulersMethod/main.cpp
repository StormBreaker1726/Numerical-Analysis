#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <fstream>
#include <chrono>

using namespace std;

#include "EulersMethod.h"

int main(void){

    double x0 = 0; 
    double y0 = 3; 
    long int n = 8;
    double xn = 1;

    cout<<setprecision(20)<<EulersMethod(x0, y0, n, xn)<<endl;

    return 0;
}