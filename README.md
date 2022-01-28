# git-pull-checker

* The `main.py` pulls the repository specified in `GIT_DIR` and saves the updated files' names in `diff.txt`.
* After saving the file, the next part of the code reads the file and checks whether is contains any `js/css` files.
* On processing the file, it determines which build link to fire.
