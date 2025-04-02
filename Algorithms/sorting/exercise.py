#Which sorting algorithm you should use in each occasion?

#1. Sort 10 schools around your house by distance. 
Insertion sort! Really good with small datasets.

#2. eBay sorts listing by the current bid amount.
Radix sort! Integers in a fixed range.

#3. Sport scores in ESPN
Quick sort! As they can be float values, and considering memory complexity + time complexity

#4. Massive Database (can't fit all in memory), need to sort last year user data.
Merge sort! We don't have to worry about memory complexity as we would need to merge in a external place. 
We also don't want the worst case to take so much time as the input is large.

#5. Almost sorted Udemy reviews. Need to add 2 reviews.
Insertion sort! Considering it is almost sorted, we choose the best cases time complexity.

#6. Temperature records for the past 50 years in Canada.
Quick sort! As the input is not big, and considering as float values. If it was only integer, radix or counting.

#7. Large username database needs to be sorted. The data is very random.
Quick sort! Considering we don't have to be aware of memory and not considering the worst cases. Otherwise Timsort or Merge.

#8. You want to teach sorting for the first time.
Bubble sort! The easiest to understand and be familiar with the core concepts of sorting.
