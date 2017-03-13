package javaish.algos.search;

public class BinarySearch {
    public static int search(final int lookFor, final int[] in) {
        int left = 0;
        int right = in.length-1;

        while (left <= right) {
            int midIndex = (left + right) / 2;
            int midValue = in[midIndex];
            if (lookFor < midValue) {
                right = midIndex - 1;
            } else if (lookFor > midValue) {
                left = midIndex + 1;
            } else {
                return midIndex;
            }
        }

        return -1;
    }
}
