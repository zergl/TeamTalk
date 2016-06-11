#!/usr/bin/env bash

# author : zergl <e3.gemini@qq.com>
#   date : 2016/06/11
#   desc : boot all modules

function is_running()
{
	if [ $# -ne 1 ];then
		echo "0"
		return
	fi

	proc_name="$1"
	ps -fe|grep "./$proc_name" |grep -v grep  > /dev/null
	if [ $? -ne 0 ]; then
		echo "0"
		return
	fi

	echo "1"
	return
}

function do_start()
{
	if [ $# -ne 1 ];then
		return
	fi

	bin_dir="$1"
	bin_name=`basename $bin_dir`
	echo "bin_dir: $bin_dir -- $bin_name"
	cd "$bin_dir"
	./"$bin_name" &
}

function do_main()
{
	source ~/tools/favorite_env.sh

	base_dir=$(cd "$(dirname "$0")"; pwd)
	svr_dir="${base_dir}/src"
	echo "base_dir: $svr_dir"

	for d in `ls "$svr_dir"`
	do
		if [ "$d" == "base" ];then
			continue
		fi

		ret=$(is_running "$d");
		if [ $ret -eq 1 ]; then
			echo "$d is running..."
			continue
		fi

		do_start "$svr_dir/$d"
	done

	sleep 2

	echo "......"
	ps axu|grep -v grep |egrep "_server|msfs"
}

do_main $?

