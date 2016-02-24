
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
  };var element = document.getElementById("83254b6a-95d2-47d0-8f72-d0fc93913f3b");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '83254b6a-95d2-47d0-8f72-d0fc93913f3b' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"7635ffef-a6cf-4ead-bfe8-db9b49c3fbac":{"roots":{"references":[{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"d86521f0-6bd6-499d-b884-f58c520667c0","type":"HelpTool"},{"attributes":{"formatter":{"id":"47bd181a-85dd-4adf-b3e5-72b16bd30b81","type":"BasicTickFormatter"},"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"},"ticker":{"id":"7290cdc9-cb96-44c9-ba08-abc923557ef6","type":"BasicTicker"}},"id":"89f919f7-b671-4a9c-84a2-6b6b6026882f","type":"LinearAxis"},{"attributes":{},"id":"47bd181a-85dd-4adf-b3e5-72b16bd30b81","type":"BasicTickFormatter"},{"attributes":{"callback":null},"id":"64b08fa1-2028-4f45-9be5-d14d3505b814","type":"DataRange1d"},{"attributes":{},"id":"36c3733c-4538-4b0f-be6b-4ca3d32906ca","type":"ToolEvents"},{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"e7dc32b6-c3cd-4d90-beec-17792263b137","type":"WheelZoomTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"cbd6b1fe-7177-4cc1-a04e-5b96e5bc2b15","type":"BoxAnnotation"},{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"a9540b59-e7c5-4701-9024-bcf12cecb74e","type":"ResetTool"},{"attributes":{"data_source":{"id":"5f847bb9-cfdb-41f9-abc9-9b1ea070a891","type":"ColumnDataSource"},"glyph":{"id":"489d6353-45d5-4a83-a8aa-e743ba5fadcd","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"ecfc8cfc-89cd-47f1-b305-058fac933fbb","type":"Line"},"selection_glyph":null},"id":"642975b7-5e76-4d3f-9d6a-cbbf2e00b3d5","type":"GlyphRenderer"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"ecfc8cfc-89cd-47f1-b305-058fac933fbb","type":"Line"},{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"},"ticker":{"id":"4fcf989f-7855-47e2-9027-d80785afa3d9","type":"BasicTicker"}},"id":"c02436a2-aa9a-4d71-8242-7396443e304e","type":"Grid"},{"attributes":{"overlay":{"id":"cbd6b1fe-7177-4cc1-a04e-5b96e5bc2b15","type":"BoxAnnotation"},"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"691c885c-e6c3-4762-bde1-acb65925aced","type":"BoxZoomTool"},{"attributes":{"below":[{"id":"e97669b9-979a-4580-92e3-18c8ee757be7","type":"LinearAxis"}],"left":[{"id":"89f919f7-b671-4a9c-84a2-6b6b6026882f","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"e97669b9-979a-4580-92e3-18c8ee757be7","type":"LinearAxis"},{"id":"c02436a2-aa9a-4d71-8242-7396443e304e","type":"Grid"},{"id":"89f919f7-b671-4a9c-84a2-6b6b6026882f","type":"LinearAxis"},{"id":"6de19d5d-807a-482d-bb94-ba05f9a142cd","type":"Grid"},{"id":"cbd6b1fe-7177-4cc1-a04e-5b96e5bc2b15","type":"BoxAnnotation"},{"id":"bb906de1-3e83-47b2-9941-c192292b7f94","type":"Legend"},{"id":"5c3ed8e8-f38c-4329-81a0-2f1b899c0972","type":"GlyphRenderer"},{"id":"642975b7-5e76-4d3f-9d6a-cbbf2e00b3d5","type":"GlyphRenderer"}],"title":"Line plot","tool_events":{"id":"36c3733c-4538-4b0f-be6b-4ca3d32906ca","type":"ToolEvents"},"tools":[{"id":"1b41af36-1968-4819-906b-4db5b60d677e","type":"PanTool"},{"id":"e7dc32b6-c3cd-4d90-beec-17792263b137","type":"WheelZoomTool"},{"id":"691c885c-e6c3-4762-bde1-acb65925aced","type":"BoxZoomTool"},{"id":"8e5adf94-a236-46dc-b299-1587ac72c3fa","type":"PreviewSaveTool"},{"id":"b8e763b4-83e7-4eb5-ad92-bcf21cbe4092","type":"ResizeTool"},{"id":"a9540b59-e7c5-4701-9024-bcf12cecb74e","type":"ResetTool"},{"id":"d86521f0-6bd6-499d-b884-f58c520667c0","type":"HelpTool"}],"x_range":{"id":"64b08fa1-2028-4f45-9be5-d14d3505b814","type":"DataRange1d"},"y_range":{"id":"bce61bf8-c1c0-444b-813c-82ad75113c75","type":"DataRange1d"}},"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"},{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"1b41af36-1968-4819-906b-4db5b60d677e","type":"PanTool"},{"attributes":{"data_source":{"id":"b9488ee0-cbaf-4a42-82ba-5f264c441cb3","type":"ColumnDataSource"},"glyph":{"id":"2ef053ac-9a96-4aa0-bc40-22ad6ef1cfe4","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"e19e2436-4eb1-48e3-95af-1b8da1dea10a","type":"Line"},"selection_glyph":null},"id":"5c3ed8e8-f38c-4329-81a0-2f1b899c0972","type":"GlyphRenderer"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"e19e2436-4eb1-48e3-95af-1b8da1dea10a","type":"Line"},{"attributes":{"dimension":1,"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"},"ticker":{"id":"7290cdc9-cb96-44c9-ba08-abc923557ef6","type":"BasicTicker"}},"id":"6de19d5d-807a-482d-bb94-ba05f9a142cd","type":"Grid"},{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"b8e763b4-83e7-4eb5-ad92-bcf21cbe4092","type":"ResizeTool"},{"attributes":{"line_color":{"value":"blue"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"489d6353-45d5-4a83-a8aa-e743ba5fadcd","type":"Line"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"2ef053ac-9a96-4aa0-bc40-22ad6ef1cfe4","type":"Line"},{"attributes":{"callback":null,"column_names":["index","y","x","foo"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"b9488ee0-cbaf-4a42-82ba-5f264c441cb3","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"8e5adf94-a236-46dc-b299-1587ac72c3fa","type":"PreviewSaveTool"},{"attributes":{"callback":null},"id":"bce61bf8-c1c0-444b-813c-82ad75113c75","type":"DataRange1d"},{"attributes":{},"id":"7290cdc9-cb96-44c9-ba08-abc923557ef6","type":"BasicTicker"},{"attributes":{"legends":[["y",[{"id":"5c3ed8e8-f38c-4329-81a0-2f1b899c0972","type":"GlyphRenderer"}]],["foo",[{"id":"642975b7-5e76-4d3f-9d6a-cbbf2e00b3d5","type":"GlyphRenderer"}]]],"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"}},"id":"bb906de1-3e83-47b2-9941-c192292b7f94","type":"Legend"},{"attributes":{"callback":null,"column_names":["index","y","x","foo"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"5f847bb9-cfdb-41f9-abc9-9b1ea070a891","type":"ColumnDataSource"},{"attributes":{"formatter":{"id":"9f0ab2b8-7ee3-424a-bc53-a6ce8e5edccb","type":"BasicTickFormatter"},"plot":{"id":"4496387c-5b67-4024-9d0c-893bb5013c69","subtype":"Figure","type":"Plot"},"ticker":{"id":"4fcf989f-7855-47e2-9027-d80785afa3d9","type":"BasicTicker"}},"id":"e97669b9-979a-4580-92e3-18c8ee757be7","type":"LinearAxis"},{"attributes":{},"id":"4fcf989f-7855-47e2-9027-d80785afa3d9","type":"BasicTicker"},{"attributes":{},"id":"9f0ab2b8-7ee3-424a-bc53-a6ce8e5edccb","type":"BasicTickFormatter"}],"root_ids":["4496387c-5b67-4024-9d0c-893bb5013c69"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"7635ffef-a6cf-4ead-bfe8-db9b49c3fbac","elementid":"83254b6a-95d2-47d0-8f72-d0fc93913f3b","modelid":"4496387c-5b67-4024-9d0c-893bb5013c69"}];
          
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