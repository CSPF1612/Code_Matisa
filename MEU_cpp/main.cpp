#include "robot.h"
#include <stdio.h>
using namespace std;

int main()
{
    Robot r1, r2;
    r1.id = 1;
    r1.pos[0] = 0;
    r1.pos[1] = 0;
    r1.showPos();

    r1.speed[0] = 3;
    r1.speed[1] = 4;
    float t = 4;
    r1.move(t);
    r1.showPos();

    float vx = 2.5;
    float vy = 5;
    r1.changeSpeed(vx, vy);
    r1.move(t);
    r1.showPos();

    return 0;
}