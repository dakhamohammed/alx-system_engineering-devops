# 0x05. Processes and signals

## General
  - What is a PID
  - What is a process
  - How to find a process’ PID
  - How to kill a process
  - What is a signal
  - What are the 2 signals that cannot be ignored

# Tasks:

1. **Task 0: What is my PID.** `0-what-is-my-pid`
   - Bash script that displays its own PID.

2. **Task 1: List your processes.** `1-list_your_processes`
   - Bash script that displays a list of currently running processes.

3. **Task 2: Show your Bash PID.** `2-show_your_bash_pid`
   - Bash script that displays lines containing the `bash` word.

4. **Task 3: Show your Bash PID made easy.** `3-show_your_bash_pid_made_easy`
   - Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

5. **Task 4: To infinity and beyond.** `4-to_infinity_and_beyond`
   - Bash script that displays `To infinity and beyond` indefinitely.

6. **Task 5: Don't stop me now!.** `5-dont_stop_me_now`
   - Bash script that stops `4-to_infinity_and_beyond` process.
     - using `kill` command.

7. **Task 6: Stop me if you can.** `6-stop_me_if_you_can`
   - Bash script that stops `4-to_infinity_and_beyond` process.
     - usind `pkill` command.

8. **Task 7: Highlander.** `7-highlander` and `67-stop_me_if_you_can`
   - Bash script that displays:
     - `To infinity and beyond` indefinitely
     - With a `sleep 2` in between each iteration
     - `I am invincible!!!` when receiving a `SIGTERM` signal

9. **Task 8: Beheaded process.** `8-beheaded_process`
   - Bash script that kills the process `7-highlander`.
   - Terminal #0   
   ```bash
   dakhamat@ubuntu20.04$ ./7-highlander
   To infinity and beyond
   To infinity and beyond
   To infinity and beyond
   To infinity and beyond
   Killed
   dakhamat@ubuntu20.04$ 
   ```
   - Terminal #1
   ```bash
   dakhamat@ubuntu20.04$ ./8-beheaded_process
   dakhamat@ubuntu20.04$ 
   ```
   - I started `7-highlander` in Terminal #0 and then run `8-beheaded_process` in terminal #1 and we can see that the `7-highlander` has been killed.

10. **Task 9: Process and PID file.** `100-process_and_pid_file`
    - Bash script that:
      - Creates the file /var/run/myscript.pid containing its PID
      - Displays `To infinity and beyond` indefinitely
      - Displays `I hate the kill command` when receiving a SIGTERM signal
      - Displays `Y U no love me?!` when receiving a SIGINT signal
      - Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

11. **Task 10: Manage my process.** `101-manage_my_process`, `manage_my_process`
    - `manage_my_process` Bash script that:
      - Indefinitely writes `I am alive!` to the file `/tmp/my_process`
      - In between every `I am alive!` message, the program should pause for 2 seconds
    - Bash (init) script `101-manage_my_process` that manages `manage_my_process`
      - When passing the argument `start`:
        - Starts `manage_my_process`
        - Creates a file containing its PID in `/var/run/my_process.pid`
        - Displays `manage_my_process started`
      - When passing the argument `stop`:
        - Stops `manage_my_process`
        - Deletes the file `/var/run/my_process.pid`
        - Displays `manage_my_process stopped`
      - When passing the argument `restart`:
        - Stops `manage_my_process`
        - Deletes the file `/var/run/my_process.pid`
        - Starts `manage_my_process`
        - Creates a file containing its PID in `/var/run/my_process.pid`
        - Displays `manage_my_process restarted`
    - Displays `Usage: manage_my_process {start|stop|restart}` if any other argument or no argument is passed

