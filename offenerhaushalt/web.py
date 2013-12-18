from flask import render_template

from offenerhaushalt.core import app, sites, pages
from offenerhaushalt.util import jsonify, JSONEncoder


@app.route('/haushalt/<slug>/')
def site(slug):
    site = sites.get(slug)
    site_json = JSONEncoder().encode(site)
    return render_template('site.html', site=site, site_json=site_json)


@app.route('/page/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    print page.meta.get('frame')
    template = page.meta.get('template', 'page.html')
    return render_template(template, page=page,
    	framed=page.meta.get('framed', True))


@app.route('/sites.json')
def sites_json():
    return jsonify(sites)


@app.route('/laender/')
def states():
    _sites = [s for s in sites if s.level == 'land']
    return render_template('states.html', sites=_sites)


@app.route('/kommunen/')
def local():
    _sites = [s for s in sites if s.level not in ['land', 'bund']]
    return render_template('local.html', sites=_sites)


@app.route('/')
def index():
    return render_template('index.html', sites=sites)
