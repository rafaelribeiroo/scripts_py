#!/bin/bash
echo 'Deploy GitHub'
git add .
echo 'Digite o commit abaixo: '
read commit
git commit -m ''$commit''
git push