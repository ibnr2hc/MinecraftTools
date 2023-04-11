#!/bin/sh
cd /home/ec2-user/minecraft

NOW=`date "+%Y%m%d"`
zip ${NOW}.zip -r world world_nether world_the_end/
aws s3 cp ${NOW}.zip s3://ojo.minecraft.backup/world/
rm -f ${NOW}.zip
