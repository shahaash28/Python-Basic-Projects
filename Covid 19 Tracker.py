import covid

from covid import Covid

covid = Covid()

# by country name
india = covid.get_status_by_country_name("India")

for i,j in india.items():
    print("{} : {}".format(i, j))