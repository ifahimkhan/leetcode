### 953	Verifying an Alien Dictionary	51.8%	Easy  
Sorting/comparator is transitive. A < B and B < C => A < C. Thus, to verify the sorted order, we only need to test adjacent pairs and see if we can find viation.   
Varient of the problem. Given order and list of strings, sort according to order.  

### 1249 Minimum Remove to Make Valid Parentheses	64.2%	Medium	
Linear scan, any ) close nothing are extra, any trailing ( can't be closed thus are extra as well. 
Either use a set to remember the loc of each above. Or use a stack and push anything that we don't need to remove onto it.  
Follow up: if string is mutable? like linked list? then short links.  

### 1428	Leftmost Column with at Least a One 49.4%	Medium	
Start from top right, walk down the stairs until either hit left wall or landed on the groud.

### 973	K Closest Points to Origin	64.6%	Medium	
Max Priority Queue(NLogK) to find K smallest or quickselect(C*O(N). 

### 680	Valid Palindrome II	37.1%	Easy	
Two pointers. If not the same, try both deletion option and see if any succeed. 

### 560	Subarray Sum Equals K	43.7%	Medium	 
Accumulating sum and annotate {Prefix sum: count(arr[:i] have prefix sum)}. Add prefix_sum[accum -k] to total and increament prefix sum. 
Init prefix_sum with 0: 1

### 1570	Dot Product of Two Sparse Vectors 91.2%	Medium	
Map non-zero index to value.  
If conserned about hashset access not truly constant and not worried about adding new element, use list of (index, value) and two pointers.  

### 415	Add Strings	48.4%	Easy	
School math, pad shorter one with 0. And just add number one by one. 
Follow up - with decimals. Split add each concat?

### 238	 Product of Array Except Self	61.4%	Medium	
prod[i] = pi(x) except xi can be decomposed to accum prod from left * accum prod from right. 
Thus do two pass accum prod. 

### 67 Add Binary	47.3%	Easy	
Similar to 415, school math. 


# 124	Binary Tree Maximum Path Sum	35.6%	Hard	

# 273	Integer to English Words	28.3%	Hard	

# 211	Design Add and Search Words Data Structure	40.5%	Medium	

# 269	Alien Dictionary 33.8%	Hard	

# 426	Convert Binary Search Tree to Sorted Doubly Linked List
61.6%	Medium	
199	
Binary Tree Right Side View	56.5%	Medium	
938	
Range Sum of BST	83.2%	Easy	
636	
Exclusive Time of Functions	55.0%	Medium	
56	
Merge Intervals	41.4%	Medium	
528	
Random Pick with Weight	44.7%	Medium	
125	
Valid Palindrome	38.5%	Easy	
158	
Read N Characters Given Read4 II - Call multiple times
37.4%	Hard	
301	
Remove Invalid Parentheses	44.8%	Hard	
987	
Vertical Order Traversal of a Binary Tree	39.0%	Hard	
721	
Accounts Merge	52.2%	Medium	
215	
Kth Largest Element in an Array	58.9%	Medium	
65	
Valid Number	16.0%	Hard	
278	
First Bad Version	37.8%	Easy	
986	
Interval List Intersections	68.5%	Medium	
173	
Binary Search Tree Iterator	60.6%	Medium	
29	
Divide Two Integers	16.9%	Medium	
523	
Continuous Subarray Sum	24.8%	Medium	
297	
Serialize and Deserialize Binary Tree	50.2%	Hard	
621	
Task Scheduler	52.2%	Medium	
827	
Making A Large Island	47.3%	Hard	
50	
Pow(x, n)	31.0%	Medium	
270	
Closest Binary Search Tree Value
50.3%	Easy	
1539	
Kth Missing Positive Number	54.9%	Easy	
236	
Lowest Common Ancestor of a Binary Tree	49.3%	Medium	
398	
Random Pick Index	58.3%	Medium	
543	
Diameter of Binary Tree	49.4%	Easy	
31	
Next Permutation	33.9%	Medium	
339	
Nested List Weight Sum
76.8%	Medium	
340	
Longest Substring with At Most K Distinct Characters
45.7%	Medium	
1650	
Lowest Common Ancestor of a Binary Tree III
76.7%	Medium	
140	
Word Break II	35.3%	Hard	
42	
Trapping Rain Water	51.6%	Hard	
249	
Group Shifted Strings
58.5%	Medium	
88	
Merge Sorted Array	40.9%	Easy	
708	
Insert into a Sorted Circular Linked List
32.7%	Medium	
1762	
Buildings With an Ocean View
80.9%	Medium	
317	
Shortest Distance from All Buildings
42.9%	Hard	
489	
Robot Room Cleaner
72.9%	Hard	
76	
Minimum Window Substring	36.2%	Hard	
139	
Word Break	41.9%	Medium	
133	
Clone Graph	39.8%	Medium	
282	
Expression Add Operators	36.9%	Hard	
34	
Find First and Last Position of Element in Sorted Array	37.5%	Medium	
10	
Regular Expression Matching	27.4%	Hard	
863	
All Nodes Distance K in Binary Tree	58.2%	Medium	
658	
Find K Closest Elements	42.2%	Medium	
1382	
Balance a Binary Search Tree	76.1%	Medium	
266	
Palindrome Permutation
62.7%	Easy	
203	
Remove Linked List Elements	39.5%	Easy	
958	
Check Completeness of a Binary Tree	52.5%	Medium	
670	
Maximum Swap	45.3%	Medium	
138	
Copy List with Random Pointer	41.4%	Medium	
785	
Is Graph Bipartite?	48.7%	Medium	
146	
LRU Cache	36.2%	Medium	
71	
Simplify Path	34.9%	Medium	
1004	
Max Consecutive Ones III	60.8%	Medium	
825	
Friends Of Appropriate Ages	44.3%	Medium	
1209	
Remove All Adjacent Duplicates in String II	57.8%	Medium	
23	
Merge k Sorted Lists	43.0%	Hard	
977	
Squares of a Sorted Array	71.8%	Easy	
157	
Read N Characters Given Read4
37.7%	Easy	
43	
Multiply Strings	35.1%	Medium	
314	
Binary Tree Vertical Order Traversal
47.3%	Medium	
1053	
Previous Permutation With One Swap	51.2%	Medium	
1047	
Remove All Adjacent Duplicates In String	71.2%	Easy	
8	
String to Integer (atoi)	15.7%	Medium	
329	
Longest Increasing Path in a Matrix	45.4%	Hard	
498	
Diagonal Traverse	50.5%	Medium	
438	
Find All Anagrams in a String	45.2%	Medium	
1233	
Remove Sub-Folders from the Filesystem	62.4%	Medium	
163	
Missing Ranges
27.3%	Easy	
247	
Strobogrammatic Number II
48.8%	Medium	
896	
Monotonic Array	57.9%	Easy	
341	
Flatten Nested List Iterator	54.8%	Medium	
333	
Largest BST Subtree
38.3%	Medium	
536	
Construct Binary Tree from String
52.1%	Medium	
689	
Maximum Sum of 3 Non-Overlapping Subarrays	47.3%	Hard	
347	
Top K Frequent Elements	62.6%	Medium	
33	
Search in Rotated Sorted Array	36.1%	Medium	
1216	
Valid Palindrome III
50.0%	Hard	
691	
Stickers to Spell Word	45.1%	Hard	
283	
Move Zeroes	58.7%	Easy	
1060	
Missing Element in Sorted Array
54.8%	Medium	
616	
Add Bold Tag in String
44.9%	Medium	
515	
Find Largest Value in Each Tree Row	62.4%	Medium	
525	
Contiguous Array	43.6%	Medium	
295	
Find Median from Data Stream	47.4%	Hard	
1757	
Recyclable and Low Fat Products
95.7%	Easy	
752	
Open the Lock	53.0%	Medium	
921	
Minimum Add to Make Parentheses Valid	74.9%	Medium	
1361	
Validate Binary Tree Nodes	43.4%	Medium	
311	
Sparse Matrix Multiplication
64.1%	Medium	
378	
Kth Smallest Element in a Sorted Matrix	56.4%	Medium	
380	
Insert Delete GetRandom O(1)	49.1%	Medium	
304	
Range Sum Query 2D - Immutable	41.1%	Medium	
78	
Subsets	65.6%	Medium	
1213	
Intersection of Three Sorted Arrays
79.4%	Easy	
739	
Daily Temperatures	64.8%	Medium	
127	
Word Ladder	32.1%	Hard	
695	
Max Area of Island	65.1%	Medium	
39	
Combination Sum	59.7%	Medium	
1120	
Maximum Average Subtree
63.9%	Medium	
791	
Custom Sort String	65.9%	Medium	
162	
Find Peak Element	44.1%	Medium	
1439	
Find the Kth Smallest Sum of a Matrix With Sorted Rows	60.2%	Hard	
148	
Sort List	46.6%	Medium	
875	
Koko Eating Bananas	53.5%	Medium	
246	
Strobogrammatic Number
46.4%	Easy	
19	
Remove Nth Node From End of List	35.9%	Medium	
463	
Island Perimeter	66.8%	Easy	
227	
Basic Calculator II	38.8%	Medium	
548	
Split Array with Equal Sum
48.3%	Medium	
253	
Meeting Rooms II
47.1%	Medium	
939	
Minimum Area Rectangle	52.2%	Medium	
1498	
Number of Subsequences That Satisfy the Given Sum Condition	38.8%	Medium	
381	
Insert Delete GetRandom O(1) - Duplicates allowed	35.0%	Hard	
114	
Flatten Binary Tree to Linked List	52.4%	Medium	
983	
Minimum Cost For Tickets	62.8%	Medium	
286	
Walls and Gates
56.9%	Medium	
449	
Serialize and Deserialize BST	54.3%	Medium	
724	
Find Pivot Index	46.0%	Easy	
666	
Path Sum IV
56.7%	Medium	
348	
Design Tic-Tac-Toe
55.7%	Medium	
1197	
Minimum Knight Moves
37.4%	Medium	
224	
Basic Calculator	38.3%	Hard	
839	
Similar String Groups	41.6%	Hard	
3	
Longest Substring Without Repeating Characters	31.5%	Medium	
1026	
Maximum Difference Between Node and Ancestor	69.7%	Medium	
844	
Backspace String Compare	47.2%	Easy	
200	
Number of Islands	49.5%	Medium	
416	
Partition Equal Subset Sum	45.0%	Medium	
605	
Can Place Flowers	31.7%	Easy	
678	
Valid Parenthesis String	31.7%	Medium	
787	
Cheapest Flights Within K Stops	39.6%	Medium	
98	
Validate Binary Search Tree	28.9%	Medium	
1329	
Sort the Matrix Diagonally	81.7%	Medium	
766	
Toeplitz Matrix	65.9%	Easy	
772	
Basic Calculator III
44.0%	Hard	
393	
UTF-8 Validation	38.1%	Medium	
15	
3Sum	28.3%	Medium	
742	
Closest Leaf in a Binary Tree
44.6%	Medium	
349	
Intersection of Two Arrays	65.3%	Easy	
647	
Palindromic Substrings	62.7%	Medium	
51	
N-Queens	50.2%	Hard	
388	
Longest Absolute File Path	43.1%	Medium	
153	
Find Minimum in Rotated Sorted Array	46.3%	Medium	
323	
Number of Connected Components in an Undirected Graph
58.2%	Medium	
20	
Valid Parentheses	40.0%	Easy	
1091	
Shortest Path in Binary Matrix	40.2%	Medium	
529	
Minesweeper	61.5%	Medium	
734	
Sentence Similarity
42.4%	Easy	
1032	
Stream of Characters	48.6%	Hard	
14	
Longest Common Prefix	36.2%	Easy	
79	
Word Search	37.1%	Medium	
824	
Goat Latin	66.9%	Easy	
408	
Valid Word Abbreviation
31.5%	Easy	
480	
Sliding Window Median	38.9%	Hard	
540	
Single Element in a Sorted Array	57.9%	Medium	
419	
Battleships in a Board	71.2%	Medium	
1522	
Diameter of N-Ary Tree
69.4%	Medium	
794	
Valid Tic-Tac-Toe State	33.9%	Medium	
1110	
Delete Nodes And Return Forest	67.9%	Medium	
445	
Add Two Numbers II	56.5%	Medium	
865	
Smallest Subtree with all the Deepest Nodes	65.0%	Medium	
109	
Convert Sorted List to Binary Search Tree	50.6%	Medium	
468	
Validate IP Address	25.1%	Medium	
694	
Number of Distinct Islands
58.1%	Medium	
219	
Contains Duplicate II	38.8%	Easy	
974	
Subarray Sums Divisible by K	51.0%	Medium	
435	
Non-overlapping Intervals	43.8%	Medium	
1614	
Maximum Nesting Depth of the Parentheses	82.7%	Easy	
1102	
Path With Maximum Minimum Value
50.8%	Medium	
46	
Permutations	67.1%	Medium	
1275	
Find Winner on a Tic Tac Toe Game	52.8%	Easy	
778	
Swim in Rising Water	54.8%	Hard	
1297	
Maximum Number of Occurrences of a Substring	50.6%	Medium	
637	
Average of Levels in Binary Tree	66.1%	Easy	
1305	
All Elements in Two Binary Search Trees	77.8%	Medium	
121	
Best Time to Buy and Sell Stock	51.8%	Easy	
230	
Kth Smallest Element in a BST	62.9%	Medium	
38	
Count and Say	46.3%	Medium	
92	
Reverse Linked List II	40.8%	Medium	
741	
Cherry Pickup	35.2%	Hard	
252	
Meeting Rooms
55.5%	Easy	
442	
Find All Duplicates in an Array	69.1%	Medium	
307	
Range Sum Query - Mutable	36.9%	Medium	
102	
Binary Tree Level Order Traversal	57.0%	Medium	
567	
Permutation in String	44.5%	Medium	
41	
First Missing Positive	33.9%	Hard	
405	
Convert a Number to Hexadecimal	44.5%	Easy	
345	
Reverse Vowels of a String	45.2%	Easy	
277	
Find the Celebrity
44.0%	Medium	
332	
Reconstruct Itinerary	38.1%	Medium	
692	
Top K Frequent Words	53.2%	Medium	
773	
Sliding Puzzle	61.2%	Hard	
395	
Longest Substring with At Least K Repeating Characters	43.6%	Medium	
91	
Decode Ways	26.9%	Medium	
228	
Summary Ranges	42.7%	Easy	
116	
Populating Next Right Pointers in Each Node	49.6%	Medium	
2	
Add Two Numbers	35.7%	Medium	
1094	
Car Pooling	59.7%	Medium	
443	
String Compression	44.1%	Medium	
1038	
Binary Search Tree to Greater Sum Tree	82.5%	Medium	
387	
First Unique Character in a String	53.9%	Easy	
207	
Course Schedule	44.3%	Medium	
993	
Cousins in Binary Tree	52.3%	Easy	
73	
Set Matrix Zeroes	44.6%	Medium	
126	
Word Ladder II	23.8%	Hard	
113	
Path Sum II	49.5%	Medium	
1123	
Lowest Common Ancestor of Deepest Leaves	68.0%	Medium	
325	
Maximum Size Subarray Sum Equals k
47.5%	Medium	
1644	
Lowest Common Ancestor of a Binary Tree II
56.2%	Medium	
257	
Binary Tree Paths	54.0%	Easy	
22	
Generate Parentheses	65.7%	Medium	
206	
Reverse Linked List	65.7%	Easy	
727	
Minimum Window Subsequence
42.4%	Hard	
1287	
Element Appearing More Than 25% In Sorted Array	60.2%	Easy	
946	
Validate Stack Sequences	64.4%	Medium	
336	
Palindrome Pairs	34.8%	Hard	
54	
Spiral Matrix	36.5%	Medium	
129	
Sum Root to Leaf Numbers	51.3%	Medium	
234	
Palindrome Linked List	41.9%	Easy	
235	
Lowest Common Ancestor of a Binary Search Tree	52.1%	Easy	
17	
Letter Combinations of a Phone Number	49.5%	Medium	
767	
Reorganize String	50.3%	Medium	
161	
One Edit Distance
33.2%	Medium	
75	
Sort Colors	49.8%	Medium	
1027	
Longest Arithmetic Subsequence	49.7%	Medium	
74	
Search a 2D Matrix	38.1%	Medium	
62	
Unique Paths	56.3%	Medium	
260	
Single Number III	65.4%	Medium	
452	
Minimum Number of Arrows to Burst Balloons	49.8%	Medium	
367	
Valid Perfect Square	42.2%	Easy	
716	
Max Stack
43.1%	Easy	
66	
Plus One	42.2%	Easy	
720	
Longest Word in Dictionary	49.4%	Easy	
159	
Longest Substring with At Most Two Distinct Characters
50.7%	Medium	
239	
Sliding Window Maximum	44.8%	Hard	
310	
Minimum Height Trees	34.8%	Medium	
143	
Reorder List	41.0%	Medium	
406	
Queue Reconstruction by Height	68.6%	Medium	
77	
Combinations	57.9%	Medium	
1	
Two Sum	46.7%	Easy	
494	
Target Sum	45.6%	Medium	
545	
Boundary of Binary Tree
40.3%	Medium	
166	
Fraction to Recurring Decimal	22.4%	Medium	
105	
Construct Binary Tree from Preorder and Inorder Traversal	52.4%	Medium	
4	
Median of Two Sorted Arrays	31.4%	Hard	
989	
Add to Array-Form of Integer	45.0%	Easy	
220	
Contains Duplicate III	21.4%	Medium	
268	
Missing Number	55.2%	Easy	
63	
Unique Paths II	35.4%	Medium	
622	
Design Circular Queue	47.7%	Medium	
103	
Binary Tree Zigzag Level Order Traversal	50.4%	Medium	
25	
Reverse Nodes in k-Group	45.3%	Hard	
242	
Valid Anagram	58.9%	Easy	
47	
Permutations II	49.8%	Medium	
698	
Partition to K Equal Sum Subsets	45.8%	Medium	
112	
Path Sum	42.6%	Easy	
128	
Longest Consecutive Sequence	46.5%	Hard	
414	
Third Maximum Number	30.7%	Easy	
399	
Evaluate Division	54.6%	Medium	
209	
Minimum Size Subarray Sum	39.8%	Medium	
328	
Odd Even Linked List	57.2%	Medium	
430	
Flatten a Multilevel Doubly Linked List	57.0%	Medium	
226	
Invert Binary Tree	67.3%	Easy	
48	
Rotate Image	60.5%	Medium	
168	
Excel Sheet Column Title	31.9%	Easy	
300	
Longest Increasing Subsequence	44.5%	Medium	
37	
Sudoku Solver	47.0%	Hard	
503	
Next Greater Element II	58.7%	Medium	
86	
Partition List	43.7%	Medium	
160	
Intersection of Two Linked Lists	44.5%	Easy	
371	
Sum of Two Integers	50.6%	Medium	
16	
3Sum Closest	46.3%	Medium	
36	
Valid Sudoku	50.8%	Medium	
703	
Kth Largest Element in a Stream	50.9%	Easy	
64	
Minimum Path Sum	56.5%	Medium	
451	
Sort Characters By Frequency	64.6%	Medium	
28	
Implement strStr()	35.3%	Easy	
303	
Range Sum Query - Immutable	48.2%	Easy	
111	
Minimum Depth of Binary Tree	39.8%	Easy	
5	
Longest Palindromic Substring	30.6%	Medium	
44	
Wildcard Matching	25.5%	Hard	
152	
Maximum Product Subarray	32.9%	Medium	
232	
Implement Queue using Stacks	52.7%	Easy	
11	
Container With Most Water	52.9%	Medium	
212	
Word Search II	37.4%	Hard	
350	
Intersection of Two Arrays II	52.1%	Easy	
7	
Reverse Integer	25.9%	Easy	
240	
Search a 2D Matrix II	45.3%	Medium	
208	
Implement Trie (Prefix Tree)	52.5%	Medium	
617	
Merge Two Binary Trees	75.5%	Easy	
57	
Insert Interval	35.3%	Medium	
547	
Number of Provinces	60.7%	Medium	
21	
Merge Two Sorted Lists	56.4%	Easy	
572	
Subtree of Another Tree	44.6%	Easy	
94	
Binary Tree Inorder Traversal	66.3%	Medium	
704	
Binary Search	54.3%	Easy	
136	
Single Number	66.7%	Easy	
210	
Course Schedule II	42.9%	Medium	
24	
Swap Nodes in Pairs	53.5%	Medium	
509	
Fibonacci Number	67.5%	Easy	
108	
Convert Sorted Array to Binary Search Tree	60.9%	Easy	
55	
Jump Game	35.2%	Medium	
53	
Maximum Subarray	47.9%	Easy	
26	
Remove Duplicates from Sorted Array	46.8%	Easy	
49	
Group Anagrams	59.7%	Medium	
122	
Best Time to Buy and Sell Stock II	58.8%	Easy	
141	
Linked List Cycle	43.1%	Easy	
13	
Roman to Integer	57.0%	Easy	
32	
Longest Valid Parentheses	29.9%	Hard	
9	
Palindrome Number	50.0%	Easy	
322	
Coin Change	37.7%	Medium	
