from scrapy.item import Item, Field


class LivingSocialDeal(Item):
    """Livingsocial container (disctionary-like object) for scraped data"""
    title = Field()
    descripttion = Field()
    link = Field()
    category = Field()
    location = Field()
    original_price = Field()
    price = Field()

