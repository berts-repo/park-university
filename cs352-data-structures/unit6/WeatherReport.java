import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.Scanner;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.io.FileNotFoundException;
import java.util.Map;
import java.util.TreeMap;

/**
 * Bert Darnell
 *  7/15/2023
 *  Unit6 Assignment2
 *
 *  This assignment builds a class to create, populate and search for items in different data structures then compare the execution time of each implementation.
 * 
 */
public class WeatherReport {
    
    private LinkedList<ExtremeWeather> fromData;

    // Step 1: Constructor for testing
    public WeatherReport() {
        fromData = new LinkedList<>();

        ExtremeWeather extreme1 = new ExtremeWeather("city1", "state1", 50, 10.1, 0.1);
        ExtremeWeather extreme2 = new ExtremeWeather("city2", "state2", 55, 19.2, 0.2);
        ExtremeWeather extreme3 = new ExtremeWeather("city3", "state3", 60, 12.3, 2.3);
        ExtremeWeather extreme4 = new ExtremeWeather("city4", "state4", 65, 13.4, 0.4);
        ExtremeWeather extreme5 = new ExtremeWeather("city5", "state5", 70, 14.5, 0.5);
        ExtremeWeather extreme6 = new ExtremeWeather("city6", "state6", 75, 15.6, 0.6);
        ExtremeWeather extreme7 = new ExtremeWeather("city7", "state7", 80, 16.7, 0.7);
        ExtremeWeather extreme8 = new ExtremeWeather("city8", "state8", 85, 17.8, 0.8);

        fromData.add(extreme1);
        fromData.add(extreme2);
        fromData.add(extreme3);
        fromData.add(extreme4);
        fromData.add(extreme5);
        fromData.add(extreme6);
        fromData.add(extreme7);
        fromData.add(extreme8);
    }

    // Step 2: from file constructor
    public WeatherReport(String fileName) throws FileNotFoundException {
        fromData = new LinkedList<>();

        File file = new File(fileName);
        Scanner scanner = new Scanner(file);

        // Skip the header row
        if (scanner.hasNextLine()) {
            scanner.nextLine();
        }

        // Read temperature recordings
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String[] data = line.split(",");

            // Assigns each element in the table to a variable
            int average = Integer.parseInt(data[0]);
            String city = data[1];
            String code = data[2];
            int direction = Integer.parseInt(data[3]);
            String fullDate = data[4];
            int maxTemp = Integer.parseInt(data[5]);
            int minTemp = Integer.parseInt(data[6]);
            String month = data[7];
            double precipitation = Double.parseDouble(data[8]);
            double windSpeed = Double.parseDouble(data[9]);
            String state = data[10];
            int day = Integer.parseInt(data[11]);
            int year = Integer.parseInt(data[12]);

            // Creates the ExtreemeWeather report
            ExtremeWeather element = new ExtremeWeather(city, state, maxTemp, windSpeed, precipitation);
            fromData.add(element);
        }

        scanner.close();
    }

    // Step 3: makes a new list that records the city with the highest temperature, fastest winds, and most prcipitation
    public ArrayList<ExtremeWeather> computeByList() {
        ArrayList<ExtremeWeather> computedList = new ArrayList<>();

        ExtremeWeather maxTempCity = null;
        ExtremeWeather maxPrecipCity = null;
        ExtremeWeather maxWindCity = null;

        // finds the highest temperature, most precipitation, and highest wind speeds.
        for (ExtremeWeather data : fromData) {
            if (maxTempCity == null || data.getHigh() > maxTempCity.getHigh()) {
                maxTempCity = data;
            }

            if (maxPrecipCity == null || data.getPrecipitation() > maxPrecipCity.getPrecipitation()) {
                maxPrecipCity = data;
            }

            if (maxWindCity == null || data.getWindSpeed() > maxWindCity.getWindSpeed()) {
                maxWindCity = data;
            }
        }

            // creates ArrayList to store the most extreme weather cities
            computedList.add(maxTempCity);
            computedList.add(maxPrecipCity);
            computedList.add(maxWindCity);

        return computedList;
    }
    
    // Step 4: makes a new tree map that records the city with the highest temperature, fastest winds, and most prcipitation
    public TreeMap<String, ExtremeWeather> computeByTree() {
        TreeMap<String, ExtremeWeather> computedTree = new TreeMap<>();

        ExtremeWeather maxTempCity = null;
        ExtremeWeather maxPrecipCity = null;
        ExtremeWeather maxWindCity = null;

        // finds the highest temperature, most precipitation, and highest wind speeds.
        for (ExtremeWeather data : fromData) {
            if (maxTempCity == null || data.getHigh() > maxTempCity.getHigh()) {
                maxTempCity = data;
            }

            if (maxPrecipCity == null || data.getPrecipitation() > maxPrecipCity.getPrecipitation()) {
                maxPrecipCity = data;
            }

            if (maxWindCity == null || data.getWindSpeed() > maxWindCity.getWindSpeed()) {
                maxWindCity = data;
            }
        }

            computedTree.put("city with Highest Temperature", maxTempCity);
            computedTree.put("city with Most Precipitation", maxPrecipCity);
            computedTree.put("city with Highest Wind Speed", maxWindCity);

        return computedTree;

    }

