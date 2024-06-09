#include "robot.h"
#include <iostream>
using namespace std;

void Robot::showPos()
{
    std::cout << "Posição X: " << this->pos[0] << std::endl;
    std::cout << "Posição Y: " << this->pos[1] << std::endl;
}

void Robot::move(float t)
{
    this->pos[0] += this->speed[0]*t;
    this->pos[1] += this->speed[1]*t;
}

void Robot::changeSpeed(float vx, float vy)
{
    this->speed[0] = vx;
    this->speed[1] = vy;
}