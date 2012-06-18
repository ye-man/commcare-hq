from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from corehq.apps.domain.decorators import require_superuser
from corehq.apps.registration.forms import DomainRegistrationForm
from dimagi.utils.web import render_to_response, json_response, get_url_base
from corehq.apps.orgs.models import Organization
from corehq.apps.domain.models import Domain
from dimagi.utils.couch.database import get_db
from django.contrib import messages

@require_superuser
def appstore(request, template="appstore/appstore_base.html"):
    apps = Domain.published_snapshots()
    vals = dict(apps=apps)
    return render_to_response(request, template, vals)

@require_superuser
def app_info(request, domain, template="appstore/app_info.html"):
    domain = Domain.get_by_name(domain)
    vals = dict(domain=domain)
    return render_to_response(request, template, vals)

@require_superuser
def search_snapshots(request, template="appstore/appstore_base.html"):
    query = request.GET.get('q')
    limit = 10
    snapshots = map(Domain.get, [r['id'] for r in get_db().search('domain/snapshot_search', q=query)])
    return render_to_response(request, template, {'apps': snapshots, 'search_query': query})

