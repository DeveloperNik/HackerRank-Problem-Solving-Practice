# 2D Array - DS
<p>Given a 6 x 6 2D array, <em>arr</em>:</p>
<p><code>1 1 1 0 0 0</code></p>
<p><code>0 1 0 0 0 0</code></p>
<p><code>1 1 1 0 0 0</code></p>
<p><code>0 0 0 0 0 0</code></p>
<p><code>0 0 0 0 0 0</code></p>
<p><code>0 0 0 0 0 0</code></p>
<p>We define an hourlgass in A to be a subset of values with indices falling in this pattern in <em>arr</em>'s graphical representation:</p>
<p><code>a b c</code></p>
<p><code>  d  </code></p>
<p><code>e f g</code></p>
<p>There are 16 hourgalsses in <em>arr</em>, and an hourglass sum is the sum of an hourglass' values. Calculate the hourgalss sum for every hourgalss in <em>arr</em>, then print the maximum hourglass sum.</p>
<p>For example, given the 2D array:</p>
<p><code>-9 -9 -9  1 1 1</code></p>
<p><code> 0 -9  0  4 3 2</code></p>
<p><code>-9 -9 -9  1 2 3</code></p>
<p><code> 0  0  8  6 6 0</code></p>
<p><code> 0  0  0 -2 0 0</code></p>
<p><code> 0  0  1  2 4 0</code></p>
<p>We calculate the following 16 hourglass values:</p>
<p><code>-63, -34,  -9,  12,</code></p>
<p><code>-10,   0,  28,  23,</code></p>
<p><code>-27, -11,  -2,  10,</code></p>
<p><code>  9,  17,  25,  18</code></p>
<p>Our highest hourglass value is 28 from the hourglass:</p>
<p><code>0 4 3</code></p>
<p><code>  1  </code></p>
<p><code>8 6 6</code></p>

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
<p><code>1 1 1 0 0 0</code></p>
<p><code>0 1 0 0 0 0</code></p>
<p><code>1 1 1 0 0 0</code></p>
<p><code>0 0 2 4 4 0</code></p>
<p><code>0 0 0 2 0 0</code></p>
<p><code>0 0 1 2 4 0</code></p>

# Sample Output
<code>19</code>

# Explanation
<p><em>arr</em>'s maximum sum hourglass is:</p>
<p><code>2 4 4</code></p>
<p><code>  2  </code></p>
<p><code>1 2 4</code></p>
<p>With a sum of 19.
  
  
# Test
<code>
2 4 4<br/>  2  <br/>1 2 4
</code>
