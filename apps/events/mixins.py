class MonthMixin(object):
    def get_context_data(self, **kwargs):
        context = super(MonthMixin, self).get_context_data(**kwargs)
        context['months'] = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL',
                             'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER',
                             'OCTOBER', 'NOVEMBER', 'DECEMBER']
        return context
