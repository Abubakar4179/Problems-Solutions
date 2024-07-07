# Solution 1 (using datetime module)
from datetime import datetime
date = "Oct 14 2005 7:15AM"
date_time = datetime.strptime(date, "%b %d %Y %I:%M%p")
print(date_time)

# Solution 2 (Using dateutil method)
from dateutil import parser
date_time = parser.parse("Oct 14 2005 7:15AM")
print(date_time)