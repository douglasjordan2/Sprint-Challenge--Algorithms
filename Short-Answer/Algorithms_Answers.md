#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^2)


b) O(log n)


c) O(n)

## Exercise II

Because floors are ordered lowest to highest (essentially a sorted list), I believe the best way to go about this is with a binary search. You'd throw an egg off the middle floor of the building. If it breaks, then it'll break on all floors above the middle one, so we can eliminate all those floors. If it doesn't break, then it won't break on all the floors below the middle floor, so we can eliminate those.

For the sake of argument, let's say it breaks when thrown from the middle floor. Now, we eliminate the top half of floors and are left with just the bottom half of the floors. Now, we throw the egg from the floor that's halfway between the bottom and middle floors. Same concept here, if it breaks we eliminate the floors above it, if it doesn't then we eliminate the floors below. We can repeat this process of throwing the egg off the middle floor of our continuously halved list of floors, eliminating floors above if the egg breaks or eliminating floors below if the egg does not break. Eventually we'll reach just a single floor, where if the egg is broken when thrown from this floor, then we've reached f. If it doesn't break, then the floor right above it is f. (f is the first floor at which the egg will break)

The runtime complexity of this binary operation is O(log n)