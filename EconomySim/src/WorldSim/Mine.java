package WorldSim;

/**
 * Created by robert on 03/02/17.
 */
public class Mine {
    private Double resources;
    public Mine(){
        Long l = Math.round(100000.00 * Math.random());
        this.resources = l.doubleValue();
        System.out.println(this.resources);
    }

    public Double oreMined(int miners){
        return   miners * 31.0;
    }
}
