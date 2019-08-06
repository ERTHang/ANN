#include <stdio.h>
#include <math.h>

double func(double x){
    return (pow(x, 5) - (4 * x) - 3);
}

double func2(double a, double b, double e){
    return (log(fabs(b - a)) - log(pow(10, e)))/log(2);
}

int main(){
    double a, b, p, n, e;
    int i = 1;
    printf("insira o intervalo [a, b] e apos a precisao(10^?): ");
    scanf("%lf%lf%lf", &a, &b, &e);
    n = ceil(func2(a, b, e));
    if(func(a)*func(b) < 0){
        while(i <= 8){
            p = (a + b) / 2.0;
            printf("iteracao %d: P = %lf\n", i, p);
            if(func(a) * func(p) < 0){
                b = p;
            }
            else if(func(p) * func(b) < 0){
                a = p;
            }
            else{
                printf("Raiz encontrada na iteracao %d\n", i);
            }
            i++;
        }
        printf("Raiz =~ %lf, a distancia de 10 ^ %.0lf pode ser obtido apos %.0lf iteracoes\n", p, e, n);
    }
    else{
        printf("Nao ha raiz entre esse intervalo\n");
    }
}