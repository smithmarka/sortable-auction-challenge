from marshmallow import fields
from marshmallow import post_load
from marshmallow import Schema

from model.common import must_not_be_blank


class Site:
	def __init__(self, name, bidders, floor):
		self.name = name
		self.bidders = bidders
		self.floor = floor

	def __repr__(self):
		return '<Site(name={self.name!r})>'.format(self=self)


class SiteSchema(Schema):
	name = fields.Str(validate=must_not_be_blank)
	bidders = fields.List(fields.String, validate=must_not_be_blank)
	floor = fields.Decimal(validate=must_not_be_blank)

	@post_load
	def make_obj(self, data, **kwargs):
		return Site(**data)
