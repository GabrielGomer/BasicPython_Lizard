# Named Tuples
# collections.namedtuple f()
# that produces subclass of tuple enhanced w/ fieldnames and a class name
from collections import namedtuple
from collections import OrderedDict
# Two parameters are required to create a named tuple: a class name and a list of field names
City = namedtuple('City', 'name abrev population coordinates')
# Data must be passed as positional arguments to the constructor
detroit = City('Detroit', 'DET', 673104, (42.2162, 83.3554))
print(detroit)
City(name='Detroit', abrev='DET', population=673104, coordinates=(42.2162, 83.3554))
# Access the fields by name or position
print(f'Detroit Data: \n'
      f'\tPopulation: {detroit.population}\n'
      f'\tCoordinates: {detroit.coordinates}\n'
      f'\tAbrev: {detroit[1]}\n')
# _fields is a tuple w/ the field names of the class
print(City._fields)
lat_long = namedtuple('lat_long', 'lat long')
delhi_data = ('Delphi NCR', 'IN', 21.935, lat_long(28.613889, 77.208889))
# _make() instantiate a named tuple from an iterable
delhi = City._make(delhi_data)
# _asdict() returns a collections.OrderDict built from the named tuple instance,
# nice display of city data
delhi._asdict()
OrderedDict([('name', 'Delphi NCR'), ('country', 'IN'), ('population', 21.935),
             ('coordinates', lat_long(lat=28.613889, long=77.208889))])
for key, value in delhi._asdict().items():
    print(key + ':', value)
# Tuples supports all list methods that do not involve adding or removing items


