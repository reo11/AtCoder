#!/bin/bash

for i in {0..100}; do
    filename=$(printf "%04d.txt" $i)
    rm out/$filename
    cat in/$filename | python after_contest.py >> out/$filename
done