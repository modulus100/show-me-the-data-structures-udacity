## Overview
The root directory may have n directories where
each directory may also have n subdirectories. In order to find all specific
files in a root and subdirectories I decided to use a simple recursion.
.  Algorithm goes through all root's subdirectories and saves file name to a list.

Time complexity: **T(n) = T(n/k) + O(1)**  
Space complexity: **T(n) = T(n/k) + O(1)**