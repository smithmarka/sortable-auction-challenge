from marshmallow import ValidationError


# Custom validator
def must_not_be_blank(data):
	if data is None:
		raise ValidationError("Data not provided.")
