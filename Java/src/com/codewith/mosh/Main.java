package com.codewith.mosh;

import java.util.Arrays;

class Main {

    public static void main(String[] args) {
        var list = new LinkedList();
        list.addLast(10);
        list.addFirst(20);
        list.addFirst(30);
        System.out.println((list.indexOf(30)));
        System.out.println(list.contains(40));
        // list.removeLast();
        // // list.removeLast();
        System.out.println(Arrays.toString(list.toArray()));
        // list.removeLast();
        // System.out.println(list.first);
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