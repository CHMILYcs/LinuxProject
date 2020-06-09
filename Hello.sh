#!/bin/bash
a=$(date +%T |awk -F: '{print $1}')
if [ $a -ge 00 ] && [ $a -le 05 ]
then
echo "注意身体，早点休息！"
elif [ $a -ge 05 ] && [ $a -le 08 ]
then
echo "早上好，奋发有为！"
elif [ $a -ge 08 ] && [ $a -le 10 ]
then
echo "上午好！愉快工作！"
elif [ $a -ge 10 ] && [ $a -le 12 ]
then
echo "中午好！记得吃午饭！"
elif [ $a -ge 12 ] && [ $a -le 17 ]
then
echo "下午好！！"
elif [ $a -ge 17 ] && [ $a -le 24 ]
then
echo "晚上好，早点休息！"
fi
