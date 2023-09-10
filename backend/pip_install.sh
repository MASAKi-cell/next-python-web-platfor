#!/bin/bash

# パッケージインストール時にrequirements.txtを自動更新する
pip install "$@"
pip freeze > requirements.txt 