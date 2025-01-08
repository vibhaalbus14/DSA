import java.util.Arrays;
public class App {
    public static void main(String[] args) throws Exception {
       int[] arr;//array declaration creates a reference variable in memory
        arr=new int[4];//instantiation of array
        arr[0]=1;//O(1)------->O(n)
        arr[1]=2;//O(1)
        arr[2]=3;//O(1)
        arr[3]=4;//O(1)
       System.out.println(Arrays.toString(arr));
        System.out.println(arr.toString());
        System.out.println(arr);
        int[] arr2={1,2,3,4};//O(1) time complexity
        System.out.println(Arrays.toString(arr2));
    }
}
