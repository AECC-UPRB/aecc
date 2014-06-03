from django_ical.views import ICalFeed
from .models import Event


class EventCalendarFeed(ICalFeed):
    product_id = '-//aecc-uprb.org//aecc-uprb//EN'
    timezone = 'UTC'
    title = 'UPRB-AECC.org'
    description = 'Calendario de reuniones UPRB-AECC'

    def items(self):
        return Event.objects.all().order_by('-event_date')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.event_date

    def timezone(self):
        return

    def item_guid(self, item):
        return '{0}@events.{1}'.format(item.id, 'aecc-uprb.org')
