FOLDER=$1

jupytext --set-kernel python3 --output "$FOLDER/kernel/main.ipynb" "$FOLDER/main.py"