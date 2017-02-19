import urllib2
from scrapy.selector import Selector

f = open('words', 'w')
for i in range(1264) :
  page = i+1
  print page
  href = 'http://www.nplg.gov.ge/gwdict/index.php?a=list&d=46&p=' + str(i)
  html = urllib2.urlopen(href).read()
  text = Selector(text=html).xpath('//dt[contains(@class, \'termpreview\')]/a/text()').extract()
  for word in text :
    f.write(word.encode('utf8'))
    f.write('\n')
f.close()

