import java.util.Scanner;
import java.io.File;

public class Day9 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(new File("input.txt"));
        String input = sc.nextLine();
        sc.close();
        
        int numPlayers = Integer.parseInt(input.split(" ")[0]);
        int maxMarble = Integer.parseInt(input.split(" ")[6]);
        
        System.out.println("Part 1: " + getScore(numPlayers, maxMarble));
        System.out.println("Part 2: " + getScore(numPlayers, 100*maxMarble));
    }
    
    public static long getScore(int players, int marbles) {
        long[] scores = new long[players];
        Node n = new Node(null, null, 0);
        n.left = n;
        n.right = n;
        
        for (int val = 1; val <= marbles; val++) {
            if (val % 23 == 0) {
                for (int i = 0; i < 7; i++) n = n.right;
                scores[val % players] += val + n.val;
                n.left.right = n.right;
                n.right.left = n.left;
                n = n.left;
            } else {
                n = n.left;
                Node newNode = new Node(n.left, n, val);
                newNode.left.right = newNode;
                n.left = newNode;
                n = newNode;
            }
        }
        
        long max = 0;
        for (long val : scores) max = val > max ? val : max;
        return max;
    }
}

class Node {
    public Node left;
    public Node right;
    public int val;
    
    public Node(Node left, Node right, int val) {
        this.left = left;
        this.right = right;
        this.val = val;
    }
}