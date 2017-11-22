#!/usr/bin/env bash

# author : zergl <e3.gemini@qq.com>
#   date : 2017/11/23
#   desc : build all modules

declare -A map=()

function do_build_module()
{
	if [ $# -ne 1 ];then
		return
	fi

	bin_dir="$1"
	bin_name=`basename $bin_dir`
	echo ""
	echo "[BEGIN]-------------------------"
	echo "bin_dir: $bin_dir -- $bin_name"
	cd "$bin_dir"
	
	prom="[BUILD] $bin_dir -- "
	rm -rf CMakeFiles CMakeCache.txt && cmake . && make

	if [ $? -eq 0 ];then
		map["'$bin_name'"]="SUCC"
		prom2="${prom}SUCC."
	else
		map["$bin_name"]="FAIL"
		prom2="${prom}FAIL."
	fi

	echo ""
	echo -e "\033[31m $prom2 \033[0m"
	echo "[END]-------------------------"
}

function do_main()
{
	base_dir=$(cd "$(dirname "$0")"; pwd)
	svr_dir="${base_dir}/src"
	echo "src_dir: $svr_dir"

	do_build_module "$svr_dir/base"
	if [ $? -eq 0 ];then
		map['base'] = "SUCC"
	fi

	for d in `ls "$svr_dir"`
	do
		if [ "$d" == "base" ];then
			continue
		fi

		do_build_module "$svr_dir/$d"
	done

	echo ""
	echo "---------------------"
	for key in ${!map[@]}
	do
		echo "   BUILD $key : ${map[$key]}"
	done
}

do_main $?

