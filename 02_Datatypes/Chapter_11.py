import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple
chaiprofile = namedtuple("chaiprofile", ["flavor", "aroma", ])