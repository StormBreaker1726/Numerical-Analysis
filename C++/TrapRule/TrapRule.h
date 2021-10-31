#ifndef D32577D7_F152_4ADE_86C6_B0EED2ED045B
#define D32577D7_F152_4ADE_86C6_B0EED2ED045B

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>

using namespace std;

string error(short int code){
    switch (code)
    {
    case 1:
        return "Division by Zero";
        break;
    case 2:
        return "Invalid Interval";
        break;
    default:
        return "Unkown Error";
        break;
    }
}

double f(double x){
    return (sqrt(pow(x,3)-1));
}


double TrapRule(double a, double b, long int n){
    double h, x, soma, R;
    long int i;
    R = -0;
    if(n == 0){
        cout<<error(1)<<endl;
    }
    else{
        if(n < 0){
            cout<<error(2)<<endl;
        }
        else{
            h = (b - a)/n;
            x = a + h;
            soma = 0;

            for(i = 1; i <= n-1; i++){
                soma = soma + f(x);
                x = x + h;
            }

            R = h * ((f(a) + f(b))/2 + soma);
        }
    }
    return R;
}

#endif /* D32577D7_F152_4ADE_86C6_B0EED2ED045B */
