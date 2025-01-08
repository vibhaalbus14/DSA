import java.util.Scanner;
import java.util.Arrays;

public class temp 
{
Scanner scanner=new Scanner(System.in);
private float[] temp_array;
double avg;
float sum=0;
int count=0;

public temp(int n)
{
 temp_array=new float[n];
for(int i=0;i<n;i++)
{
    Arrays.fill(temp_array,Integer.MIN_VALUE);

}
}


public void insert()
{
    for(int i=0;i<temp_array.length;i++)
    {
        try
        {
        if(temp_array[i]==Integer.MIN_VALUE)
        {System.out.println("enter temperature");
        temp_array[i]=scanner.nextFloat();
        System.out.println(Arrays.toString(temp_array));
        }
        }
    
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("duplicate value or index error");
        }

    }
}


public void avg_calc()
{   
    for(float i:temp_array)
    {
        sum+=i;
    }
    avg=sum/temp_array.length;
    System.out.println("average temperature is:"+avg);

}

public int return_counts( )
{
for(float i:temp_array)
{
    if(i>=avg)
    
    {
        count++;
    }
}
    return count;

}

}
