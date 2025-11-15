package com.codewith.mosh;

public class LinkedList {
    private class Node {
        private int value;
        private Node next;
        Node(int value) {
            this.value = value;
        }
    }
    private Node first;
    private Node last;
    private boolean isEmpty(){
        return first == null;
    }
    public void addLast(int value) {
        var node = new Node(value);
        if (isEmpty()) {
            first = last = node;
        } else {
            last.next = node;
            last = node;
        }
    }
    public void addFirst(int value) {
        var node = new Node(value);
        if (isEmpty()){
            first = last = node;
        }
        else {
            node.next = first;
            first = node;
        }
    }
    public int indexOf(int item) {
        int index = 0;
        // boolean found = false;
        var currentNode = first;
        while (currentNode != null) {
            if (currentNode.value == item) return index;
            currentNode = currentNode.next;
            index++;
        }
        return -1;
    }
}
