#!/bin/bash

# Execute the auction script inside of a Docker container

AUCTION_CONFIG_FILE_PATH=/auction/config.json
AUCTION_INPUT_FILE_PATH=/auction/input.json
AUCTION_RESULT_FILE_PATH=/auction/output.json


python /src/main.py $AUCTION_CONFIG_FILE_PATH $AUCTION_INPUT_FILE_PATH $AUCTION_RESULT_FILE_PATH
