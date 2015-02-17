from datetime import datetime


def months_dropdown_content(request):
    if datetime.now().month <= 7:
        months = {
            '1': 'january', '2': 'february', '3': 'march',
            '4': 'april', '5': 'may'}
        return {'months': months}
    else:
        months = {
            '1': 'august', '2': 'september', '3': 'october',
            '4': 'november', '5': 'december'}
        return {'months': months}
