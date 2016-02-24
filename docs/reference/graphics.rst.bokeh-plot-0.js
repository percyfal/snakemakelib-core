
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
  };var element = document.getElementById("6d072295-291c-4c97-928a-a11edd490b6d");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '6d072295-291c-4c97-928a-a11edd490b6d' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"3186dea7-ecd1-4c68-aa2e-490de531e63b":{"roots":{"references":[{"attributes":{"callback":null,"column_names":["index","y","x"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"3f579e9c-4067-43d8-8f4b-8cb376d617bf","type":"ColumnDataSource"},{"attributes":{},"id":"b6480701-2470-413d-91b1-0ef18247a3e9","type":"BasicTickFormatter"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"ef325f9c-e84e-4f99-88fe-2d0c8bd51459","type":"Circle"},{"attributes":{"grid_line_color":{"value":"black"},"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"},"ticker":{"id":"8f3f301f-06e7-45ed-acb6-506ec8f05f23","type":"BasicTicker"}},"id":"a2c44030-8f16-40d4-9ab5-62960984fc87","type":"Grid"},{"attributes":{"below":[{"id":"2e560bb0-132a-4eab-8b74-3fc813527a5a","type":"LinearAxis"}],"left":[{"id":"e60847d8-0cfb-47b7-a240-6997dd6f496a","type":"LinearAxis"}],"plot_height":300,"plot_width":300,"renderers":[{"id":"2e560bb0-132a-4eab-8b74-3fc813527a5a","type":"LinearAxis"},{"id":"a2c44030-8f16-40d4-9ab5-62960984fc87","type":"Grid"},{"id":"e60847d8-0cfb-47b7-a240-6997dd6f496a","type":"LinearAxis"},{"id":"6dc3b7d1-760c-4807-b69d-68ceefeb2580","type":"Grid"},{"id":"080df8be-0b77-4498-8798-d2a1dfafb95a","type":"BoxAnnotation"},{"id":"9d53e26f-6270-49fe-8d55-c463860fee35","type":"GlyphRenderer"},{"id":"22cd3832-97c3-431d-94a1-9ce897236e07","type":"GlyphRenderer"}],"title":"My plot","title_text_color":{"value":"olive"},"title_text_font":"times","title_text_font_style":"italic","tool_events":{"id":"24f63a47-17b4-4ab0-aee9-26b59938ef40","type":"ToolEvents"},"tools":[{"id":"41f2a3df-e2f4-4e62-b8ca-66e9f3bfff7c","type":"PanTool"},{"id":"fd9ff521-a9bd-413c-af18-925ab8aba244","type":"WheelZoomTool"},{"id":"eceeb11c-f134-4d2f-917d-35a7f24c01a2","type":"BoxZoomTool"},{"id":"69807765-8a66-462f-8eef-54bdab6a6ab1","type":"PreviewSaveTool"},{"id":"f10bb203-9b78-4951-bdb6-2c3e38ee8326","type":"ResizeTool"},{"id":"51716249-44c1-4312-bf57-44827230f6f1","type":"ResetTool"},{"id":"d5bce9e0-1261-47b9-8272-67057a5fb9dc","type":"HelpTool"}],"x_range":{"id":"9ae7cc2d-351f-4487-bacb-59692b1ceef6","type":"DataRange1d"},"y_range":{"id":"dd1fed24-706d-4f22-b4d9-ff5a5d735ab1","type":"DataRange1d"}},"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"},{"attributes":{"axis_label":"x","formatter":{"id":"8c8af373-8076-44d7-bc8f-65b69d09279c","type":"BasicTickFormatter"},"major_label_orientation":1.0471975511965976,"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"},"ticker":{"id":"8f3f301f-06e7-45ed-acb6-506ec8f05f23","type":"BasicTicker"}},"id":"2e560bb0-132a-4eab-8b74-3fc813527a5a","type":"LinearAxis"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"080df8be-0b77-4498-8798-d2a1dfafb95a","type":"BoxAnnotation"},{"attributes":{"callback":null},"id":"dd1fed24-706d-4f22-b4d9-ff5a5d735ab1","type":"DataRange1d"},{"attributes":{"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"d5bce9e0-1261-47b9-8272-67057a5fb9dc","type":"HelpTool"},{"attributes":{"data_source":{"id":"af3b0a37-993a-451e-b62f-af01f8706ccd","type":"ColumnDataSource"},"glyph":{"id":"41004d95-6bb5-4582-9f11-a909066a1195","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"ef325f9c-e84e-4f99-88fe-2d0c8bd51459","type":"Circle"},"selection_glyph":null},"id":"22cd3832-97c3-431d-94a1-9ce897236e07","type":"GlyphRenderer"},{"attributes":{},"id":"8f3f301f-06e7-45ed-acb6-506ec8f05f23","type":"BasicTicker"},{"attributes":{},"id":"8c8af373-8076-44d7-bc8f-65b69d09279c","type":"BasicTickFormatter"},{"attributes":{"axis_label":null,"axis_line_color":{"value":null},"formatter":{"id":"b6480701-2470-413d-91b1-0ef18247a3e9","type":"BasicTickFormatter"},"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"},"ticker":{"id":"3551d740-6498-4962-ae7f-1b81f7c9e4f6","type":"BasicTicker"}},"id":"e60847d8-0cfb-47b7-a240-6997dd6f496a","type":"LinearAxis"},{"attributes":{"dimension":1,"grid_line_color":{"value":"black"},"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"},"ticker":{"id":"3551d740-6498-4962-ae7f-1b81f7c9e4f6","type":"BasicTicker"}},"id":"6dc3b7d1-760c-4807-b69d-68ceefeb2580","type":"Grid"},{"attributes":{"data_source":{"id":"3f579e9c-4067-43d8-8f4b-8cb376d617bf","type":"ColumnDataSource"},"glyph":{"id":"be32ac45-cfd6-4f78-b4f0-1c672d765766","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"40bb8750-9618-4b6b-ad33-583b9369db6b","type":"Circle"},"selection_glyph":null},"id":"9d53e26f-6270-49fe-8d55-c463860fee35","type":"GlyphRenderer"},{"attributes":{"callback":null},"id":"9ae7cc2d-351f-4487-bacb-59692b1ceef6","type":"DataRange1d"},{"attributes":{"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"f10bb203-9b78-4951-bdb6-2c3e38ee8326","type":"ResizeTool"},{"attributes":{"callback":null,"column_names":["index","y","x"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"af3b0a37-993a-451e-b62f-af01f8706ccd","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"69807765-8a66-462f-8eef-54bdab6a6ab1","type":"PreviewSaveTool"},{"attributes":{"fill_color":{"value":"red"},"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"be32ac45-cfd6-4f78-b4f0-1c672d765766","type":"Circle"},{"attributes":{"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"fd9ff521-a9bd-413c-af18-925ab8aba244","type":"WheelZoomTool"},{"attributes":{},"id":"24f63a47-17b4-4ab0-aee9-26b59938ef40","type":"ToolEvents"},{"attributes":{"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"41f2a3df-e2f4-4e62-b8ca-66e9f3bfff7c","type":"PanTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"40bb8750-9618-4b6b-ad33-583b9369db6b","type":"Circle"},{"attributes":{"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"51716249-44c1-4312-bf57-44827230f6f1","type":"ResetTool"},{"attributes":{"overlay":{"id":"080df8be-0b77-4498-8798-d2a1dfafb95a","type":"BoxAnnotation"},"plot":{"id":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44","subtype":"Figure","type":"Plot"}},"id":"eceeb11c-f134-4d2f-917d-35a7f24c01a2","type":"BoxZoomTool"},{"attributes":{},"id":"3551d740-6498-4962-ae7f-1b81f7c9e4f6","type":"BasicTicker"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"41004d95-6bb5-4582-9f11-a909066a1195","type":"Circle"}],"root_ids":["a8f68445-8d3e-4b6e-9630-da3eaa7ada44"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"3186dea7-ecd1-4c68-aa2e-490de531e63b","elementid":"6d072295-291c-4c97-928a-a11edd490b6d","modelid":"a8f68445-8d3e-4b6e-9630-da3eaa7ada44"}];
          
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