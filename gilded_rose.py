# -*- coding: utf-8 -*-


class DefaultBehavior:
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = max(0, item.quality - 2)
        else:
            item.quality = max(0, item.quality - 1)
        item.sell_in = item.sell_in - 1


class AgedBrieBehavior:
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
        item.sell_in = item.sell_in - 1


class BackstagePassTAFKAL80ETCBehavior:
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in <= 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
        item.sell_in = item.sell_in - 1


class SulfurasBehavior:
    def update_quality(self, item):
        # This is a legendary item, never has to be sold or never degrades.
        pass


class ConjuredBehavior:
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = max(0, item.quality - 4)
        else:
            item.quality = max(0, item.quality - 2)
        item.sell_in = item.sell_in - 1


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
