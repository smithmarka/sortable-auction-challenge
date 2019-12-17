# Auction Coding Challenge

Submitted: Mark Smith, 2019-12-16

This challenge was completed using Python 3. Instructions are provided below for running both inside of a Python virtual 
env as well as inside of a Docker container. Bash scripts to build and run the container were created for developer
convenience and included in submission.

A number of test scenarios were configured in the test_data folder and were used to test the validity of the submission.
These tests are far from complete but should cover the main scenarios and fail cases. 

## Assumptions
1) Input data will be well formed
2) Winning bids are still valid when output as a decimal (i.e. 35.0 instead of 35)
3) Reading input.json from stdin was not strictly necessary. It appeared that using argparse was interfering with
input from stdin. This did not appear to be related to any core logic so for ease of development this data is loaded 
the same way as config.json.  

## Running the auctions


### Without Docker

Create Python Virtual Env and install requirements
```bash
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

Run pre-configured test auction data
```bash
$ ./run_tests.sh
```

Application usage help 
```bash
$ python ./src/main.py
usage: main.py [-h]                                                                                                                                                                                                                                 
               auction_config_file_path auction_input_file_path                                                                                                                                                                                     
               output_file_path
main.py: error: the following arguments are required: auction_config_file_path, auction_input_file_path, output_file_path

```

### With Docker (Manual)

Example docker build and execution

```bash
$ docker build -t challenge .
$ docker run -i -v /path/to/auction/config/:/auction/ -v /path/to/source/:/src/ challenge
```
or
```bash 
docker run -i -v $PWD/test_data/original/:/auction/ -v $PWD/src/:/src/ challenge
```

### With Docker (Bash Scripts)

Example docker build and execution. Do not forget to update $AUCTION_FOLDER_PATH in docker_run.sh

```bash
$ ./docker_build.sh
$ ./docker_run.sh
```
