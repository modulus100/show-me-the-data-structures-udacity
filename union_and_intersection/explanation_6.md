## Overview

LinkedList was given as a base data structure which works fine for
solving such problems, simple list also could be used. To 
solve **union** and **intersection** I found sets useful in order
to keep track on which values have been already added and which not. It helps
me to avoid copies. Any data structure which keeps order of values
could be applied, this algorithm does not mutate inputs.

Time complexity: **O(n + m)**  
Space complexity: **O(n + m)**  
Where **n** is a fist list size and **m** is a second list size.