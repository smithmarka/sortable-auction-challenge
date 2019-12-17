#!/bin/bash


execute_auction () {
    echo '----------------------------------------------------------------------------'
    echo Executing auction for: $1
    AUCTION_CONFIG_FILE_PATH=$1/config.json
    AUCTION_INPUT_FILE_PATH=$1/input.json
    AUCTION_RESULT_FILE_PATH=$1/output.json
    python src/main.py $AUCTION_CONFIG_FILE_PATH $AUCTION_INPUT_FILE_PATH $AUCTION_RESULT_FILE_PATH
    echo '----------------------------------------------------------------------------'
}

# Original test cases
BASE_FOLDER_PATH=./test_data/original
execute_auction $BASE_FOLDER_PATH

# Site names configured in input.json do not match config.json
BASE_FOLDER_PATH=./test_data/test_01
execute_auction $BASE_FOLDER_PATH

# No bids configured in input.json
BASE_FOLDER_PATH=./test_data/test_02
execute_auction $BASE_FOLDER_PATH

# No bidders for the site in config.json
BASE_FOLDER_PATH=./test_data/test_03
execute_auction $BASE_FOLDER_PATH

# No bidders configured in config.json
BASE_FOLDER_PATH=./test_data/test_04
execute_auction $BASE_FOLDER_PATH

# No units configured in input.json
BASE_FOLDER_PATH=./test_data/test_05
execute_auction $BASE_FOLDER_PATH

# No bids configured for auction unit (bids_by_unit_list)
BASE_FOLDER_PATH=./test_data/test_06
execute_auction $BASE_FOLDER_PATH

# No valid bidder for unit auction (run_unit_auction)
BASE_FOLDER_PATH=./test_data/test_07
execute_auction $BASE_FOLDER_PATH

# Adjusted bid below floor value (run_unit_auction)
BASE_FOLDER_PATH=./test_data/test_08
execute_auction $BASE_FOLDER_PATH

# Multiple bids from same bidder, going down
BASE_FOLDER_PATH=./test_data/test_09
execute_auction $BASE_FOLDER_PATH
