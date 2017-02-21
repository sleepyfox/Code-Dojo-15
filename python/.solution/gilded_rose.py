# -*- coding: utf-8 -*-

# Symbolic constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
TEN_DAYS = 10
FIVE_DAYS = 5
MAX_ITEM_QUALITY = 50
MIN_ITEM_QUALITY = 0
LEGENDARY_ITEM_QUALITY = 80

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.age_one_day()

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Stock_Item(Item):
    def out_of_date(self):
        return self.sell_in < 0

    def age_one_day(self):
        self.sell_in -= 1
        self.update_quality()

    def _improve_quality(self, amount):
        self.quality += amount
        if self.quality > MAX_ITEM_QUALITY:
            self.quality = MAX_ITEM_QUALITY

    def _reduce_quality(self, amount):
        self.quality -= amount
        if self.quality < MIN_ITEM_QUALITY:
            self.quality = MIN_ITEM_QUALITY

    def update_quality(self):
        if self.out_of_date():
            self._reduce_quality(2)
        else:
            self._reduce_quality(1)

class Legendary_Item(Stock_Item):
    def age_one_day(self):
        self.quality = LEGENDARY_ITEM_QUALITY

class Cheese_Item(Stock_Item):
    def update_quality(self):
        if self.out_of_date():
            self._improve_quality(2)
        else:
            self._improve_quality(1)

class Backstage_Item(Stock_Item):
    def update_quality(self):
        if self.out_of_date():
            self.quality = MIN_ITEM_QUALITY
        elif self.sell_in < FIVE_DAYS:
            self._improve_quality(3)
        elif self.sell_in < TEN_DAYS:
            self._improve_quality(2)
        else:
            self._improve_quality(1)
