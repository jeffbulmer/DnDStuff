package WorldSim;

/**
 * Created by robert on 03/02/17.
 */
public class Simulation {

    public static void main(String [ ] args) {
        City Breadstol =  new City(1000);
        City Ryeport = new City(2500);
        Breadstol.connectsWith(Ryeport);



    }
}
