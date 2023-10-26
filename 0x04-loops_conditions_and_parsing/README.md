# 0x04. Loops, conditions and parsing

## General
   - How to create SSH keys
   - What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
   - How to use `while`, `until` and `for` loops
   - How to use `if`, `else`, `elif` and `case` condition statements
   - How to use the `cut` command
   - What are files and other comparison operators, and how to use them

### Tasks: ###

1. **Task 0: SSH RSA key pair.** `0-RSA_public_key.pub`
   - SSH and RSA keys will be covered in depth in a later project.

2. **Task 1: For loop.** `1-for_best_school`
   - Bash script that displays `Best School` 10 times:
     - using `for` loop.

3. **Task 2: While loop.** `2-while_best_school`
   - Bash script that displays Best School 10 times:
     - using `while` loop.

4. **Task 3: Until loop.** `3-until_best_school`
   - Bash script that displays Best School 10 times.
     - using `until` loop.

5. **Task 4: If statement.** `4-if_9_say_hi`
   - Bash script that displays Best School 10 times, but for the 9th iteration, displays Best School and then Hi on a new line.
     - using `while` loop and `if` statement.

6. **Task 5: If, elif, else.:** `5-4_bad_luck_8_is_your_chance`
   - Bash script that loops from 1 to 10 and:
     - displays `bad luck` for the 4th loop iteration
     - displays `good luck` for the 8th loop iteration
     - displays `Best School` for the other iterations
     - using `while` loop and `if`, `elif`, `else` statements

7. **Task 6: Case statement.** `6-superstitious_numbers`
   - Bash script that displays numbers from 1 to 20 and:
     - displays `4` and then `bad luck from China` for the 4th loop iteration
     - displays `9` and then `bad luck from Japan` for the 9th loop iteration
     - displays `17` and then `bad luck from Italy` for the 17th loop iteration

8. **Task 7: Clock.** `7-clock`
   - Bash script that displays the time for 12 hours and 59 minutes:
     - display hours from 0 to 12
     - display minutes from 1 to 59

9. **Task 8: Ls.** `8-for_ls`
   - Bash script that displays:
     - The content of the current directory
     - In a list format
     - Where only the part of the name after the first dash is displayed

10. **Task 9: To file, or not to file.** `9-to_file_or_not_to_file`
    - Bash script that gives you information about the school file.
    ```bash
    user@linux$ file school
    school: cannot open `school' (No such file or directory)
    user@linux$ ./9-to_file_or_not_to_file
    school file does not exist
    user@linux$ touch school
    user@linux$ ./9-to_file_or_not_to_file
    school file exists
    school file is empty
    school is a regular file
    user@linux$ echo 'Dakhamat' > school
    user@linux$ ./9-to_file_or_not_to_file
    school file exists
    school file is not empty
    school is a regular file
    user@linux$ 
    ```

11. **Task 10: FizzBuzz.** `10-fizzbuzz`
    - Bash script that displays numbers from 1 to 100.
      - Displays `FizzBuzz` when the number is a multiple of 3 and 5
      - Displays `Fizz` when the number is multiple of 3
      - Displays `Buzz` when the number is a multiple of 5
      - Otherwise, displays the number
      - In a list format

12. **Task 11: Read and cut.** `100-read_and_cut`
    - Bash script that displays the content of the file /etc/passwd.

