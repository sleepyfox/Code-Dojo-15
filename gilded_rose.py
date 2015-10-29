# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
TEN_DAYS = 10
FIVE_DAYS = 5

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
        if self.quality > 50:
            self.quality = 50

    def _reduce_quality(self, amount):
        self.quality -= amount
        if self.quality < 0:
            self.quality = 0

    def update_quality(self):
        if self.out_of_date():
            if self.name == AGED_BRIE:
                self._improve_quality(2)
            elif self.name == BACKSTAGE_PASS:
                self.quality = 0
            else:
                self._reduce_quality(2)
        else:
            if self.name == AGED_BRIE:
                self._improve_quality(1)
            elif self.name == BACKSTAGE_PASS:
                if self.sell_in < FIVE_DAYS:
                    self._improve_quality(3)
                elif self.sell_in < TEN_DAYS:
                    self._improve_quality(2)
                else:
                    self._improve_quality(1)
            else:
                self._reduce_quality(1)

class Legendary_Item(Stock_Item):
    def age_one_day(self):
        self.quality = 80
