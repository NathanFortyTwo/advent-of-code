#/bin/bash

mkdir $1
cd $1 || exit

cp ../template.py ./step1.py
cp ../template.py ./step2.py
touch input.txt
exit 0;
