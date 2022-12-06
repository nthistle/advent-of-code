import java.util.Scanner;
import java.io.File;

public class Day14 {
    public static void main(String[] args) {
        int[] starting = new int[] {3, 7};
        Node tail = new Node(null, starting[0]);
        Node head = tail;
        for (int i = 1; i < starting.length; i++) {
            tail = (tail.next = new Node(null, starting[i]));
        }
        tail.next = head;
        
        Node elf1 = head;
        Node elf2 = head.next;
        
        int target = 84601; // 084601
        
        int rolling = 37;
        
        String part1 = "";
        
        int numRecipes = starting.length;
        
        while(true) {
            int elf1val = elf1.val;
            int elf2val = elf2.val;
            int sum = elf1val + elf2val;
            
            if (sum > 9) {
                tail = (tail.next = new Node(head, 1));
                numRecipes++;
                
                rolling = ((rolling * 10) + tail.val) % 1000000;
                if (rolling == target) {
                    System.out.println("Part 2: " + (numRecipes-6));
                    break;
                }
                
                if (numRecipes > target && numRecipes < (target + 11)) {
                    part1 += tail.val;
                }
            }
            tail = (tail.next = new Node(head, sum%10));
            numRecipes++;
            
            rolling = ((rolling * 10) + tail.val) % 1000000;
            if (rolling == target) {
                System.out.println("Part 2: " + (numRecipes-6));
                break;
            }
            
            if (numRecipes > target && numRecipes < (target + 11)) {
                part1 += tail.val;
            }
            
            for (int j = 0; j < 1 + elf1val; j++) elf1 = elf1.next;
            for (int j = 0; j < 1 + elf2val; j++) elf2 = elf2.next;
        }
        
        System.out.println("Part 1: " + part1);
    }
}

class Node {
    public Node next;
    public int val;
    
    public Node(Node next, int val) {
        this.next = next;
        this.val = val;
    }
}