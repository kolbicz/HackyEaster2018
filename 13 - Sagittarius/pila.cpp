// sample code accompanying the paper:
// "Analytical Methods for Squaring the Disc"
// http://arxiv.org/abs/1509.06344

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define epsilon 0.0000001

inline double sgn(double input)
{
    double output = 1.0f;
    if (input < 0.0) {
        output = -1.0f;
    }
    return output;
}

// Simple Stretching map
// mapping a circular disc to a square region
// input: (u,v) coordinates in the circle
// output: (x,y) coordinates in the square
void stretchDiscToSquare(double u, double v, double& x, double& y)
{
    if ( (fabs(u) < epsilon) || (fabs(v) < epsilon))  {
        x = u;
        y = v;
        return;
    } 

    double u2 = u * u;
    double v2 = v * v;
    double r = sqrt(u2 + v2);

    // a trick based on Dave Cline's idea
    // link Peter Shirley's blog
    if (u2 >= v2) {
        double sgnu = sgn(u);
        x = sgnu * r;
        y = sgnu * r * v / u;
    } else {
        double sgnv = sgn(v);
        x = sgnv * r * u / v;
        y = sgnv * r;
    }
    
}


// Simple Stretching map
// mapping a square region to a circular disc
// input: (x,y) coordinates in the square
// output: (u,v) coordinates in the circle
void stretchSquareToDisc(double x, double y, double& u, double& v)
{
    if ( (fabs(x) < epsilon) || (fabs(y) < epsilon))  {
        u = x;
        v = y;
        return;
    }
    
    double x2 = x*x;
    double y2 = y*y;
    double hypothenusSquared = x2 + y2;

    // code can use fast reciprocal sqrt doubleing point trick
    // https://en.wikipedia.org/wiki/Fast_inverse_square_root
    double reciprocalHypothenus =  1.0f/sqrt(hypothenusSquared);
    
    double multiplier = 1.0f;
    // a trick based on Dave Cline's idea
    if (x2 > y2) {
        multiplier = sgn(x) * x * reciprocalHypothenus;
    } else {
        multiplier = sgn(y) * y * reciprocalHypothenus;
    }

    u = x * multiplier;
    v = y * multiplier;
}


int main(int argc, char *argv[])
{
    double x,y;
    double u,v;

	FILE* fp;
	char buffer[255];

	fp = fopen("C:\\Users\\administrator\\Desktop\\hacky2018\\pila\\coordinates.txt", "r");

	while(fgets(buffer, 255, (FILE*) fp)) {
		sscanf(strtok(buffer, ","), "%lf", &u);
		sscanf(strtok(NULL, ","), "%lf", &v);
		stretchDiscToSquare(u,v,x,y);
		printf("%lf,%lf\n",x,y);
	}

	fclose(fp);    

    return 0;
}