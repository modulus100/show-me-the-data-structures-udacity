## Overview

Solution is based on https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU, 
I already used this solution for leetcode. LRU cache can be implemented using a hashmap
and doubly linked list. Hashmap as a key uses a key from LRU's **get/set** methods and
as a value it uses a reference to the node from doubly linked list.
Doubly linked list keeps nodes with value and works as a queue with limited capacity.

Time complexity:  **O(1)**, no iterations.  
Space complexity: **O(n)**, internal cache got to store **n** nodes max.