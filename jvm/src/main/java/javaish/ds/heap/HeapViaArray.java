package javaish.ds.heap;

import java.util.Arrays;

public class HeapViaArray {
    private int elems[];

    public HeapViaArray() {
        elems = new int[0];
    }

    public void insert(int element) {
        elems = Arrays.copyOf(elems, elems.length+1);
        elems[elems.length-1] = element;
        shiftUp(elems.length-1);
    }

    public int top() {
        return elems[0];
    }

    public int pop() {
        if (elems.length <= 0) {
            throw new IllegalStateException("zero elements");
        }

        int result = elems[0];
        elems = Arrays.copyOfRange(elems, 1, elems.length);
        shiftDown(0);
        return result;
    }

    public int[] elems() {
        return elems.clone();
    }

    private void shiftUp(int idx) {
        if (idx <= 0) return;

        int parentIdx = (idx-1)/2;
        if (elems[parentIdx] > elems[idx]) {
            swap(parentIdx, idx);
            shiftUp(parentIdx);
        }
    }

    private void shiftDown(int idx) {
        int childIdx = idx * 2 + 1;

        if (childIdx  >= elems.length)
            return;

        if (childIdx + 1 < elems.length && elems[childIdx + 1] < elems[childIdx]) {
            childIdx += 1;
        }

        if (elems[childIdx] < elems[idx]) {
            swap(idx, childIdx);
            shiftDown(childIdx);
        }
    }

    private void swap(int idx1, int idx2) {
        int tmp = elems[idx1];
        elems[idx1] = elems[idx2];
        elems[idx2] = tmp;
    }
}
