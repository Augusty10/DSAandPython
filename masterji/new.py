class Solution {
  merge(arr1, m, arr2, n) {
    let i = m - 1;        // last valid element in arr1
    let j = n - 1;        // last element in arr2
    let k = m + n - 1;    // last position in arr1

    // Merge from the end
    while (i >= 0 && j >= 0) {
      if (arr1[i] > arr2[j]) {
        arr1[k] = arr1[i];
        i--;
      } else {
        arr1[k] = arr2[j];
        j--;
      }
      k--;
    }

    // If arr2 still has elements, copy them
    while (j >= 0) {
      arr1[k] = arr2[j];
      j--;
      k--;
    }
  }
}