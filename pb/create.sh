#!/bin/env bash

SRC_DIR=./
DST_DIR=./gen

lang_list="cpp java python"
for lang in $lang_list
do
    echo " Creating proto source files for $lang"
    mkdir -p "$DST_DIR/$lang"
    protoc -I=$SRC_DIR --${lang}_out=$DST_DIR/$lang $SRC_DIR/*.proto
done

