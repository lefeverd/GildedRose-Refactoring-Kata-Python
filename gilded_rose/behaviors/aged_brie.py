class AgedBrieBehavior:
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)
        item.sell_in = item.sell_in - 1
