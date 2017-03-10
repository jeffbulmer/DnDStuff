package WorldSim;

import com.sun.org.apache.bcel.internal.generic.POP;

import java.util.ArrayList;

/**
 * Created by robert on 03/02/17.
 */


/**
 * A City has the following:
 *  Population
 *  Army
 *  And resources.
 *  Resources include:
 *    Gold
 *    Ore
 *    Gems
 *    Food
  */

/** A City will have a number of Workers
 *  Priority goes to farmers
 *  From there,
 */

public class City {
    private ArrayList<City> connections;
    private ArrayList<Mine> mines;
    private int population;
    private int size;
    private int army;
    public double farmers;
    public double ore_miners;

    public City(int Population){
        this.connections = new ArrayList<City>();
        this.mines = new ArrayList<Mine>();
        this.population = Population;
        this.army = Population / 10;
        this.size = 3;
        this.generateWorkers();
    }
    public City(int Population, boolean hasArmy){
        this.connections = new ArrayList<City>();
        this.population = Population;
        if (hasArmy){
            this.army = Population / 100;
        } else {
            this.army = 0;
        }
    }
    public void connectsWith(City partner){
        this.connections.add(partner);
    }

    // RESOURCE FUNCTIONS
      // LAND
    public Double residentialLand() {
        return this.population * 0.0005;
    }
    private Double farmlandAvailable(){
        return Math.max(0, this.size - this.residentialLand());
    }
    private Double farmlandNeeded() {
        // This is actually all that is needed
        // 1 square kilometer can feed 1500 people off sweet potatoes
        // If we have pop 1500 we need ~ 1 square kilometer
        return (this.population / 1500.00);
    }
      // FOOD
    public Double foodNeeded() {
        return this.population * 31.00;
    }
      // MINES
    public void openMine(){

        this.mines.add(new Mine());

    }
        //ORE
    public Double oreNeeded(){
        return this.army * 6.00;
    }

    // CITIZEN FUNCTIONS
    private Double workingPopulation() {
        Double l = (this.population * 0.35);
        return l;
    }
    public void mineOre(){
        Double remaining_miners = this.ore_miners;
        while (remaining_miners > 0){
            
        }
    }
    public void generateWorkers() {
        //carpenters
        Double totalNeed = this.oreNeeded() + this.foodNeeded();
        Double workers = this.workingPopulation() - this.army;
        Double farmers_required =
                Math.min(Math.min(Math.ceil(this.farmlandNeeded() * 50),
                                  Math.ceil(this.farmlandAvailable() * 50)),
                        workers);

        Double miners_required = Math.min(Math.ceil(oreNeeded() / (31)),
                                          workers - farmers_required);

        Double remaining_workers = workers - farmers_required - miners_required;

        Double randfactor = Math.random();


        long extra_farmers = Math.round(Math.min(
                (1 - randfactor) * remaining_workers,
                (this.farmlandAvailable() * 50) - farmers_required));

        long extra_miners = Math.round(Math.max(randfactor * remaining_workers, remaining_workers - extra_farmers));

        System.out.println("FARMERS REQUIRED: " + Double.toString(farmers_required));
        System.out.println("MINERS REQUIRED: " + Double.toString(miners_required));
        System.out.println("REMAINING WORKERS: " + Double.toString(remaining_workers));
        System.out.println("FARMERS EXTRA: " + Double.toString(extra_farmers));
        System.out.println("MINERS EXTRA: " + Double.toString(extra_miners));
    }

}
