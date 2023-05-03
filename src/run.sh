#!/bin/bash
for venv_dir in ./*venv*/; do
  if [ -d "$venv_dir" ]; then
    echo "Activating virtual environment in $venv_dir"
    source "$venv_dir/bin/activate"
  fi
done
pip3 install -r requirements.txt
clear
python3 main.py