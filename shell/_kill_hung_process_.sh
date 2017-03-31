#!/bin/bash

user=`whoami`
project='test-project'

# ps command truncates the username if the length is greater than 8
if [ ${#user} -gt 8 ]; then
  environment="${user:0:7}+"
else
  environment=$user
fi

for process_id in  "$(ps -ef | grep $environment | grep $project | awk '{print $2}')"; do
  echo "Killing process $process_id"
  kill -9 $process_id
done
