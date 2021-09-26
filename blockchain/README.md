## Overview
This solution represents a complex linked list implementation where a connection
between block(node) is a hashcode not a reference to a node.  

Time complexity **O(n)**, this is an approximate complexity since this code uses
external library methods which must be optimised, for example sha256, serialize,
encode.  
Space complexity **O(n)**, just a number of blocks in a chain.