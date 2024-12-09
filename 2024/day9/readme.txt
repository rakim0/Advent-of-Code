    time       rank      points     time       rank      points
9   00:19:25   1880      0          00:48:18   1764      0

Just bruteforced it. 
part 1: O(n)
part 2: O(n^2)

I think for the second part it's better to maintain an list of dots with cnt and index and then checking accordingly
instead of scanning the whole line from start
but would need to somehow update the indicies after insertion of the leftover dots.
 