# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_sell_in_value()
            item.update_quality_value()
            item.update_quality_when_sellin_passed()

    def _improve_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def _reduce_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Stock_Item(Item):
    def update_sell_in_value(self):
        if self.name != SULFURAS:
            self.sell_in -= 1

    def _improve_quality(self):
        if self.quality < 50:
            self.quality += 1

    def _reduce_quality(self):
        if self.quality > 0:
            self.quality -= 1

    def update_quality_value(self):
        if self.name == AGED_BRIE or self.name == BACKSTAGE_PASS:
            self._improve_quality()
            if self.name == BACKSTAGE_PASS:
                if self.sell_in < 10:
                    self._improve_quality()
                if self.sell_in < 5:
                    self._improve_quality()
        else:
            if self.name != SULFURAS:
                self._reduce_quality()

    def update_quality_when_sellin_passed(self):
        if self.sell_in < 0:
            if self.name != AGED_BRIE:
                if self.name != BACKSTAGE_PASS:
                    if self.name != SULFURAS:
                        self._reduce_quality()
                else:
                    self.quality = 0
            else:
                self._improve_quality()
