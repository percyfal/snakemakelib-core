
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
  };var element = document.getElementById("5476662e-777d-4f15-a8dc-44e1f827b67c");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '5476662e-777d-4f15-a8dc-44e1f827b67c' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"4e1aa230-8506-49ce-bd88-c46bf4dcf67c":{"roots":{"references":[{"attributes":{"below":[{"id":"bcdf4129-12c0-45e0-8194-af95594c278b","type":"LinearAxis"}],"left":[{"id":"79fdfe96-b8d2-45c0-92a3-7751f11bb5dd","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"bcdf4129-12c0-45e0-8194-af95594c278b","type":"LinearAxis"},{"id":"3d104087-64e7-4ae9-afd7-8433ebb3d28e","type":"Grid"},{"id":"79fdfe96-b8d2-45c0-92a3-7751f11bb5dd","type":"LinearAxis"},{"id":"e8ec3a2a-8a42-427e-b43b-5068c5b40eb2","type":"Grid"},{"id":"904c44ea-287f-422c-9ee3-24fcc6b55552","type":"BoxAnnotation"},{"id":"93de13a0-1b98-4b36-a099-1aed64ab0698","type":"Legend"},{"id":"65582ba2-e15f-4b6a-940e-4f1d5f4bff3c","type":"GlyphRenderer"},{"id":"e4daae1e-dd99-4065-909d-2a036319be74","type":"GlyphRenderer"}],"title":"Line plot","tool_events":{"id":"b4455ef6-3ea5-43d4-818d-611476976bc3","type":"ToolEvents"},"tools":[{"id":"b75349e9-b39f-4acf-975d-b04cd25707e6","type":"PanTool"},{"id":"e84071be-3346-4bbd-9454-d4d1a502ba4e","type":"WheelZoomTool"},{"id":"9364dbbe-9b55-4aec-8e3f-7db212352ae4","type":"BoxZoomTool"},{"id":"1a7a17f0-5829-4fb8-ac85-ba959180d045","type":"PreviewSaveTool"},{"id":"7b220ac1-fee3-4957-b282-36af67699128","type":"ResizeTool"},{"id":"b14b38c0-5652-4c5e-8682-eac0a0c2074a","type":"ResetTool"},{"id":"4ac2f1b8-ca4e-41d5-9a19-3379c6526f4b","type":"HelpTool"}],"x_range":{"id":"3b10c204-f462-4fd7-9196-ef4d2f3895cd","type":"DataRange1d"},"y_range":{"id":"54234cdf-5ab4-422f-b18f-565146816786","type":"DataRange1d"}},"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"56026343-664e-4da4-a7f9-23d69775c504","type":"Line"},{"attributes":{"callback":null},"id":"54234cdf-5ab4-422f-b18f-565146816786","type":"DataRange1d"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"b14b38c0-5652-4c5e-8682-eac0a0c2074a","type":"ResetTool"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"7b220ac1-fee3-4957-b282-36af67699128","type":"ResizeTool"},{"attributes":{},"id":"7d29553b-cceb-4ac3-8e96-1afeb727dc37","type":"BasicTickFormatter"},{"attributes":{},"id":"f6aec357-c2c7-44ce-b205-54e7195be062","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"7d29553b-cceb-4ac3-8e96-1afeb727dc37","type":"BasicTickFormatter"},"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"},"ticker":{"id":"59c1e688-4042-423a-a21d-d040d3ec6e1a","type":"BasicTicker"}},"id":"bcdf4129-12c0-45e0-8194-af95594c278b","type":"LinearAxis"},{"attributes":{"data_source":{"id":"c9f6dfe0-a2af-4d0e-a5cb-464cc555025d","type":"ColumnDataSource"},"glyph":{"id":"56026343-664e-4da4-a7f9-23d69775c504","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"8657e5a4-b571-4ee3-8a83-d6c7cefb2761","type":"Line"},"selection_glyph":null},"id":"65582ba2-e15f-4b6a-940e-4f1d5f4bff3c","type":"GlyphRenderer"},{"attributes":{"legends":[["y",[{"id":"65582ba2-e15f-4b6a-940e-4f1d5f4bff3c","type":"GlyphRenderer"}]],["foo",[{"id":"e4daae1e-dd99-4065-909d-2a036319be74","type":"GlyphRenderer"}]]],"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"93de13a0-1b98-4b36-a099-1aed64ab0698","type":"Legend"},{"attributes":{"callback":null,"column_names":["y","x","foo","index"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"c9f6dfe0-a2af-4d0e-a5cb-464cc555025d","type":"ColumnDataSource"},{"attributes":{"callback":null},"id":"3b10c204-f462-4fd7-9196-ef4d2f3895cd","type":"DataRange1d"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"},"ticker":{"id":"59c1e688-4042-423a-a21d-d040d3ec6e1a","type":"BasicTicker"}},"id":"3d104087-64e7-4ae9-afd7-8433ebb3d28e","type":"Grid"},{"attributes":{},"id":"b4455ef6-3ea5-43d4-818d-611476976bc3","type":"ToolEvents"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"b75349e9-b39f-4acf-975d-b04cd25707e6","type":"PanTool"},{"attributes":{"data_source":{"id":"be1e97cf-fd37-4405-ac28-773a8a30cace","type":"ColumnDataSource"},"glyph":{"id":"b626bc19-1c70-4751-bf70-bbbe1f8f5fe0","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"ee2834d2-66ec-4a7c-a5b1-4281f179fb8c","type":"Line"},"selection_glyph":null},"id":"e4daae1e-dd99-4065-909d-2a036319be74","type":"GlyphRenderer"},{"attributes":{"overlay":{"id":"904c44ea-287f-422c-9ee3-24fcc6b55552","type":"BoxAnnotation"},"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"9364dbbe-9b55-4aec-8e3f-7db212352ae4","type":"BoxZoomTool"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"8657e5a4-b571-4ee3-8a83-d6c7cefb2761","type":"Line"},{"attributes":{"line_color":{"value":"blue"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"b626bc19-1c70-4751-bf70-bbbe1f8f5fe0","type":"Line"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"e84071be-3346-4bbd-9454-d4d1a502ba4e","type":"WheelZoomTool"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"4ac2f1b8-ca4e-41d5-9a19-3379c6526f4b","type":"HelpTool"},{"attributes":{},"id":"59c1e688-4042-423a-a21d-d040d3ec6e1a","type":"BasicTicker"},{"attributes":{"dimension":1,"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"},"ticker":{"id":"bebb662a-dce8-467c-b920-63c74a0e24e9","type":"BasicTicker"}},"id":"e8ec3a2a-8a42-427e-b43b-5068c5b40eb2","type":"Grid"},{"attributes":{},"id":"bebb662a-dce8-467c-b920-63c74a0e24e9","type":"BasicTicker"},{"attributes":{"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"}},"id":"1a7a17f0-5829-4fb8-ac85-ba959180d045","type":"PreviewSaveTool"},{"attributes":{"callback":null,"column_names":["y","x","foo","index"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"be1e97cf-fd37-4405-ac28-773a8a30cace","type":"ColumnDataSource"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"904c44ea-287f-422c-9ee3-24fcc6b55552","type":"BoxAnnotation"},{"attributes":{"formatter":{"id":"f6aec357-c2c7-44ce-b205-54e7195be062","type":"BasicTickFormatter"},"plot":{"id":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83","subtype":"Figure","type":"Plot"},"ticker":{"id":"bebb662a-dce8-467c-b920-63c74a0e24e9","type":"BasicTicker"}},"id":"79fdfe96-b8d2-45c0-92a3-7751f11bb5dd","type":"LinearAxis"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"ee2834d2-66ec-4a7c-a5b1-4281f179fb8c","type":"Line"}],"root_ids":["82e2eaee-23cd-447a-85c7-2ff1f7c46e83"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"4e1aa230-8506-49ce-bd88-c46bf4dcf67c","elementid":"5476662e-777d-4f15-a8dc-44e1f827b67c","modelid":"82e2eaee-23cd-447a-85c7-2ff1f7c46e83"}];
          
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