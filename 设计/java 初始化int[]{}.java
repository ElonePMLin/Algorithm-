class ParkingSystem {
    private int[] carTypes;

    public ParkingSystem(int big, int medium, int small) {
        carTypes = new int[]{big, medium, small};
    }

    public boolean addCar(int carType) {
        if (carTypes[carType - 1] > 0) {
            carTypes[carType - 1]--;
            return true;
        }
        return false;
    }
}