# 2D Array - DS
<p>Given a 6 x 6 2D array, <em>arr</em>:</p>
~~~~
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
~~~~
<p>We define an hourlgass in A to be a subset of values with indices falling in this pattern in <em>arr</em>'s graphical representation:</p>
~~~~
a b c
  d  
e f g
~~~~
<p>There are 16 hourgalsses in <em>arr</em>, and an hourglass sum is the sum of an hourglass' values. Calculate the hourgalss sum for every hourgalss in <em>arr</em>, then print the maximum hourglass sum.</p>
<p>For example, given the 2D array:</p>
~~~~
-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
~~~~
<p>We calculate the following 16 hourglass values:</p>
~~~~
-63, -34,  -9,  12,
-10,   0,  28,  23,
-27, -11,  -2,  10,
  9,  17,  25,  18
~~~~
<p>Our highest hourglass value is 28 from the hourglass:</p>
~~~~
0 4 3
  1  
8 6 6
~~~~

# Note:
If you have already solved the Java doomain's Java 2D Array challenge, you may wish to skip this challenge

# Function Description
<p>Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.</p>
<p>hourglassSum has the following parameter(s):</p>
<ul>
<li>arr: an array of integers</li>
</ul>

# Input Format
<p>Each of the 6 lines of inputs <em>arr[i]</em> contains 6 space-separated integers <em>arr[i][j]</em>.</p>

# Constraints
<ul>
<li>-9 ≤ <em>arr[i][j] ≤ 9</em></li>
<li>0 ≤ <em>i, j</em> ≤ 5</li>
</ul>

# Output Format
<p>Print the largest (maximum) hourglass sum found in <em>arr</em></p>

# Sample Input
~~~~
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
~~~~

# Sample Output
~~~~
19
~~~~

# Explanation
<p><em>arr</em>'s maximum sum hourglass is:</p>
~~~~
2 4 4
  2  
1 2 4
~~~~
<p>With a sum of 19.
