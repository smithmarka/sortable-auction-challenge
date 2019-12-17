from marshmallow import fields
from marshmallow import post_load
from marshmallow import Schema

from model.common import must_not_be_blank


class Bid:
	def __init__(self, bidder, unit, bid):
		self.bidder = bidder
		self.unit = unit
		self.bid = bid

	def __repr__(self):
		return '<Bid(bidder={self.bidder!r})>'.format(self=self)


class BidSchema(Schema):
	bidder = fields.Str(validate=must_not_be_blank)
	unit = fields.Str(validate=must_not_be_blank)
	bid = fields.Decimal(validate=must_not_be_blank)

	@post_load
	def make_obj(self, data, **kwargs):
		return Bid(**data)
