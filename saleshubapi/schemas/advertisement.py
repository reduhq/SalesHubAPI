from marshmallow import Schema, fields, validate

class AdvertisementBase(Schema):
    title = fields.String(
        required = False,
        allow_none = False,
        validate = validate.Length(
            min=1,
            max=70,
            error="The title must be at least 70 characters"
        )
    )
    description = fields.String()
    establishment = fields.Bool()
    price = fields.Float(
        required=False,
        allow_none=False,
        validate=validate.Range(
            min=0.0,
            max=9999.0
        )
    )
    
class AdvertisementSchema(AdvertisementBase):
    date = fields.Date()
    
class AdvertisementCreateSchema(AdvertisementBase):
    title = fields.String(
        required = True,
        allow_none = False,
        validate = validate.Length(
            min=1,
            max=70,
            error="The title must be at least 70 characters"
        )
    )
    description = fields.String(required=True, allow_none=False)
    establishment = fields.Bool(required=True, allow_none=False)
    price = fields.Float(
        required=True,
        allow_none=False,
        validate=validate.Range(
            min=0.0,
            max=9999.0
        )
    )
    
class AdvertisementUpdateSchema(AdvertisementBase):
    date = fields.Date()