package WorldSim;

import java.util.ArrayList;

/**
 * Created by robert on 03/02/17.
 */
public class World {
    private ArrayList<City> cities;
    public World(){
        this.cities = new ArrayList<City>();
    }
    public void containsCity(City c){
        this.cities.add(c);
    }
    public void oreAvailable(){
        for (City city : cities) {
            System.out.println(city.oreMined(););
        }
    }
}
