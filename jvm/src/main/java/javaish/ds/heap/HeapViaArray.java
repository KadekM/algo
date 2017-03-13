package javaish.ds.heap;

public class HeapViaArray {
    private int elems[];

    public HeapViaArray() {
        elems = new int[0];
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

    public int[] elems() {
        return elems.clone();
    }

    private void heapify(int idx) {
        int leftIdx = idx * 2;
        int rightIdx = idx * 2 + 1;

        if (leftIdx < elems.length && elems[leftIdx] > elems[idx]) {
            swap(idx, leftIdx);
            heapify(leftIdx);
        }
        else if (rightIdx < elems.length && elems[rightIdx] > elems[idx]) {
            swap(idx, rightIdx);
            heapify(rightIdx);
        }
    }

    private void swap(int idx1, int idx2) {
        int tmp = elems[idx1];
        elems[idx1] = elems[idx2];
        elems[idx2] = tmp;
    }
}
