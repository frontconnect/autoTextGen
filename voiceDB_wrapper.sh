#!/bin/bash

# check the input arguments
set -e # errror gördüğünde dur
set -x # çalıştırdığı her şeyi ekrana yaz

if [ $# -ne 1 ]
then 
	echo "Usage: <pack number>"
	exit 1
fi
PACK_NO="$1"
#prepare the hash mails
./hash-mails.sh "mails-inp${PACK_NO}" "mails-out${PACK_NO}"

#assign the texts
./assign-texts.sh "mails-out${PACK_NO}" "users${PACK_NO}.csv" 5 "mails-fin${PACK_NO}"

# prepare the hash mails
./prepare-attachments.sh "users${PACK_NO}.csv" "mails-fin${PACK_NO}" "mails-zip${PACK_NO}"
