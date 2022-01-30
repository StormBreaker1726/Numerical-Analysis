#ifndef A4AD2980_CD7D_4F5A_9FFC_B37D0E951C78
#define A4AD2980_CD7D_4F5A_9FFC_B37D0E951C78

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <fstream>
#include <chrono>

double f(double x, double y){
    return (sqrt((pow(x, 2)+4*y)));
}

double EulersMethod(double x0, double y0, long int n, double xn){
    int i = 0;

    double yn;

    double h = (xn - x0)/n;

    while(i < n){
        yn = y0 + h * f(x0 + i*h, y0);

        y0 = yn;

        i++;
    }

    return yn;
}

#endif /* A4AD2980_CD7D_4F5A_9FFC_B37D0E951C78 */
