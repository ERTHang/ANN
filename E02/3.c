#include <stdio.h>
#include <math.h>

double func(double x){
    return pow(x, 3) - 4*x -1;
}

int main(){
    double x, y;
    double xn;
    scanf("%lf%lf", &x, &y);
    for(int i=0;i<5;i++){
        xn = x*func(y) - y*func(x);
        xn /= (func(y) - func(x));
        if(func(xn)*func(x) < 0)
            y = xn;
        else
            x = xn;
        
        printf("%.8lf\n", xn);
    }
}