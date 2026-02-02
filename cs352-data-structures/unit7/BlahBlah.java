import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.TreeMap;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;

public class BlahBlah {

	public static List<String> readWords(String filePath) {
		// List for storing words from file
		List<String> wordsList = new ArrayList<>();
		try {
			File file = new File(filePath);
			Scanner scanner = new Scanner(file);
			while (scanner.hasNext()) {
				String word = scanner.next();
				// Remove commas, periods, question marks, exclamation points, and capitalization
				word = word.replaceAll("[,.?!]", "");
				wordsList.add(word.toLowerCase());
			}
			scanner.close();
		} catch (IOException e) {
			System.out.println("Unable to read file");
		}

		return wordsList;
	}

	public static Map<String, Integer> wordCountUsingTreeMap(List<String> wordsList) {
		
		Map<String, Integer> wordCount = new TreeMap<>();
		
		for (String word : wordsList) {
			// If there is a new word it sets the count to 1, else if word is in list it increments the word's count by 1.
			if (!wordCount.containsKey(word)) {
				wordCount.put(word, 1);
			} else { wordCount.put(word, wordCount.get(word) + 1); }
		}

		return wordCount;
	}

	public static Map<String, Integer> wordCountUsingHashMap(List<String> wordsList) {

		Map<String, Integer> wordCount = new HashMap<>();

		for (String word : wordsList){
			// If there is a new word it sets the count to 1, else if word is in list it increments the word's count by 1.
			if (!wordCount.containsKey(word)) {
				wordCount.put(word, 1);
			} else { wordCount.put(word, wordCount.get(word) + 1); }
		}
		return wordCount;
	}

	public static void main(String[] args) {
		String filePath = "theOdyssey.txt";
		List<String> wordsList = readWords(filePath);

		// Start the TreeMap comparison to HashMap
		System.out.println("------------------------------");
		System.out.println("Starting the TreeMap timer");	
		long startTimeTreeMap = System.currentTimeMillis();
		
		Map<String, Integer> wordCountTreeMap = wordCountUsingTreeMap(wordsList);
		TreeMap<String, Integer> sortedWordCountTreeMap = new TreeMap<>();

		// Count words and filter out those with a length <= 6 characters
		for (Map.Entry<String, Integer> entry : wordCountTreeMap.entrySet()) {
			String word = entry.getKey();
			int count = entry.getValue();
			if (word.length() > 6) {
				sortedWordCountTreeMap.put(word, count);
			}
		}

		// Print only the top 5 from TreeMap
		int countTreeMap = 0;
		for (Map.Entry<String, Integer> entry : sortedWordCountTreeMap.entrySet()) {
			if (countTreeMap >= 5) {
				break;
			}
			System.out.println(entry.getKey() + " " + entry.getValue());
			countTreeMap++;
		}

		// Stop the TreeMap timer
		long endTimeTreeMap = System.currentTimeMillis();
		long executionTimeTreeMap = endTimeTreeMap - startTimeTreeMap;
		System.out.println("Run time: " + executionTimeTreeMap + " milliseconds");

		System.out.println("------------------------------");
		System.out.println("Starting the HashMap timer");

		// Start the HashMap comparison to TreeMap
		long startTimeHashMap = System.currentTimeMillis();
		Map<String, Integer> wordCountHashMap = wordCountUsingHashMap(wordsList);
		HashMap<String, Integer> sortedWordCountHashMap = new HashMap<>();

		// Count words and filter out those with a length > 6 characters using HashMap
		for (Map.Entry<String, Integer> entry : wordCountHashMap.entrySet()) {
			String word = entry.getKey();
			int countHashMap = entry.getValue();
			if (word.length() > 6) {
				sortedWordCountHashMap.put(word, countHashMap);
			}
		}

		// Print only the top 5 from HashMap
		int countHashMap = 0;
		for (Map.Entry<String, Integer> entry : sortedWordCountHashMap.entrySet()) {
			if (countHashMap >= 5) {
				break;
			}
			System.out.println(entry.getKey() + " " + entry.getValue());
			countHashMap++;
		}

		// Stop the HashMap timer
		long endTimeHashMap = System.currentTimeMillis();
		long executionTimeHashMap = endTimeHashMap - startTimeHashMap;
		System.out.println("Run time: " + executionTimeHashMap + " milliseconds");
		System.out.println("------------------------------");
	}
}
