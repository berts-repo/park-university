import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;
import java.util.Comparator;
import java.util.LinkedList;

/**
 * Bert Darnell
 * Professor David  
 * CS352 Unit5
 * 7/15/2023
 *
 *  This assignment builds a class to create, populate and search for items in different data structures then compare the execution time of each implementation.
 *
 *  Extreme weather class for storing the cities with the highest winds, most precipitation, and hotest temperatures. 
 */

class ExtremeWeather {
    private String city;
    private String state;
    private int high;
    private double windSpeed;
    private double precipitation;

    public ExtremeWeather(String city, String state, int temperature, double windSpeed, double precipitation) {
        this.city = city;
        this.state = state;
        this.high = temperature;
        this.windSpeed = windSpeed;
        this.precipitation = precipitation;
    }

    public int getHigh() {
        return high;
    }

    public double getWindSpeed() {
        return windSpeed;
    }

    public double getPrecipitation() {
        return precipitation;
    }

    public String getCity() {
        return city;
    }

    public String getState(){
        return state;
    }
}
