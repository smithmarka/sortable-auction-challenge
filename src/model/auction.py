from marshmallow import fields
from marshmallow import post_load
from marshmallow import Schema

from model.common import must_not_be_blank
from model.bid import BidSchema


class Auction:
	def __init__(self, site, units, bids):
		self.site = site
		self.units = units
		self.bids = bids

	def __repr__(self):
		return '<Auction(site={self.site!r})>'.format(self=self)


class AuctionSchema(Schema):
	site = fields.Str(validate=must_not_be_blank)
	units = fields.List(fields.String, validate=must_not_be_blank)
	bids = fields.List(fields.Nested(BidSchema))

	@post_load
	def make_obj(self, data, **kwargs):
		return Auction(**data)
