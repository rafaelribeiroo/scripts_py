#!/bin/bash
green=`tput setaf 2`
yellow=`tput setaf 3`
white=`tput setaf 7`

if [ -n "$(git status --porcelain)" ]; then
	echo "${green}Há alterações que precisam ser 'deployadas'${yellow}"
	git status --porcelain
	git add -A .
	echo "${green}Acima, os arquivos que precisam ser upados para que possa descrever melhor o commit${white}"
	read -p "Descrição do commit: " desc  
	git commit -m "$desc"
	git push origin master
else
	echo "Não há alterações nesse repositório, vamos trabalhar!";
fi
