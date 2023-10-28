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

