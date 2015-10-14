''' Provides access to templates and css files '''
from snakemakelib.log import LoggerManager
logger = LoggerManager().getLogger(__name__)
from jinja2 import Environment, PackageLoader
from snakemakelib import SNAKEMAKELIB_PATH

# Template path and templates
SmlTemplateEnv = Environment(loader = PackageLoader("snakemakelib", "_templates"))
SmlTemplateEnv.globals.update(zip=zip)

# Static css files
css_files = [os.path.join(SNAKEMAKELIB_PATH, 'static', 'basic.css')]

