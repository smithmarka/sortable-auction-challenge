import json

from model.site import SiteSchema
from model.bidder import BidderSchema
from model.auction import AuctionSchema
from model.bid import BidSchema


def load_dict_from_json_text(file_path):
	"""
	Summary:
		Read text file at file_path into a dictionary object

	Args:
		file_path (str): input file to read
	"""

	loaded_json = None
	with open(file_path, 'r') as f:
		loaded_json = json.load(f)

	return loaded_json


# # This function was removed in favor of loading via file_path
# def read_input_config_from_stdin():
# 	import fileinput

# 	file_text = None
# 	for line in fileinput.input():
# 		if file_text is None:
# 			file_text = line
# 		else:
# 			file_text += line

# 	return file_text


def load_sites_from_config_dict(config_dict):
	"""
	Summary:
		Load site data from a config dict into Site model objects

	Args:
		config_dict (dict): dictionary containing configuration data
	"""
	sites_json = config_dict['sites']

	site_schema = SiteSchema(many=True)
	result = site_schema.load(sites_json)
	
	return result


def load_auctions_from_dict(auction_data_json):
	"""
	Summary:
		Load auctions data from a config dict into Auction model objects

	Args:
		auction_data_json (dict): dictionary containing auction configuration data
	"""
	auction_schema = AuctionSchema(many=True)
	result = auction_schema.load(auction_data_json)
	return result


def load_bidders_from_config_dict(config_dict):
	"""
	Summary:
		Load bidder data from config dict into Bidder model objects

	Args:
		config_dict (dict): dictionary containing configuration data
	"""
	bidders_json = config_dict['bidders']
	bidder_schema = BidderSchema(many=True)
	result = bidder_schema.load(bidders_json)
	return result


def preprocess_auctions_result(auctions_result):
	"""
	Summary:
		Pre-process the auctions result to make dumping the results to text file a little easier.

	Args:
		auctions_result (list): list containing the auction results
	"""
	bid_schema = BidSchema()
	processed_result = []
	for site_auction in auctions_result:
		site_result = []
		for winning_bid in site_auction:
			if winning_bid is None:
				site_result.append([])
				continue
			dumped_winning_bid = bid_schema.dump(winning_bid)
			dumped_winning_bid['bid'] = float(dumped_winning_bid['bid'])
			site_result.append(dumped_winning_bid)

		processed_result.append(site_result)	

	return processed_result


def output_auctions_result(auctions_result, output_file_path):
	"""
	Summary:
		Output the auctions result file

	Args:
		auctions_result (list): list containing the auction results
		output_file_path (str): output file to write results
	"""
	
	processed_auctions_result = preprocess_auctions_result(auctions_result)
	json_auctions_result = json.dumps(processed_auctions_result, indent=4)
	
	with open(output_file_path, 'w+') as f:
		f.write(json_auctions_result)