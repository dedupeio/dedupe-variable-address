from __future__ import print_function

from parseratorvariable import ParseratorType
import usaddress

STREET = (('address number',   ('AddressNumberPrefix',
                                'AddressNumber',
                                'AddressNumberSuffix')),
          ('street direction', ('StreetNamePreDirectional',
                                'StreetNamePostDirectional')),
          ('street name',      ('StreetNamePreModifier',
                                'StreetName',
                                'StreetNamePostModifier')),
          ('street type',      ('StreetNamePostType',
                                'StreetNamePreType')),
          ('occupancy type',   ('OccupancyType',)),
          ('occupancy id',     ('OccupancyIdentifier',)),
          ('building name',    ('BuildingName',)))

BOX =  (('box group type', ('USPSBoxGroupType',)),
        ('box group id',   ('USPSBoxGroupID',)),
        ('box type',       ('USPSBoxType',)),
        ('box id',         ('USPSBoxID',)))

INTERSECTION_A = (('street direction A', ('StreetNamePreDirectional',
                                          'StreetNamePostDirectional')),
                  ('street name A',      ('StreetNamePreModifier',
                                          'StreetName',
                                          'StreetNamePostModifier')),
                  ('street type A',      ('StreetNamePostType',
                                          'StreetNamePreType')))
INTERSECTION_B = (('street direction B', ('SecondStreetNamePreDirectional',
                                          'SecondStreetNamePostDirectional')),
                  ('street name B',      ('SecondStreetNamePreModifier',
                                          'SecondStreetName',
                                          'SecondStreetNamePostModifier')),
                  ('street type B',      ('SecondStreetNamePostType',
                                          'SecondStreetNamePreType')))


class USAddressType(ParseratorType) :
    type = "Address"
    
    def tagger(self, field) :
        return usaddress.tag(field)

    def __init__(self, definition) :
        self.components = (('Street Address', self.compareFields, STREET),
                           ('PO Box', self.compareFields, BOX),
                           ('Intersection', self.comparePermutable, 
                            INTERSECTION_A, INTERSECTION_B))

        super(USAddressType, self).__init__(definition)

