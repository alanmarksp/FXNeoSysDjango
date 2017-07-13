from decimal import *
from random import gauss

from celery.task import periodic_task

from quotes.models import Quote


class ForexMarketSimulationTask:
    @staticmethod
    def run():
        quotes = Quote.objects.latest_quotes()
        if not quotes.exists():
            for symbol in Quote.SYMBOLS:
                Quote.objects.create(symbol=symbol[0], bid_price=1.0003, ask_price=1.0000)
        quotes = Quote.objects.latest_quotes()
        for quote in quotes:
            v = Decimal(round(gauss(0, 0.0001), 4))
            quote.bid_price = round(quote.bid_price + v, 4)
            quote.ask_price = round(quote.ask_price + v, 4)
            quote.save()
            print(quote.bid_price)


@periodic_task(run_every=1, name="run_simulation", ignore_result=True)
def run_simulation():
    ForexMarketSimulationTask.run()
