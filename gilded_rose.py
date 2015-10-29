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
            item.update_sell_in_value()
            item.update_quality_value()
            item.update_quality_when_sellin_passed()

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

    def update_sell_in_value(self):
        if self.name != SULFURAS:
            self.sell_in -= 1

    def _improve_quality(self):
        if self.quality < 50:
            self.quality += 1

    def _reduce_quality(self):
        if self.quality > 0 and self.name != SULFURAS:
            self.quality -= 1

    def update_quality_value(self):
        if self.name == AGED_BRIE:
            self._improve_quality()
        elif self.name == BACKSTAGE_PASS:
            self._improve_quality()
            if self.sell_in < TEN_DAYS:
                self._improve_quality()
            if self.sell_in < FIVE_DAYS:
                self._improve_quality()
        else:
            self._reduce_quality()

    def update_quality_when_sellin_passed(self):
        if self.out_of_date():
            if self.name == AGED_BRIE:
                self._improve_quality()
            elif self.name == BACKSTAGE_PASS:
                self.quality = 0
            else:
                self._reduce_quality()
