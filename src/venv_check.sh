#!/bin/bash
if [ -d *venv* ]; then
  echo "venv environment exists"
else
  echo "venv environment does not exist, please run 'python3 -m venv main-venv' to create it"
fi