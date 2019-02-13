class ConjuredBehavior:
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = max(0, item.quality - 4)
        else:
            item.quality = max(0, item.quality - 2)
        item.sell_in = item.sell_in - 1
