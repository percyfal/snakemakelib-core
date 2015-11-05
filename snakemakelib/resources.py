''' Provides access to templates and css files '''
import os
from jinja2 import Environment, PackageLoader
from bokeh.settings import ROOT_DIR
from snakemakelib import SNAKEMAKELIB_PATH
from snakemakelib.log import LoggerManager
logger = LoggerManager().getLogger(__name__)

# Template path and templates
SmlTemplateEnv = Environment(loader = PackageLoader("snakemakelib", "_templates"))
SmlTemplateEnv.globals.update(zip=zip)

# Static css files
css_files = [os.path.join(SNAKEMAKELIB_PATH, 'static', 'css', 'basic.css')]
bootstrap_css_files = [os.path.join(ROOT_DIR, "server/static/bootstrap/css/bootstrap.min.css"),
                       os.path.join(SNAKEMAKELIB_PATH, 'static', 'css', 'basic.css')]

# snakemakelib javascript library
js_files = [os.path.join(SNAKEMAKELIB_PATH, 'static', 'js', 'snakemakelib.js')]
bootstrap_js_files = [os.path.join(ROOT_DIR, "server/static/bootstrap/js/bootstrap.min.js"),
                      os.path.join(SNAKEMAKELIB_PATH, 'static', 'js', 'snakemakelib.js')]

                      
# Add coffee script here possible?
