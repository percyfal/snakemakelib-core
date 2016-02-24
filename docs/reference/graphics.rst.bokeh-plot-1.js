
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
  };var element = document.getElementById("45a0d37d-498c-4e2b-b901-67d1168257fc");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '45a0d37d-498c-4e2b-b901-67d1168257fc' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"3b737d49-729d-4283-9446-b8e66454b756":{"roots":{"references":[{"attributes":{"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"42f1a077-ee0b-484a-909e-2895ff58e234","type":"Line"},{"attributes":{},"id":"cdc8ee1f-6397-4f58-bd5f-7c04746bec3e","type":"BasicTickFormatter"},{"attributes":{},"id":"91b38f8d-219b-41b5-aab6-984d3b6e7fa8","type":"BasicTicker"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"13334b29-ce5d-4647-bb4d-31f0dc29c491","type":"ColumnDataSource"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"95da9d8b-d18a-4cb2-a85e-e1ad7a67ff38","type":"Line"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"x"}},"id":"386a6e12-0ca6-460f-b963-c5385db45482","type":"Line"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"19e52f46-7ecd-4225-b279-97074aede339","type":"BoxAnnotation"},{"attributes":{"dimension":1,"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"},"ticker":{"id":"91b38f8d-219b-41b5-aab6-984d3b6e7fa8","type":"BasicTicker"}},"id":"aeab3bc6-0b92-4cf2-a024-de8a18c61159","type":"Grid"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"x"}},"id":"3dccf5c3-ee4f-46bd-b81b-4ac69bc0bdc3","type":"Line"},{"attributes":{"callback":null},"id":"39e59be6-6fdf-46f2-8818-738d217d3efc","type":"DataRange1d"},{"attributes":{"overlay":{"id":"19e52f46-7ecd-4225-b279-97074aede339","type":"BoxAnnotation"},"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"7239d35f-4362-40b4-9df9-42789c817525","type":"BoxZoomTool"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"ee6ee6cb-5dd3-427e-ab76-039f86b7b686","type":"ColumnDataSource"},{"attributes":{"callback":null},"id":"ca07b9e7-4539-4f8a-9136-7695bda3532c","type":"DataRange1d"},{"attributes":{},"id":"54a1365e-b554-4c36-b5bc-fd2a7cdbf3b4","type":"ToolEvents"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"47decdeb-6506-4f12-a082-02447ca1ad17","type":"ResetTool"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"},"ticker":{"id":"319567cc-34c3-4d27-9e19-4e2d41ac9807","type":"BasicTicker"}},"id":"a37a8f3f-a2f9-4691-b489-541399625715","type":"Grid"},{"attributes":{"legends":[["y",[{"id":"39e5d64c-233c-48fd-8fda-ce5f9a795ca4","type":"GlyphRenderer"}]],["x",[{"id":"7f51faed-3ddc-401d-8f93-605fc34a6b49","type":"GlyphRenderer"}]]],"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"d8f75c87-aa7d-40de-b106-f1c056ec4812","type":"Legend"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"9f5ced98-e769-4b0c-a94b-94d3f1e4f34d","type":"PanTool"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"a46b55e8-a4b4-4889-a005-13de09ae276a","type":"ResizeTool"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"cfcea8fb-f81e-4ced-b3b5-c914d75fb698","type":"HelpTool"},{"attributes":{"below":[{"id":"30323634-d708-4e71-a90d-7c893ab9207e","type":"LinearAxis"}],"left":[{"id":"80daf3a3-5250-44d6-982f-00c74732325f","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"30323634-d708-4e71-a90d-7c893ab9207e","type":"LinearAxis"},{"id":"a37a8f3f-a2f9-4691-b489-541399625715","type":"Grid"},{"id":"80daf3a3-5250-44d6-982f-00c74732325f","type":"LinearAxis"},{"id":"aeab3bc6-0b92-4cf2-a024-de8a18c61159","type":"Grid"},{"id":"19e52f46-7ecd-4225-b279-97074aede339","type":"BoxAnnotation"},{"id":"d8f75c87-aa7d-40de-b106-f1c056ec4812","type":"Legend"},{"id":"39e5d64c-233c-48fd-8fda-ce5f9a795ca4","type":"GlyphRenderer"},{"id":"7f51faed-3ddc-401d-8f93-605fc34a6b49","type":"GlyphRenderer"}],"title":"Line plot","tool_events":{"id":"54a1365e-b554-4c36-b5bc-fd2a7cdbf3b4","type":"ToolEvents"},"tools":[{"id":"9f5ced98-e769-4b0c-a94b-94d3f1e4f34d","type":"PanTool"},{"id":"ffbbdf3a-2c44-40cc-bb6e-65267eed8d34","type":"WheelZoomTool"},{"id":"7239d35f-4362-40b4-9df9-42789c817525","type":"BoxZoomTool"},{"id":"0987130a-b1a2-45d3-9cd8-96c5229ef9df","type":"PreviewSaveTool"},{"id":"a46b55e8-a4b4-4889-a005-13de09ae276a","type":"ResizeTool"},{"id":"47decdeb-6506-4f12-a082-02447ca1ad17","type":"ResetTool"},{"id":"cfcea8fb-f81e-4ced-b3b5-c914d75fb698","type":"HelpTool"}],"x_range":{"id":"39e59be6-6fdf-46f2-8818-738d217d3efc","type":"DataRange1d"},"y_range":{"id":"ca07b9e7-4539-4f8a-9136-7695bda3532c","type":"DataRange1d"}},"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"0987130a-b1a2-45d3-9cd8-96c5229ef9df","type":"PreviewSaveTool"},{"attributes":{"formatter":{"id":"cdc8ee1f-6397-4f58-bd5f-7c04746bec3e","type":"BasicTickFormatter"},"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"},"ticker":{"id":"91b38f8d-219b-41b5-aab6-984d3b6e7fa8","type":"BasicTicker"}},"id":"80daf3a3-5250-44d6-982f-00c74732325f","type":"LinearAxis"},{"attributes":{},"id":"319567cc-34c3-4d27-9e19-4e2d41ac9807","type":"BasicTicker"},{"attributes":{"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"}},"id":"ffbbdf3a-2c44-40cc-bb6e-65267eed8d34","type":"WheelZoomTool"},{"attributes":{"formatter":{"id":"7b9c8ccc-6c75-4ab8-982e-d1e243023138","type":"BasicTickFormatter"},"plot":{"id":"342062fc-056f-4e7a-a923-c571bc4bfd65","subtype":"Figure","type":"Plot"},"ticker":{"id":"319567cc-34c3-4d27-9e19-4e2d41ac9807","type":"BasicTicker"}},"id":"30323634-d708-4e71-a90d-7c893ab9207e","type":"LinearAxis"},{"attributes":{},"id":"7b9c8ccc-6c75-4ab8-982e-d1e243023138","type":"BasicTickFormatter"},{"attributes":{"data_source":{"id":"13334b29-ce5d-4647-bb4d-31f0dc29c491","type":"ColumnDataSource"},"glyph":{"id":"42f1a077-ee0b-484a-909e-2895ff58e234","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"95da9d8b-d18a-4cb2-a85e-e1ad7a67ff38","type":"Line"},"selection_glyph":null},"id":"39e5d64c-233c-48fd-8fda-ce5f9a795ca4","type":"GlyphRenderer"},{"attributes":{"data_source":{"id":"ee6ee6cb-5dd3-427e-ab76-039f86b7b686","type":"ColumnDataSource"},"glyph":{"id":"386a6e12-0ca6-460f-b963-c5385db45482","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"3dccf5c3-ee4f-46bd-b81b-4ac69bc0bdc3","type":"Line"},"selection_glyph":null},"id":"7f51faed-3ddc-401d-8f93-605fc34a6b49","type":"GlyphRenderer"}],"root_ids":["342062fc-056f-4e7a-a923-c571bc4bfd65"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"3b737d49-729d-4283-9446-b8e66454b756","elementid":"45a0d37d-498c-4e2b-b901-67d1168257fc","modelid":"342062fc-056f-4e7a-a923-c571bc4bfd65"}];
          
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