# In this README you will find what each script is doing.

1. 0-iam_betty
   - Shell script to switches the current user to the user betty.

2. 1-who_am_i
   - Shell script that prints the effective username of the current user.

3. 2-groups
   - Shell script that prints all the groups the current user is part of.

4. 3-new_owner
  - Shell script that change the owner of the file hello to the user betty.

5. 4-empty
   - Shell script that creates an empty file with name ***hello***.

6. 5-execute
   - Shell script that adds execute permission to the owner of the file hello.

7. 6-multiple_permissions
   - Shell script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

8. 7-everybody
   - Shell script that adds execution permission to the owner, the group owner and the other users, to the file hello.

9. 8-James_Bond
   - Shell script that sets the permission to the file hello with
     - Owner: no permission at all
     - Group: no permission at all
     - Other users: all the permissions

10. 9-John_Doe
    - Shell script that sets the mode of the file hello to this:
      - `-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello`

11. 10-mirror_permissions
    - Shell script that sets the mode of the file **hello** the same as **olleh's** mode.

12. 11-directories_permissions
    - Shell script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

13. 12-directory_permissions
    - Shell script that creates a dir called ***my_dir*** with permission 751 in current working directory.

14. 13-change_group
    - Shell script that changes the group owner to **school** for the file **hello**.

15. 100-change_owner_and_group
    - Shell script that changes the owner to **vincent** and the group owner to **staff** for all the files and dirs in the working dir.

16. 101-symbolic_link_permissions
    - Shell script that changes the owner and the group owner of **_hello** to **vincent** and **staff** respectively.

17. 102-if_only
    - Shell script that changes the owner of the file **hello** to **bety** only if it is owned by the user **guillaume**.

18. 103-Star_Wars
    - Shell script to play **Star Wars IV** episode in the terminal.
