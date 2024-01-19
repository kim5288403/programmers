import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum = 0;
        long sumA = 0;
        long max = 0;
        boolean flag = false;
        
        Queue<Long> a = new LinkedList<>();
        Queue<Long> b = new LinkedList<>();
        
        for (int i = 0; i < queue1.length; i++) {
            a.add((long)queue1[i]);
            b.add((long)queue2[i]);
            sumA += queue1[i];
            sum += queue1[i];
            sum += queue2[i];
            max = queue1[i] > max ? queue1[i] : max;
            max = queue2[i] > max ? queue2[i] : max;
        }
        
        long target = sum / 2;
        
        long gap = target - sumA;
        
        if (sum - max < max) return -1;
        
        while(b.size() != 0) {
            if(gap == 0) {
                flag = true;
                break;
            } else if(gap > 0) {
                gap -= b.peek();
                a.add(b.poll());
                answer++;
            } else {
              gap += a.poll();
              answer++;
          }
            
        }
        
        if (!flag) {
            answer = -1;
        }
        
        return answer;
        
    }
}