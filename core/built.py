__author__ = 'BackOffice-3'


import builtwith


website = builtwith.parse("itechlabs.com.au")
print(website)
for key, value in website.items():
    print(key + ":", ", ".join(value))
