#! /bin/bash
function create(){
	echo 'Current path: ' $(pwd)
	export DIR=$1
	CMDIR="/Users/ariel/my_cmd"
	mkdir -p /home/Projects/${DIR}
	cd /home/Projects/${DIR}
	echo 'New path: ' $(pwd)
	git init
	remote_url=`python3 create.py | tail -1`
	
	echo 'In bash'
	echo $remote_url
	echo 'New repo: ' $DIR
	touch README.md
	git add README.md
	git commit -m "first commit"
	git branch -M main
	git remote add origin $remote_url
	git push -u origin main
	echo $(code .)
}
