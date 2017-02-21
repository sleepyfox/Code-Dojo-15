# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             Stock_Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Stock_Item(name="Aged Brie", sell_in=2, quality=0),
             Stock_Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Legendary_Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Legendary_Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Stock_Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Stock_Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Stock_Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Stock_Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 2
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
