#!/bin/sh
awk 'BEGIN{largest=0;sum=0}{ if(NF){sum=sum+$1}else{ if(sum>largest){largest=sum} sum=0 }} END{ print largest }' input.txt
