import argparse

from auction_runner import run_auctions

from data_loader import load_auctions_from_dict
from data_loader import load_bidders_from_config_dict
from data_loader import load_dict_from_json_text
from data_loader import load_sites_from_config_dict
from data_loader import output_auctions_result


def main():
	"""
	Summary:
		Main entry point into the application
	"""

	# Parse the application arguments 
	parser = argparse.ArgumentParser(description='Process a challenge auction.')
	parser.add_argument("auction_config_file_path", help="Path to auction configuration file.", type=str)
	parser.add_argument("auction_input_file_path", help="Path to auction input file.", type=str)
	parser.add_argument("output_file_path", help="Path to auction result output file.", type=str)
	args = parser.parse_args()

	config_file_path = args.auction_config_file_path
	auction_input_path = args.auction_input_file_path
	output_file_path = args.output_file_path

	# Load auction configuration from provided config file
	config_dict = load_dict_from_json_text(config_file_path)
	bidder_list = load_bidders_from_config_dict(config_dict)
	site_list = load_sites_from_config_dict(config_dict)

	# Loading from stdin was causing issues under particular scenarios so the decision
	# was made to read the auction input data from a file path
	# input_config_text = read_input_config_from_stdin()
	# auction_list = load_auctions(input_config_text)

	# Load auction_input from file_path
	auction_dict = load_dict_from_json_text(auction_input_path)
	auction_list = load_auctions_from_dict(auction_dict)

	# Run the auctions to find the winning bids
	auctions_result = run_auctions(auction_list, bidder_list, site_list)
	
	# Output the results to the provided file path
	output_auctions_result(auctions_result, output_file_path)


if __name__ == '__main__':
	main()
