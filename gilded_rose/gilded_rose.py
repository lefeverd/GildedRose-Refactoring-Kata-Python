# -*- coding: utf-8 -*-

from gilded_rose.behaviors.default import DefaultBehavior
from gilded_rose.behaviors.aged_brie import AgedBrieBehavior
from gilded_rose.behaviors.backstage_pass import BackstagePassTAFKAL80ETCBehavior
from gilded_rose.behaviors.conjured import ConjuredBehavior
from gilded_rose.behaviors.sulfuras import SulfurasBehavior

BEHAVIORS = {
    "Aged Brie": AgedBrieBehavior(),
    "Backstage passes to a TAFKAL80ETC concert":
    BackstagePassTAFKAL80ETCBehavior(),
    "Sulfuras, Hand of Ragnaros": SulfurasBehavior(),
    "Conjured": ConjuredBehavior(),
}

DEFAULT_BEHAVIOR = DefaultBehavior()


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            behavior = BEHAVIORS.get(item.name, DEFAULT_BEHAVIOR)
            behavior.update_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
