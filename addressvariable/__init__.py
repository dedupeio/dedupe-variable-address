import usaddress
from parseratorvariable import ParseratorType

STREET = (
    ("address number", ("AddressNumberPrefix", "AddressNumber", "AddressNumberSuffix")),
    ("street direction", ("StreetNamePreDirectional", "StreetNamePostDirectional")),
    ("street name", ("StreetNamePreModifier", "StreetName", "StreetNamePostModifier")),
    ("street type", ("StreetNamePostType", "StreetNamePreType")),
    ("occupancy type", ("OccupancyType",)),
    ("occupancy id", ("OccupancyIdentifier",)),
    ("building name", ("BuildingName",)),
)

BOX = (("box group id", ("USPSBoxGroupID",)), ("box id", ("USPSBoxID",)))

INTERSECTION_A = (
    ("street direction A", ("StreetNamePreDirectional", "StreetNamePostDirectional")),
    (
        "street name A",
        ("StreetNamePreModifier", "StreetName", "StreetNamePostModifier"),
    ),
    ("street type A", ("StreetNamePostType", "StreetNamePreType")),
)
INTERSECTION_B = (
    (
        "street direction B",
        ("SecondStreetNamePreDirectional", "SecondStreetNamePostDirectional"),
    ),
    (
        "street name B",
        (
            "SecondStreetNamePreModifier",
            "SecondStreetName",
            "SecondStreetNamePostModifier",
        ),
    ),
    ("street type B", ("SecondStreetNamePostType", "SecondStreetNamePreType")),
)


class USAddress(ParseratorType):
    type = "Address"

    def tagger(self, field):
        return self.tag(field)

    def __init__(self, field, **kwargs):
        self.components = (
            ("Street Address", self.compareFields, STREET),
            ("PO Box", self.compareFields, BOX),
            ("Intersection", self.comparePermutable, INTERSECTION_A, INTERSECTION_B),
        )

        block_parts = ("StreetName",)
        super().__init__(field, usaddress.tag, block_parts, **kwargs)
