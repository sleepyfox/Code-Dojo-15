# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item._update_sell_in_value()
            self._update_quality_value(item)
            self._update_quality_when_sellin_passed(item)

    def _improve_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def _reduce_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def _update_quality_value(self, item):
        if item.name == AGED_BRIE or item.name == BACKSTAGE_PASS:
            self._improve_quality(item)
            if item.name == BACKSTAGE_PASS:
                if item.sell_in < 10:
                    self._improve_quality(item)
                if item.sell_in < 5:
                    self._improve_quality(item)
        else:
            if item.name != SULFURAS:
                self._reduce_quality(item)

    def _update_quality_when_sellin_passed(self, item):
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASS:
                    if item.name != SULFURAS:
                        self._reduce_quality(item)
                else:
                    item.quality = 0
            else:
                self._improve_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class Stock_Item(Item):
    def _update_sell_in_value(self):
        if self.name != SULFURAS:
            self.sell_in -= 1
