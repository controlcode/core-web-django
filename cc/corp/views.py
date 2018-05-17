from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import logging

analytics = settings.GOOGLE_ANALYTICS

logger = logging.getLogger(__name__)

logger.info('Environment Configuration')
logger.info('-------------------------')
#logger.info(f'Google Analytics = {analytics}')
logger.info("Google Analytics = {}".format(analytics))


def index(request):
    context = {}
    template = loader.get_template('corp/index.html')
    return HttpResponse(template.render(context, request))


def about(request):
    context={}
    template = loader.get_template('corp/about.html')
    return HttpResponse(template.render(context, request))


def enterprise(request):
    context={}
    template = loader.get_template('corp/enterprise.html')
    return HttpResponse(template.render(context, request))
