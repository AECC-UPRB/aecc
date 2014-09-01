import datetime
from datetime import date

from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from django.shortcuts import redirect, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, InvalidPage

from .models import Event, Hackathon
from .mixins import MonthMixin

from .constants import MONTHS, FIRST_SEMESTER, SECOND_SEMESTER, SEMESTER_DETERMINATOR


class IndexView(MonthMixin, ListView):
    model = Event
    template_name = 'events/index.html'
    context_object_name = 'events_information'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['current_month'] = date.today().strftime('%B')
        context['semester'] = FIRST_SEMESTER if datetime.datetime.now(
        ).date() > SEMESTER_DETERMINATOR.date() else SECOND_SEMESTER
        return context


class EventView(DetailView):
    model = Event
    slug_field = 'title_slug'
    slug_url_kwarg = 'title_slug'
    template_name = 'events/event.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        event = Event.objects.get(title_slug=self.kwargs['title_slug'])
        context['is_current_date'] = event.event_date.date() == date.today()
        context[
            'has_checked_in'] = self.request.user in event.checked_in.all()
        context['pagination_dictionary'] = self.listing(
            self.kwargs['title_slug'])
        return context

    def listing(self, title_slug):
        event = Event.objects.get(title_slug=title_slug)
        people = event.checked_in.all()

        paginator = Paginator(people, 4)

        page = self.request.GET.get('page')

        try:
            section = page
            people_checked_in = paginator.page(page).object_list

        except:
            section = 1
            people_checked_in = paginator.page(1).object_list

        try:
            page_obj = paginator.page(section)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
        except InvalidPage:
            page_obj = paginator.page(paginator.num_pages)

        return {
            'pagination': paginator,
            'page_obj': page_obj,
            'people_checked_in': people_checked_in
        }


class HackathonView(TemplateView):
    model = Hackathon
    template_name = 'events/hackathon.html'
    context_object_name = 'hackathon_sponsors'

    def get_context_data(self, **kwargs):
        context = super(HackathonView, self).get_context_data(**kwargs)
        context['hackathon_sponsors'] = Hackathon.objects.all()
        return context


class EventByMonth(ListView):
    model = Event
    paginate_by = 5
    context_object_name = 'events'
    template_name = 'events/events_by_month.html'

    def get_queryset(self):
        return Event.objects.filter(month=self.kwargs['month']).order_by('event_date')

    def get_context_data(self, **kwargs):
        if self.kwargs['month'] not in MONTHS:
            raise Http404
        context = super(EventByMonth, self).get_context_data(**kwargs)
        context['month'] = self.kwargs['month']
        return context


class ParticipatingView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = "/events/%s/%s" % (kwargs['title_slug'], kwargs['month'],)
        return url

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            event = get_object_or_404(Event, title_slug=kwargs['month'])
            if request.user.id not in event.checked_in.all():
                event.checked_in.add(request.user.id)
                event.save()
        return redirect(self.get_redirect_url(self, *args, **kwargs))
