#include <stdio.h>
#include <math.h>

double func(double x){
    return pow(x, 3) - 4*x -1;
}

double derfunc(double x){
    return 3 * pow(x, 2) - 4;
}

int main(){
    double p1, res;
    scanf("%lf", &p1);
    res = p1;
    for (size_t i = 1; i <= 5; i++)
    {
        printf("x%lu = %.7lf\n", i, res);
        res = res - func(res) / derfunc(res);
    }
    
}