#!/bin/env bash

SRC_DIR=./
DST_DIR=./gen
PROTO_DIR=../server/src/base/pb/protocol

lang_list="cpp java python"
for lang in $lang_list
do
    echo " Creating proto source files for $lang"
    mkdir -p "$DST_DIR/$lang"
    protoc -I=$SRC_DIR --${lang}_out=$DST_DIR/$lang $SRC_DIR/*.proto
done

rm -rf $PROTO_DIR
mkdir -p $PROTO_DIR
cp -r $DST_DIR/* $PROTO_DIR

