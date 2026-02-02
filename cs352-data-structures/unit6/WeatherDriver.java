import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.TreeMap;
import java.util.Date;
/**
 * Bert Darnell
 * Professor David  
 * CS352 Unit5
 * 7/15/2023
 *
 *  This assignment builds a class to create, populate and search for items in different data structures then compare the execution time of each implementation.
 */
class WeatherDriver {
	public static void main(String[] args) {
		System.out.println("Starting simulation");
		System.out.println("---------------------------------------");
		
		// Create a new WeatherReport object from the file "weather.txt"
		try {
			WeatherReport report = new WeatherReport("weather.txt");

			long startTime;
			long endTime;
			long elapsedTime;

			System.out.println("Computed List:");
			System.out.println("---------------------------------------");

			// compute ArrayList
			startTime = System.currentTimeMillis();
			ArrayList<ExtremeWeather> computedList = report.computeByList();

			ExtremeWeather maxTempCity1 = computedList.get(0);
			ExtremeWeather maxPrecipCity1 = computedList.get(1);
			ExtremeWeather maxWindCity1 = computedList.get(2);

			System.out.println("City with Highest Temperature:");
			System.out.println("City: " + maxTempCity1.getCity());
			System.out.println("State: " + maxTempCity1.getState());
			System.out.println("High Temperature: " + maxTempCity1.getHigh());
			System.out.println("---------------------------------------");

			System.out.println("City with Most Precipitation:");
			System.out.println("City: " + maxPrecipCity1.getCity());
			System.out.println("State: " + maxPrecipCity1.getState());
			System.out.println("High Temperature: " + maxPrecipCity1.getPrecipitation());
			System.out.println("---------------------------------------");

			System.out.println("City with Highest Wind Speed:");
			System.out.println("City: " + maxWindCity1.getCity());
			System.out.println("State: " + maxWindCity1.getState());
			System.out.println("High Temperature: " + maxWindCity1.getWindSpeed());
			System.out.println("---------------------------------------");

			endTime = System.currentTimeMillis();
			elapsedTime = endTime - startTime;
			System.out.println("Compute by list run time: " + elapsedTime);
			System.out.println("---------------------------------------");

			System.out.println("---------------------------------------");
			System.out.println("Computed TreeMap:");
			System.out.println("---------------------------------------");

			// compute TreeMap
			startTime = System.currentTimeMillis();
			TreeMap<String, ExtremeWeather> computedTree = report.computeByTree();

			ExtremeWeather maxTempCity = computedTree.get("city with Highest Temperature");
			ExtremeWeather maxPrecipCity = computedTree.get("city with Most Precipitation");
			ExtremeWeather maxWindCity = computedTree.get("city with Highest Wind Speed");

			if (maxTempCity != null) {
				System.out.println("City with Highest Temperature:");
				System.out.println("City: " + maxTempCity.getCity());
				System.out.println("State: " + maxTempCity.getState());
				System.out.println("High Temperature: " + maxTempCity.getHigh());
				System.out.println("---------------------------------------");
			}

			if (maxPrecipCity != null) {
				System.out.println("City with Most Precipitation:");
				System.out.println("City: " + maxPrecipCity.getCity());
				System.out.println("State: " + maxPrecipCity.getState());
				System.out.println("Precipitation: " + maxPrecipCity.getPrecipitation());
				System.out.println("---------------------------------------");
			}

			if (maxWindCity != null) {
				System.out.println("City with Highest Wind Speed:");
				System.out.println("City: " + maxWindCity.getCity());
				System.out.println("State: " + maxWindCity.getState());
				System.out.println("Wind Speed: " + maxWindCity.getWindSpeed());
				System.out.println("---------------------------------------");

			}
			endTime = System.currentTimeMillis();
			elapsedTime = endTime - startTime;
			System.out.println("Compute by tree run time: " + elapsedTime);

		} catch (FileNotFoundException e) {
			System.out.println("File not found: weather.txt");
		}


		System.out.println("---------------------------------------");
		System.out.println("Finished simulation");
	}
}
