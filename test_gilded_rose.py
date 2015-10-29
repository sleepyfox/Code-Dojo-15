# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_item_decreases_in_quality_by_one(self):
        items = [Item("Elixir of the Mongoose,", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_item_sell_by_decreases_by_one(self):
        items = [Item("Elixir of the Mongoose,", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_cannot_exceed_fifty(self):
        items = [Item("Aged Brie", 50, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

if __name__ == '__main__':
    unittest.main()
