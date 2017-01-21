#!/bin/bash

kill $(ps -ef | grep siyer | grep backfill | awk -F ' ' '{print $2}')
