import java.util.ArrayList;
import java.util.Arrays;

public class disc2 {
	
	public static ArrayList<Integer> findIndexList( ArrayList<Integer> list, int target ){
		
		ArrayList<Integer> indexList = new ArrayList <Integer>();
	
		for (int i = 0; i < list.size(); ++i ){

			if ( list.get(i) == target ){   // Comparing a wrapper class object with a primitive variable.
				indexList.add(i);		
			} 
		}
		return indexList;	
	}

	public static void main(String[] args){

		int target = 2;
		
		ArrayList<Integer> arrayList1 = new ArrayList<Integer>(Arrays.asList(2,1,1,1,2,2,2,1));
		ArrayList<Integer> arrayList2 = new ArrayList<Integer>(Arrays.asList(1,2,3,4,5,6));
		ArrayList<Integer> arrayList3 = new ArrayList<Integer>(Arrays.asList(2,2,2,2,-2,-2,-2));
		ArrayList<Integer> arrayList4 = new ArrayList<Integer>(Arrays.asList(2,2,100,200,300,400));
		
		System.out.println( findIndexList(arrayList1, target) ); // return [0, 4, 5, 6]
		System.out.println( findIndexList(arrayList2, target) ); // returns [1]
		System.out.println( findIndexList(arrayList3, target) ); // returns [0, 1, 2, 3]
		System.out.println( findIndexList(arrayList4, target) ); // returns [0, 1]
	}
}
