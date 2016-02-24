
(function(global) {
  function now() {
    return new Date();
  }

  if (typeof (window._bokeh_onload_callbacks) === "undefined") {
    window._bokeh_onload_callbacks = [];
  }

  function run_callbacks() {
    window._bokeh_onload_callbacks.forEach(function(callback) { callback() });
    delete window._bokeh_onload_callbacks
    console.info("Bokeh: all callbacks have finished");
  }

  function load_libs(js_urls, callback) {
    window._bokeh_onload_callbacks.push(callback);
    if (window._bokeh_is_loading > 0) {
      console.log("Bokeh: BokehJS is being loaded, scheduling callback at", now());
      return null;
    }
    if (js_urls == null || js_urls.length === 0) {
      run_callbacks();
      return null;
    }
    console.log("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
    window._bokeh_is_loading = js_urls.length;
    for (var i = 0; i < js_urls.length; i++) {
      var url = js_urls[i];
      var s = document.createElement('script');
      s.src = url;
      s.async = false;
      s.onreadystatechange = s.onload = function() {
        window._bokeh_is_loading--;
        if (window._bokeh_is_loading === 0) {
          console.log("Bokeh: all BokehJS libraries loaded");
          run_callbacks()
        }
      };
      s.onerror = function() {
        console.warn("failed to load library " + url);
      };
      console.log("Bokeh: injecting script tag for BokehJS library: ", url);
      document.getElementsByTagName("head")[0].appendChild(s);
    }
  };var element = document.getElementById("db4cdc37-1f72-4323-b860-715e78e695d6");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid 'db4cdc37-1f72-4323-b860-715e78e695d6' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"e6cd2483-08d7-46a5-b26c-29ab158264de":{"roots":{"references":[{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"x"}},"id":"eb3fb7b3-a653-412b-9a3a-df9e663ee72c","type":"Line"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"92edcdb9-e0d1-4378-8173-e91b18212191","type":"PreviewSaveTool"},{"attributes":{},"id":"14a37df1-9dcb-4e71-b12d-4ad86cb50c5e","type":"BasicTickFormatter"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"9306669b-acdf-434a-9662-47269ef5b982","type":"Line"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"1c1340f3-7784-4901-a87f-c737c99c8cf5","type":"WheelZoomTool"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"x"}},"id":"c160508e-7a38-4f56-92ff-91dc49207f4f","type":"Line"},{"attributes":{"dimension":1,"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"},"ticker":{"id":"ba4938cc-8a14-47de-9f2a-6150d9021404","type":"BasicTicker"}},"id":"7e892e22-6231-4463-acdf-e34b6f2522b8","type":"Grid"},{"attributes":{},"id":"ab312a46-1b85-4f16-929c-8829ca28cd09","type":"BasicTickFormatter"},{"attributes":{"overlay":{"id":"a6007424-7ba7-49dc-b9a6-4ad9e3de87e8","type":"BoxAnnotation"},"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"53d255ad-99a4-49c0-a111-10db8642c00e","type":"BoxZoomTool"},{"attributes":{"below":[{"id":"c5cc2921-388f-45dc-a086-9c69360c1e70","type":"LinearAxis"}],"left":[{"id":"19f60729-9504-4622-9799-607cdf292a40","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"c5cc2921-388f-45dc-a086-9c69360c1e70","type":"LinearAxis"},{"id":"69f01307-9f3c-491f-b2c3-897d8aaa8117","type":"Grid"},{"id":"19f60729-9504-4622-9799-607cdf292a40","type":"LinearAxis"},{"id":"7e892e22-6231-4463-acdf-e34b6f2522b8","type":"Grid"},{"id":"a6007424-7ba7-49dc-b9a6-4ad9e3de87e8","type":"BoxAnnotation"},{"id":"d17372c7-72c8-42d1-b208-bf1ffd3f84cb","type":"Legend"},{"id":"bde477d5-f559-4d1f-9e07-c9a532c36db1","type":"GlyphRenderer"},{"id":"65f4223d-7abe-4652-9e0d-91c2a0ce1ae7","type":"GlyphRenderer"}],"title":"Line plot","tool_events":{"id":"ee7f0f91-0305-48c2-86ea-fe6a5371b535","type":"ToolEvents"},"tools":[{"id":"1b1dc9c3-fdf1-491a-b9a0-bec5fbb85405","type":"PanTool"},{"id":"1c1340f3-7784-4901-a87f-c737c99c8cf5","type":"WheelZoomTool"},{"id":"53d255ad-99a4-49c0-a111-10db8642c00e","type":"BoxZoomTool"},{"id":"92edcdb9-e0d1-4378-8173-e91b18212191","type":"PreviewSaveTool"},{"id":"d2cb1071-9acf-4723-95ed-48958ab17dfe","type":"ResizeTool"},{"id":"bc325990-8527-4477-a2f7-37a852ef010a","type":"ResetTool"},{"id":"6f76abe9-899c-4758-9480-27d96ec42587","type":"HelpTool"}],"x_range":{"id":"535a6381-35a0-405b-b6eb-7d7a0f0207dc","type":"DataRange1d"},"y_range":{"id":"93e51092-8487-41d5-902b-ca8215ee5104","type":"DataRange1d"}},"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"},{"attributes":{"callback":null,"column_names":["index","y","x"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"c97de9f8-09e5-4000-9374-f5043a40b6cb","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"},"ticker":{"id":"7d5cea2f-7387-470b-9731-58936d10f3b8","type":"BasicTicker"}},"id":"69f01307-9f3c-491f-b2c3-897d8aaa8117","type":"Grid"},{"attributes":{},"id":"ee7f0f91-0305-48c2-86ea-fe6a5371b535","type":"ToolEvents"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"1b1dc9c3-fdf1-491a-b9a0-bec5fbb85405","type":"PanTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"a6007424-7ba7-49dc-b9a6-4ad9e3de87e8","type":"BoxAnnotation"},{"attributes":{},"id":"ba4938cc-8a14-47de-9f2a-6150d9021404","type":"BasicTicker"},{"attributes":{"callback":null},"id":"93e51092-8487-41d5-902b-ca8215ee5104","type":"DataRange1d"},{"attributes":{"formatter":{"id":"14a37df1-9dcb-4e71-b12d-4ad86cb50c5e","type":"BasicTickFormatter"},"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"},"ticker":{"id":"7d5cea2f-7387-470b-9731-58936d10f3b8","type":"BasicTicker"}},"id":"c5cc2921-388f-45dc-a086-9c69360c1e70","type":"LinearAxis"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"d2cb1071-9acf-4723-95ed-48958ab17dfe","type":"ResizeTool"},{"attributes":{"callback":null},"id":"535a6381-35a0-405b-b6eb-7d7a0f0207dc","type":"DataRange1d"},{"attributes":{"callback":null,"column_names":["index","y","x"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"fb59c50b-d29b-4587-8e51-17d7858afec4","type":"ColumnDataSource"},{"attributes":{"formatter":{"id":"ab312a46-1b85-4f16-929c-8829ca28cd09","type":"BasicTickFormatter"},"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"},"ticker":{"id":"ba4938cc-8a14-47de-9f2a-6150d9021404","type":"BasicTicker"}},"id":"19f60729-9504-4622-9799-607cdf292a40","type":"LinearAxis"},{"attributes":{"legends":[["y",[{"id":"bde477d5-f559-4d1f-9e07-c9a532c36db1","type":"GlyphRenderer"}]],["x",[{"id":"65f4223d-7abe-4652-9e0d-91c2a0ce1ae7","type":"GlyphRenderer"}]]],"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"d17372c7-72c8-42d1-b208-bf1ffd3f84cb","type":"Legend"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"bc325990-8527-4477-a2f7-37a852ef010a","type":"ResetTool"},{"attributes":{"data_source":{"id":"fb59c50b-d29b-4587-8e51-17d7858afec4","type":"ColumnDataSource"},"glyph":{"id":"312bdcbb-40d4-4067-9901-310e2fd20f22","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"9306669b-acdf-434a-9662-47269ef5b982","type":"Line"},"selection_glyph":null},"id":"bde477d5-f559-4d1f-9e07-c9a532c36db1","type":"GlyphRenderer"},{"attributes":{},"id":"7d5cea2f-7387-470b-9731-58936d10f3b8","type":"BasicTicker"},{"attributes":{"plot":{"id":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f","subtype":"Figure","type":"Plot"}},"id":"6f76abe9-899c-4758-9480-27d96ec42587","type":"HelpTool"},{"attributes":{"data_source":{"id":"c97de9f8-09e5-4000-9374-f5043a40b6cb","type":"ColumnDataSource"},"glyph":{"id":"c160508e-7a38-4f56-92ff-91dc49207f4f","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"eb3fb7b3-a653-412b-9a3a-df9e663ee72c","type":"Line"},"selection_glyph":null},"id":"65f4223d-7abe-4652-9e0d-91c2a0ce1ae7","type":"GlyphRenderer"},{"attributes":{"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"312bdcbb-40d4-4067-9901-310e2fd20f22","type":"Line"}],"root_ids":["ea8d4ee7-e18d-4417-9ccd-dac07b7b908f"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"e6cd2483-08d7-46a5-b26c-29ab158264de","elementid":"db4cdc37-1f72-4323-b860-715e78e695d6","modelid":"ea8d4ee7-e18d-4417-9ccd-dac07b7b908f"}];
          
          Bokeh.embed.embed_items(docs_json, render_items);
      });
    },
    function(Bokeh) {
      console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.css");
      Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.css");
      console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.css");
      Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.css");
    }
  ];

  function run_inline_js() {
    for (var i = 0; i < inline_js.length; i++) {
      inline_js[i](window.Bokeh);
    }
  }

  if (window._bokeh_is_loading === 0) {
    console.log("Bokeh: BokehJS loaded, going straight to plotting");
    run_inline_js();
  } else {
    load_libs(js_urls, function() {
      console.log("Bokeh: BokehJS plotting callback run at", now());
      run_inline_js();
    });
  }
}(this));