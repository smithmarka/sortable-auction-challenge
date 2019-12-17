#!/bin/bash

AUCTION_FOLDER_PATH=$PWD/test_data/original/

SRC_FOLDER_PATH=$PWD/src/

docker run -i -v $AUCTION_FOLDER_PATH:/auction/ -v $SRC_FOLDER_PATH:/src/ challenge
