# -*- coding: utf-8 -*-

from gilded_rose.goods import Goods
from gilded_rose.behaviors.default import DefaultBehavior
from gilded_rose.behaviors.aged_brie import AgedBrieBehavior
from gilded_rose.behaviors.backstage_pass import BackstagePassTAFKAL80ETCBehavior
from gilded_rose.behaviors.conjured import ConjuredBehavior
from gilded_rose.behaviors.sulfuras import SulfurasBehavior

BEHAVIORS = {
    Goods.AGED_BRIE.value: AgedBrieBehavior(),
    Goods.BACKSTAGE_PASS.value: BackstagePassTAFKAL80ETCBehavior(),
    Goods.SULFURAS.value: SulfurasBehavior(),
    Goods.CONJURED.value: ConjuredBehavior(),
}

DEFAULT_BEHAVIOR = DefaultBehavior()


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            behavior = BEHAVIORS.get(item.name, DEFAULT_BEHAVIOR)
            behavior.update_quality(item)
