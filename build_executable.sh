#!/bin/sh

pyinstaller main.py --onefile --clean --name=git_pull_and_sync 
rm -rf build
rm -rf __pycache__