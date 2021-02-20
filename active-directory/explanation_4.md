## Overview

For this problem decided not to use complicated algorithms with indexing.
Implemented simple data search with a recursion. Overall datastructure
looks like m-ary tree. My implementation goes throughout all root's subdirectories
until the end or until he will find a data he is looking for, no magic.

Time complexity: **T(n) = T(n/k) + O(1)**  
Space complexity: **T(n) = T(n/k) + O(1)**