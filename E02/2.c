#include <stdio.h>
#include <math.h>

double func(double x){
    return pow(x, 3) - 4*x -1;
}

int main(){
    double x[6];
    scanf("%lf%lf", &x[0], &x[1]);
    for (size_t i = 1; i < 5; i++)
    {
        printf("x%lu = %.7lf, x%lu = %.7lf\n", (i), x[i - 1], (i + 1), x[i]);
        x[i + 1] = -x[i] * func(x[i - 1]) + x[i - 1] * func(x[i]);
        x[i + 1] /= (func(x[i]) - func(x[i - 1]));
    }
}