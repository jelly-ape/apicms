# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from model.festival import BaseFestival
from model.access import Access
from model.mix_date import MixDate


date = MixDate(7, 18, True)
f1 = BaseFestival('6夕节', '6夕情人节', date)
print f1.name
print f1.description
print f1.solar_date
print f1.lunar_date
print f1.is_today()

date = MixDate(6, 6, False)
f2 = BaseFestival('七夕节', '七夕情人节', date)
print f2.name
print f2.description
print f2.solar_date
print f2.lunar_date
print f2.is_today()

print
print "access"
a = Access(1, 3)
print a.owner_read
print a.owner_write
print a.other_read
print a.other_write
