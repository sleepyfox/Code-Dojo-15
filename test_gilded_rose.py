# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Stock_Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_item_decreases_in_quality_by_one(self):
        items = [Stock_Item("Elixir of the Mongoose,", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_item_sell_by_decreases_by_one(self):
        items = [Stock_Item("Elixir of the Mongoose,", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_aged_brie_increases_in_quality(self):
        items = [Stock_Item("Aged Brie", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_cannot_exceed_fifty(self):
        items = [Stock_Item("Aged Brie", 50, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_cannot_be_below_zero(self):
        items = [Stock_Item("Elixir of the Mongoose,", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_legendary_items_dont_have_to_be_sold(self):
        items = [Stock_Item("Sulfuras, Hand of Ragnaros", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)

    def test_legendary_items_dont_decrease_in_quality(self):
        items = [Stock_Item("Sulfuras, Hand of Ragnaros", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_degrades_twice_as_fast_when_sellby_date_passed(self):
        items = [Stock_Item("Elixir of the Mongoose,", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_aged_brie_increases_in_quality_twice_as_fast_once_sell_by_passed(self):
        items = [Stock_Item("Aged Brie", 0, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_backstage_pass_increases_in_quality_until_10_before_sell_by(self):
        items = [Stock_Item("Backstage passes to a TAFKAL80ETC concert", 11, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_backstage_pass_increases_in_quality__by_two_until_5_before_sell_by(self):
        items = [Stock_Item("Backstage passes to a TAFKAL80ETC concert", 10, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_backstage_pass_increases_in_quality_by_3_until_sell_by(self):
        items = [Stock_Item("Backstage passes to a TAFKAL80ETC concert", 5, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_backstage_pass_loses_quality_at_sell_by(self):
            items = [Stock_Item("Backstage passes to a TAFKAL80ETC concert", 0, 4)]
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
