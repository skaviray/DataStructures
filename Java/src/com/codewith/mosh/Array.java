package com.codewith.mosh;
public class Array {
    private int[] items;
    private int count;
    public Array(int length) {
        items = new  int[length];
    };

    // public static void main(String[] args) {
    //     System.out.println("length");
    // }
    public void print() {
        for (int i=0;i<items.length;i++){
            System.out.println(items[i]);
        }
    }
    public void insert(int item) {
        // System.out.println(count);
        if (items.length == count) {
            int [] newItems = new int[count * 2];
            for(int i=0; i< count; i++){
                newItems[i] = items[i];
            }
            items = newItems;
        }
        items[count++] = item; 
    }
    public int  indexOf(int item){
        for (int i=0;i<items.length;i++){
            // System.out.println(items[i]);
            if (items[i] == item) {
                return i;
            }
        }
        return -1;
    }
    public void removeAt(int index) {
        if (index <0 || index >= count) {
            throw new IllegalArgumentException();
        }
        for (int i = index; i <count-1; i++){
            items[i] = items[i+1];
        }
        items[count-1] = 0;
        count--;
    }
    // public void Insert(int number) {
    //     System.out.println(this.length);
    // }
}
