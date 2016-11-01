
public class HelloWorld
{
 
  static int solution(int[] A) {
        // write your code in Java SE 8
        
        //BASE CASE:
        int len = A.length;
        if (len < 1){
            return -1;
        }
        else if (len == 1){
         return 0;
        }
        else{
            int [] sumUp = new int[len];
            int [] sumDown = new int[len];
            
            //INITIALIZE UP and DOWN;
            sumUp[0] = 0;
            sumDown[len-1] = 0;
            
            for (int i=1; i<len; i++){
                sumUp[i] = sumUp[i-1] + A[i-1];
            }
            for (int j=len-2; j>=0; j--){
                sumDown[j] = sumDown[j+1] + A[j+1];
            }

            //DEBUGGING:
            System.out.println("");
            for (int i=0; i<len; i++){
            	System.out.print(sumUp[i]+ " ");
            }
            System.out.println("");
            for (int j=0; j<len; j++){
                System.out.print(sumDown[j]+ " ");
            }
            
            
            //SOLUTIONS:
            for(int i = 0; i<len; i++){
                if (sumUp[i] == sumDown[i]){
                    return i;
                }
            }
            
            return -1;
        }
               
    }

   // arguments are passed using the text field below this editor
  public static void main(String[] args){
   	System.out.println("Hello World");
    int [] a = {-1};
    int [] a1 = {-1,-2,-3,-4,10,-4,-3,-2,-1};
    int [] a2 = {-1,-1,-1,-1,-1,-1,-1,-1,1,8,-7};
    int [] a3 = {0,0,0,0,0,0,0,0,0,0};
    int [] a4 = {1000000,20000,-100000,-20000,0};
    int [] a5 = {100,-100,100,-100,1,1,1,1,1,-1,-1,-1,-1,-1,-1};
    int [] a6 = {0};
    
    System.out.println("TEST 0. " + solution(a)); 
    System.out.println("TEST 1. " + solution(a1));
    System.out.println("TEST 2. " + solution(a2));
    System.out.println("TEST 3. " + solution(a3));
    System.out.println("TEST 4. " + solution(a4));
    System.out.println("TEST 5. " + solution(a5));
    System.out.println("TEST 6. " + solution(a6));
    
    
  }
  
}
