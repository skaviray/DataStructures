package com.codewith.mosh;

import java.util.NoSuchElementException;

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
    private int size;
    // private int[] list;
    private boolean isEmpty(){
        return first == null;
    }
    private Node getPrevious(Node item) {
        var currentNode = first;
        while(currentNode != null) {
            if (currentNode.next == item) return currentNode;
            currentNode = currentNode.next;   
        } 
        return null;
    }
    public void addLast(int value) {
        var node = new Node(value);
        if (isEmpty()) {
            first = last = node;
        } else {
            last.next = node;
            last = node;
        }
        size++;
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
        size++;
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
    public boolean contains(int item) {
        return indexOf(item) != -1;
    }
    public void removeFirst() {
        if (isEmpty()) {
            throw  new NoSuchElementException();
        }
        if (first == last) {
            first = last = null;
        } else {
        var second = first.next;
        first.next = null;
        first = second;
        }

        size--;
    }
    public void removeLast() {
        if (isEmpty()) {
            throw  new NoSuchElementException();
        }
        if (first == last) {
            first = last = null;
        } else {
            var previousNode = getPrevious(last);
            last = previousNode;
            last.next = null;
        }
        size--;
    }
    public int size() {
        return size;
    }
    public int[] toArray() {
        int[] array = new  int[size];
        var current = first;
        var index = 0;
        while (current != null ) {
            array[index++] = current.value;
            current = current.next;
        }
        return array;
    }
}
