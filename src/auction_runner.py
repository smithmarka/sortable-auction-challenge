def run_auctions(auction_list, bidder_list, site_list):
	"""
	Summary:
		Main entry point into auction running logic. Determines the result of each individual 
		auction and returns the result list

	Args:
		auction_list (list): list of Auction model objects
		bidder_list (list): list of Bidder model objects
		site_list (list): list of Site model objects
	"""

	auctions_results = []

	# For each Auction provided in input.json
	for auction in auction_list:
		# Validate the auction site exists in the provided configuration
		site = find_site(site_list, auction.site)

		if site is None:
			auctions_results.append([])
			continue

		# Run the individual site auction
		site_auction_result = run_site_auction(site, auction, bidder_list)

		auctions_results.append(site_auction_result)

	return auctions_results


def run_site_auction(site, auction, bidder_list):
	"""
	Summary:
		Run a single site auction and return the results

	Args:
		site (Site): object containing site data
		auction (Auction): object containing auction data
		bidder_list (list): list of Bidder model objects
	"""
	
	site_auction_result = []

	# Validate at least one bid exists for an auction
	if len(auction.bids) < 1:
		print('INFO - No bids for site: {}'.format(site.name))
		return site_auction_result

	# Get valid bidder list
	site_bidder_list = get_bidders_by_name_list(site.bidders, bidder_list)

	# Validate at least one valid bidder exists for this site
	if len(site_bidder_list) < 1:
		print('INFO - No valid bidders for site: {}'.format(site.name))
		return site_auction_result

	# For each unit in the auction determine the winning bid, if any
	for unit in auction.units:
		# Get all bids for this specific unit
		bids_by_unit_list = list(filter(lambda x: x.unit == unit, auction.bids))

		# Validate
		if len(bids_by_unit_list) < 1:
			print('INFO - No bids for site: {}, unit: {}'.format(site.name, unit))
			site_auction_result.append(None)
			continue

		# Run the unit auction to determine the highest bidder and append to result
		highest_bid = run_unit_auction(site.floor, bids_by_unit_list, site_bidder_list)
		site_auction_result.append(highest_bid)

	return site_auction_result


def run_unit_auction(site_floor, bids, bidder_list):
	"""
	Summary:
		Run a single unit auction by iterating through a list of bids and determining
		the highest valid bid

	Args:
		site_floor (decimal): minimum required bid to win the auction
		bids (list): list of Bid model objects
		bidder_list (list): list of Bidder model objects
	"""
	current_highest_bid = None
	highest_adjusted_bid = None

	for bid in bids:

		# Validate that the bidder is configured correctly in the system
		bidder = find_bidder(bidder_list, bid.bidder)
		if bidder is None:
			continue

		# Calculate the adjusted bid
		bidder_adjustment_multiplier = 1 + bidder.adjustment
		adjusted_bid = bid.bid * bidder_adjustment_multiplier

		# Adjusted bid below the minimum accepted floor.
		if adjusted_bid < site_floor:
			print('INFO - {} did not meet site floor {} with bid {}'.format(bid.bidder, site_floor, bid.bid))
			continue

		# Set the adjusted bid on the Bid object
		bid.adjusted_bid = adjusted_bid

		# Set current highest bid if appropriate
		if current_highest_bid is None or adjusted_bid > current_highest_bid.adjusted_bid:
			current_highest_bid = bid
			highest_adjusted_bid = adjusted_bid
			print('INFO - {} has current highest bid: {} ({} adjusted)'.format(bid.bidder, bid.bid, adjusted_bid))

	return current_highest_bid


def get_bidders_by_name_list(name_list, bidder_list):
	"""
	Summary:
		Helper function to find get the list of valid bidders for a site

	Args:
		name_list (list): list of bidder names
		bidder_list (list): list of Bidder model objects
	"""

	filtered_list = list(filter(lambda x: x.name in name_list, bidder_list))

	return filtered_list


def find_site(site_list, site_name):
	"""
	Summary:
		Helper function to find a Site by name in the site_list and validate that only one configured site exists

	Args:
		site_list (list): list of Site model objects
		site_name (str): name of the Site to find
	"""

	filtered_site_list = list(filter(lambda x: x.name == site_name, site_list))

	# Validate that the site exists
	if len(filtered_site_list) < 1:
		print('ERROR - Invalid config - Unable to find configured Site: {}'.format(site_name))
		return None

	if len(filtered_site_list) > 1:
		print('ERROR - Invalid config - Too many configured Sites: {}'.format(site_name))
		return None

	return filtered_site_list[0]


def find_bidder(bidder_list, bidder_name):
	"""
	Summary:
		Helper function to find a Bidder by name in the bidder_list

	Args:
		bidder_list (list): list of Bidder model objects
		bidder_name (str): name of the Bidder to find
	"""

	filtered_list = list(filter(lambda x: x.name == bidder_name, bidder_list))

	# Validate that the bidder exists
	if len(filtered_list) < 1:
		print('ERROR - Invalid config - Unable to find configured Bidder: {}'.format(bidder_name))
		return None

	return filtered_list[0]
