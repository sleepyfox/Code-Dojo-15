# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *
import csv

if __name__ == "__main__":
    print ("OMGHAI!")
    items = []
    with open("items.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(Item(row['Name'], int(row['sellIn']), int(row['quality'])))

    days = 1
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()

