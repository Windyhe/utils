#!/bin/bash
 
RUNDIR=`dirname $0`
PIDFILE="${RUNDIR}/$0.pid"
 
if [ -s ${PIDFILE} ]; then
  echo "脚本已经在运行，不重复运行，退出."
  exit 1
fi
echo $$ > ${PIDFILE}
 
# <各种业务处理逻辑>
 
cat /dev/null > ${PIDFILE}
