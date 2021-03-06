# -*- coding: utf-8 -*-
import unittest

from gilded_rose.gilded_rose import GildedRose
from gilded_rose.item import Item
from gilded_rose.goods import Goods


class GildedRoseTest(unittest.TestCase):
    def test_item_sell_in_decrease(self):
        items = [Item("Item", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_item_quality_decrease(self):
        items = [Item("Item", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Item", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_degrades_twice_after_sell_in(self):
        items = [Item("Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_maximum_quality(self):
        items = [Item(Goods.AGED_BRIE.value, 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_sell_in(self):
        items = [Item(Goods.SULFURAS.value, 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_sulfuras_quality_never_degrades(self):
        items = [Item(Goods.SULFURAS.value, 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_aged_brie_quality_increase(self):
        items = [Item(Goods.AGED_BRIE.value, 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_aged_brie_quality_increases_twice_after_sell_in(self):
        items = [Item(Goods.AGED_BRIE.value, 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_pass_quality_increase_by_two_ten_days_or_less(self):
        items = [Item(Goods.BACKSTAGE_PASS.value, 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_pass_quality_increase_by_three_five_days_or_less(self):
        items = [Item(Goods.BACKSTAGE_PASS.value, 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_pass_quality_drops_to_zero_after_sell_in(self):
        items = [Item(Goods.BACKSTAGE_PASS.value, 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_quality_normal_increase(self):
        """
        Verify the increase of the backstage pass when
        no special conditions apply.
        """
        items = [Item(Goods.BACKSTAGE_PASS.value, 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_multiple_items(self):
        items = [Item(Goods.AGED_BRIE.value, 5, 10), Item("Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[1].quality)
        self.assertEqual(4, items[1].sell_in)

    def test_conjured_quality_decrease_twice(self):
        items = [Item(Goods.CONJURED.value, 11, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_conjured_quality_decrease_by_four_after_sell_in(self):
        items = [Item(Goods.CONJURED.value, 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)

    def test_conjured_quality_never_negative(self):
        items = [Item(Goods.CONJURED.value, 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
