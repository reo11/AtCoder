#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    double x, y;
    x = a * cos(c * M_PI / 180.0) - b * sin(c * M_PI / 180.0);
    y = a * sin(c * M_PI / 180.0) + b * cos(c * M_PI / 180.0);

    printf("%f %f\n", x, y);
}