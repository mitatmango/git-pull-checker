import os
import re

# Defining main function
def main() -> None:
    GIT_DIR = "~/GIT/MangoApps_RoR_Rails5"
    PULL_COMMAND = "git pull origin main"
    OUTPUT_FILE = f"{os.getcwd()}/diff.txt"

    os.system(
        f"cd {GIT_DIR} && {PULL_COMMAND} && git diff --name-status ORIG_HEAD.. > {OUTPUT_FILE}"
    )

    found_js_css_file = False
    file_empty = os.stat(OUTPUT_FILE).st_size == 0

    if not file_empty:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as diff:
            for line in diff:
                if re.search("(\\.css|\\.js)$", line.strip()):
                    found_js_css_file = True
                    break

        if found_js_css_file:
            print("Call Link 2")
        else:
            print("Call Link 1")
    else:
        print("Build is already up to date.")


if __name__ == "__main__":
    main()