/*****************************************************************************************************
 *
 *  Unit 5
 *
 * */

    // return true if sorted by city
    public Boolean isSortedByCity(){

        for (int i = 0; i < fromData.size() - 1; i++){
            ExtremeWeather current = fromData.get(i);
            ExtremeWeather next = fromData.get(i+1);
            int check = current.getCity().compareTo(next.getCity());
            if (check > 0) { 
                return false; 
            }
        } 
        return true;
    }
        
        // return true if sorted by highest temperature
        public Boolean isSortedByHigh(){
        
        for (int i = 0; i < fromData.size() - 1; i++){
            ExtremeWeather current = fromData.get(i);
            ExtremeWeather next = fromData.get(i+1);

            if (current.getHigh() > next.getHigh()) { 
                return false;
            }

        }
        return true;
    }

    // sorts with Collection by city or high temperature
    public void sortWithCollections(String by) {
        if (by.equals("City")) {
            Collections.sort(fromData, new SortByCity());
        } else if (by.equals("High")) {
            Collections.sort(fromData, new SortByHigh());
        } else {
            System.out.println("Invalid sort option");
        }
    }

    // sorts by city or high temperature, using the Merge sort and calling it recursivly
    public void sortWithMerge(String by) {
        if (by.equals("City")) {
            fromData = mergeSort(fromData, new SortByCity());
        } else if (by.equals("High")) {
            fromData = mergeSort(fromData, new SortByHigh());
        } else {
            System.out.println("Invalid sort option");
        }
    }
    
    // recurisve function to MergeSort a LinkedList
    private LinkedList<ExtremeWeather> mergeSort(LinkedList<ExtremeWeather> list, Comparator<ExtremeWeather> comparator) {
        if (list.size() <= 1) {
            return list;
        }

        // splits list in half
        int mid = list.size() / 2;
        LinkedList<ExtremeWeather> left = new LinkedList<>(list.subList(0, mid));
        LinkedList<ExtremeWeather> right = new LinkedList<>(list.subList(mid, list.size()));

        // recursively sorts each half, until each half reaches the base
        left = mergeSort(left, comparator);
        right = mergeSort(right, comparator);

        // calls merge(), starting with smallest recursive halfs first, and combines the list in a sorted order
        return merge(left, right, comparator);
    }

    // mergSort method calls this method to combine the halfed sections in order, according to comparator class.
    private LinkedList<ExtremeWeather> merge(LinkedList<ExtremeWeather> left, LinkedList<ExtremeWeather> right, Comparator<ExtremeWeather> comparator) {
        // stores merged and sorted
        LinkedList<ExtremeWeather> merged = new LinkedList<>();

        while (!left.isEmpty() && !right.isEmpty()) {
            //  If compare is less than or equal to 0 the element from the left is smaller or equal
            if (comparator.compare(left.getFirst(), right.getFirst()) <= 0) {
                merged.addLast(left.removeFirst());
            } else {
                merged.addLast(right.removeFirst());
            }
        }
        // adds remaining nodes if any
        merged.addAll(left);
        merged.addAll(right);

        return merged;
    }

}   // End WeatherReport


/*****************************************************************************************************
 * 
 * Comparator to sort by the city stored in a ExtremeWeather object
 */
class SortByCity implements Comparator<ExtremeWeather> {
    // Used for sorting in ascending order of City
    public int compare(ExtremeWeather t1, ExtremeWeather t2)
    {
        return t1.getCity().compareTo(t2.getCity());
    }
}

/*
 * Comparator to sort by the high temperature stored in a ExtremeWeather object
 */
class SortByHigh implements Comparator<ExtremeWeather> {
    // Used for sorting in ascending order of high temperature
    public int compare(ExtremeWeather t1, ExtremeWeather t2)
    {
        return t1.getHigh() - t2.getHigh();
    }
}
