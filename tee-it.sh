#!/usr/bin/env bash
if [[ "$#" != "2" ]]; then
	echo "tee-it <out file> <cmd>"
	echo "Note that tee-t redirects stderr to stdout."
fi

out_file=$1
cmd=$2

unbuffer ${cmd} 2>&1 | tee ${out_file}
