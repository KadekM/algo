package javaish.ds.heap;

public class HeapViaArray {
    private int elems[];

    public HeapViaArray(final int size) {
        elems = new int[size];
    }

    public void insert(int element) {
        int[] newElems = new int[elems.length + 1];
        newElems[0] = element;
        elems = newElems;
        heapify(0);
    }

    public int top() {
        return elems[0];
    }

    public int pop() {
        if (elems.length <= 0) {
            throw new IllegalStateException("zero elements");
        }

        return -1;
    }

    private void heapify(int idx) {
        if (idx >= elems.length) {
            return;
        }

        int left = idx * 2;
        int right = idx * 2 + 1;

        heapify(left);
        heapify(right);
    }

    private void swap(int idx1, int idx2) {
        int tmp = elems[idx1];
        elems[idx1] = elems[idx2];
        elems[idx2] = tmp;
    }
}
