class ParkingSystem {
public:
    int parking[3];  // array<int, 3> parking;  是一样的
    ParkingSystem(int big, int medium, int small)
    {
        parking[0]=big;
        parking[1]=medium;
        parking[2]=small;
    }

    bool addCar(int carType)
    {
        if(parking[carType-1]>0)
        {
            parking[carType-1]--;
            return true;
        }
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */