#ifndef ROBOT_H
#define ROBOT_H

class Robot
{
    private:
    public:
        int id;
        float pos[2];
        float speed [2];
        void showPos();
        void move(float t);
        void changeSpeed(float, float);
};

#endif