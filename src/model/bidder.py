from marshmallow import fields
from marshmallow import post_load
from marshmallow import Schema
from model.common import must_not_be_blank


class Bidder:
	def __init__(self, name, adjustment):
		self.name = name
		self.adjustment = adjustment

	def __repr__(self):
		return '<Bidder(name={self.name!r})>'.format(self=self)


class BidderSchema(Schema):
	name = fields.Str(validate=must_not_be_blank)
	adjustment = fields.Decimal(validate=must_not_be_blank)
	# created_at = fields.DateTime()

	@post_load
	def make_obj(self, data, **kwargs):
		return Bidder(**data)
