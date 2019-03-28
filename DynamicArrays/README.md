# Dynamic Arrays

<ul>
<li>Create a list, <i>seqList</i>, of <i>N</i> empty sequences, where each sequence is indexed from 0 to <i>N</i> - 1. The elements within each of the <i>N</i> sequences also use 0-indexing.</li>
<li>Create an integer, <i>lastAnswer</i>, and initialize it to 0.</li>
<li>The 2 types of queries that can be performed on your list of sequences (<i>seqList</i>) are described below:</li>
<ol>
<li>Query: <code>1 x y</code></li>
<ol>
<li>Find the sequence, <i>seq</i>, at index ((<i>x</i> xor <i>lastAnswer</i>) % <i>N</i>) in <i>seqList</i></li>
<li>Append integer <i>y</i> to sequence <i>seq</i>.</li>
</ol>
<li>Query: <code>2 x y</code></li>
<ol>
<li>Find the sequence, <i>seq</i>, at index ((<i>x</i> xor <i>lastAnswer</i>) % <i>N</i>) in <i>seqList</i></li>
<li>Find the value of element <i>y</i> % <i>size</i>(where <i>size</i> is the size of <i>seq</i>) and assign it to <i>lastAnswer</i>.</li>
<li>Print the new value of <i>lastAnswer</i> on a new line.</li>
</ol>
</ol>
</ul>

# Task

<p>Given <i>N, Q</i>, and <i>Q</i> queries, execute each query.</p>
<p><strong>Note:</strong>XOR is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.</p>

# Input Format
<p>The first line contains two space-separated integers, <i>N</i> (the number of sequences) and <i>Q</i> (the number of queries), respectively</p>
<p>Each of the <i>Q</i> subsequent lines contains a query in the format defined above.</p>

# Constraints
<ul>
<li>1 ≤ <i>N, Q</i> ≤ 10^5</li>
<li>0 ≤ <i>x</i> ≤ 10^9</li>
<li>0 ≤ <i>y</i> ≤ 10^9</li>
<li>It is guaranteed that query type 2 will never query an empty sequence or index</li>
</ul>

# Output Format
<p>For each type 2 query, print the updated value of <i>lastAnswer</i> on a new line.</p>

# Sample Input

~~~~
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
~~~~

# Sample Output

~~~~
7
3
~~~~

# Explanation
<p>Initial Values:</p>
<p><i>lastAnswer</i> = 0</p>
<p><i>S0</i> = []</p>
<p><i>S1</i> = []</p>
<p>Query 0: Append 5 to sequence ((0 XOR 0) % 2) = 0.</p>
<p><i>lastAnswer</i> = 0</p>
<p><i>S0</i> = [5]</p>
<p><i>S1</i> = []</p>
<p>Query 1: Append 7 to sequence ((1 XOR 0) % 2) = 0</p>
<p><i>lastAnswer</i> = 0</p>
<p><i>S0</i> = [5]</p>
<p><i>S1</i> = [7]</p>
<p>Query 2: Append 3 to sequence ((0 XOR 0) % 2) = 0</p>
<p><i>lastAnswer</i> = 0</p>
<p><i>S0</i> = [5, 3]</p>
<p><i>S1</i> = [7]</p>
<p>Query 3: Assign the value at index 0 of sequence ((1 XOR 0) % 2) = 1 to <i>lastAnswer</i>, print <i>lastAnswer</i></p>
<p><i>lastAnswer</i> = 7</p>
<p><i>S0</i> = [5, 3]</p>
<p><i>S1</i> = [7]</p>

~~~~
7
~~~~

<p>Query 4: Assign the value at index 1 of sequence ((1 XOR 7) % 2) = 0 to <i>lastAnswer</i>, print <i>lastAnswer</i></p>
<p><i>lastAnswer</i> = 3</p>
<p><i>S0</i> = [5, 3]</p>
<p><i>S1</i> = [7]</p>

~~~~
3
~~~~