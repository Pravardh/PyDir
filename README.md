PyDir is a program written in python that can be used to bruteforce websites to scan for directories. The goal is to add multithreading and concurrency to speed up the process by a lot.

Here all the things I would like to add to this particular project.

This uses multiprocessing so it should be a lot faster than other directory bruteforcing tools.
How to use:-

python PyDir.py -s

It asks for the url automatically!
Enter the url, and scan away! 

use flag -q to print out only successful requests
use flag -S to SYN flood (DOS attack) a website/address

To Do:-
1. Concurrency -- done
2. Multithreading -- done
3. GUI mode
4. Error handling
5. DoS attacks -- done
6. Curl commands on websites
7. Web crawler
8. Compile to C
