# -*- coding: utf-8 -*-

ITEM_AGED_BRIE = "Aged Brie"
ITEM_BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
ITEM_SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self._update_quality(item)
            self._update_sell_in_value(item)
            self._update_quality_when_sellin_passed(item)

    def _update_quality(self, item):
        if item.name != ITEM_AGED_BRIE and item.name != ITEM_BACKSTAGE_PASS:
            if item.quality > 0:
                if item.name != ITEM_SULFURAS:
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == ITEM_BACKSTAGE_PASS:
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1

    def _update_sell_in_value(self, item):
        if item.name != ITEM_SULFURAS:
            item.sell_in = item.sell_in - 1

    def _update_quality_when_sellin_passed(self, item):
        if item.sell_in < 0:
            if item.name != ITEM_AGED_BRIE:
                if item.name != ITEM_BACKSTAGE_PASS:
                    if item.quality > 0:
                        if item.name != ITEM_SULFURAS:
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
