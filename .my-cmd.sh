#! /bin/bash

CMDIR=""
PROJECT_ROOT=""

function create(){
	echo '> Current path: ' $(pwd)
	export PROJECT_DIR=$1
		
	mkdir -p ${PROJECT_ROOT}/${PROJECT_DIR}
	cd ${PROJECT_ROOT}/${PROJECT_DIR}	
	echo '> New path: ' $(pwd)
	git init
	echo '> New repository: ' $PROJECT_DIR
	touch README.md
	git add README.md
	git commit -m "initial"

	echo -n '> Enter remote url: '
	read REMOTE_URL
	
	git remote add origin $REMOTE_URL
	git push -u origin main

	echo '> Repository created: ' ${PROJECT_ROOT}/${PROJECT_DIR}
	echo $(code .)
}

function create-github(){
     echo '> Current path: ' $(pwd)
     export PROJECT_DIR=$1

     mkdir -p ${PROJECT_ROOT}/${PROJECT_DIR}
     cd ${PROJECT_ROOT}/${PROJECT_DIR}
     echo '> New path: ' $(pwd)
     
     REMOTE_URL=`python3 ${CMDIR}/create.py | tail -1`
     if [ -n "$REMOTE_URL" ] && [ ${#REMOTE_URL} -gt 0 ]; then
         echo '> New repository: ' $PROJECT_DIR
         touch README.md
         git init
         git add README.md
         git commit -m "initial"
         git remote add origin $REMOTE_URL
         git push -u origin main
         echo '> Repository created: ' ${PROJECT_ROOT}/${PROJECT_DIR}
         echo $(code .)
     else
         echo "[!] Create Github repository failed" 1>&2
     fi
 }