# Copyright (C) 2015 by Per Unneberg
import os
import mimetypes
import base64
from bokeh.resources import INLINE
from bokeh.templates import JS_RESOURCES, CSS_RESOURCES
from bokeh.embed import components
from bokeh.models.widget import Widget
from bokeh.util.string import encode_utf8


def static_html(template, title="snakemakelib-core bokeh plot", resources=INLINE, css_raw=None, template_variables=None):
    """Render static html document.

    This is a minor modification of :py:meth:`bokeh.embed.file_html`.

    Args:
      template (Template): a Jinja2 HTML document template
      title (str): a title for the HTML document ``<title>`` tags.
      resources (Resources): a resource configuration for BokehJS assets
      css_raw (list): a list of file names for inclusion in the raw css

      template_variables (dict): variables to be used in the Jinja2
          template. In contrast to :py:meth:`bokeh.embed.file_html`,
          this is where plot objects are placed. The plot objects will
          be automagically split into script and div components. If
          used, the following variable names will be overwritten:
          title, js_resources, css_resources

    Returns:
      html : standalone HTML document with embedded plot

    """
    # From bokeh.resources
    def _inline(paths):
        strings = []
        for path in paths:
            begin = "/* BEGIN %s */" % path
            middle = open(path, 'rb').read().decode("utf-8")
            end = "/* END %s */" % path
            strings.append(begin + '\n' + middle + '\n' + end)
        return strings


    # Assume we always have resources
    js_resources = resources
    css_resources = resources

    bokeh_js = ''
    if js_resources:
        bokeh_js = JS_RESOURCES.render(js_raw=js_resources.js_raw, js_files=js_resources.js_files)

    bokeh_css = ''

    _css_raw = css_resources.css_raw
    if css_raw:
        tmp = lambda: _inline(css_raw)
        _css_raw += tmp()
    if css_resources:
        bokeh_css = CSS_RESOURCES.render(css_raw=_css_raw, css_files=css_resources.css_files)
        
    # Hack to get on-the-fly double mapping
    def _update(template_variables):
        tmp = {}
        for k, v in template_variables.items():
            if (isinstance(v, Widget)):
                tmp.update({k: [{'script': s, 'div': d}
                                for s, d in [components(v, resources)]][0]})
            elif (isinstance(v, dict)):
                if not v:
                    tmp.update(v)
                else:
                    v.update(_update(v))
            else:
                tmp.update({k: v})
        return tmp

    template_variables.update(_update(template_variables))
    template_variables_full = \
        template_variables.copy() if template_variables is not None else {}
    template_variables_full.update(
        {
            'title' : title,
            'bokeh_js' : bokeh_js,
            'bokeh_css' : bokeh_css,
        }     
    )
    html = template.render(template_variables_full)
    return encode_utf8(html)
