package com.codewith.mosh;

import java.util.HashMap;
import java.util.Map;

class Main {
    public static Character getFirstNonRepeatedChar(String str) {
        Map<Character,Integer> frequentlyRepeteadString = new  HashMap<>();
        for (var ch : str.toCharArray()) {
            if (frequentlyRepeteadString.containsKey(ch)) {
                var currentCount = frequentlyRepeteadString.get(ch);
                frequentlyRepeteadString.put(ch, currentCount + 1);
            } else {
                frequentlyRepeteadString.put(ch, 1);
            }
        }
        for (var ch : str.toCharArray()) {
            if (frequentlyRepeteadString.get(ch) == 1) {
                return  ch;
            }
        }
        return null;
    }
    public static void main(String[] args) {
        // Map<Integer,String> map = new  HashMap<>();
        // map.put(1,"shiva");
        // map.put(2,"Manasa");
        // map.put(3,"Amulya");
        // System.out.println(map.get(2))
        var input = "a green apple";
        var firstNonRepeatedChar = getFirstNonRepeatedChar(input);
        System.out.println(firstNonRepeatedChar);
    }
    }

// public class Sample {
//     public static void main (String[]args) {
//         System.err.println("This is the sample");
//     }
//     // public static String Hello () {
//     //     return  "Hello";
//     // }
// }