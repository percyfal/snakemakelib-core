
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
  };var element = document.getElementById("3711bd23-714d-4700-abf6-7417e80153df");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '3711bd23-714d-4700-abf6-7417e80153df' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"956c93d5-85c5-412b-a769-ed799131a654":{"roots":{"references":[{"attributes":{},"id":"965eedc6-27ba-49fc-a6d7-d59f6e063636","type":"BasicTickFormatter"},{"attributes":{"below":[{"id":"f21a2c9f-1892-4f08-a7fe-744a030be4f6","type":"LinearAxis"}],"left":[{"id":"4bc65242-216b-4dd2-9030-0bfe88e95ff6","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"f21a2c9f-1892-4f08-a7fe-744a030be4f6","type":"LinearAxis"},{"id":"7f6e1088-a7dc-4548-a066-f4182e583a5c","type":"Grid"},{"id":"4bc65242-216b-4dd2-9030-0bfe88e95ff6","type":"LinearAxis"},{"id":"785d7714-8220-4cb7-8629-1eefc1f32eee","type":"Grid"},{"id":"8edad728-5a89-4d36-8b6f-439aec38018f","type":"BoxAnnotation"},{"id":"b3aeb45f-c267-4868-835a-e5e1a5617439","type":"Legend"},{"id":"8cc3e09e-da71-41b2-bc71-ff5b40fc42c3","type":"GlyphRenderer"},{"id":"f36ac67e-a09d-41c2-a607-7622c1d1a5ac","type":"GlyphRenderer"}],"title":"Line plot","tool_events":{"id":"7c17ef47-10f6-41a9-9133-87f92e32aca7","type":"ToolEvents"},"tools":[{"id":"03e996df-eb26-40c4-8a48-3b9bb7d32254","type":"PanTool"},{"id":"4eaa53f6-00b0-425e-a577-688a1385ed17","type":"WheelZoomTool"},{"id":"f0ee3acc-6cbd-40e0-9015-bc6fc45a440f","type":"BoxZoomTool"},{"id":"81464267-ec0b-4a02-852f-2119ce953cce","type":"PreviewSaveTool"},{"id":"cc7c0ec6-9e43-4c90-b957-47e08580f8aa","type":"ResizeTool"},{"id":"db7ff109-71b6-459f-ba00-459a74e62feb","type":"ResetTool"},{"id":"6fcd405a-8291-4685-b6fa-7b5b7a8b9429","type":"HelpTool"}],"x_range":{"id":"b9cc0474-8692-4e0a-8920-475bb55184ec","type":"DataRange1d"},"y_range":{"id":"e53027cb-78e5-4ffb-b6ec-41d932542a90","type":"DataRange1d"}},"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"},{"attributes":{"callback":null},"id":"b9cc0474-8692-4e0a-8920-475bb55184ec","type":"DataRange1d"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"81464267-ec0b-4a02-852f-2119ce953cce","type":"PreviewSaveTool"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"6fcd405a-8291-4685-b6fa-7b5b7a8b9429","type":"HelpTool"},{"attributes":{"data_source":{"id":"dd4fb44d-333a-46aa-982b-eabc435ffc34","type":"ColumnDataSource"},"glyph":{"id":"472ab006-d060-41fa-8aed-b66128175ea2","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"6e12749e-a130-44a6-ad29-c51d5b2f6751","type":"Line"},"selection_glyph":null},"id":"f36ac67e-a09d-41c2-a607-7622c1d1a5ac","type":"GlyphRenderer"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"8edad728-5a89-4d36-8b6f-439aec38018f","type":"BoxAnnotation"},{"attributes":{},"id":"80a5a91f-0337-4afa-b81a-788cdd00e209","type":"BasicTicker"},{"attributes":{},"id":"c757b087-0b27-47fb-88ad-55f21fdb61bc","type":"BasicTicker"},{"attributes":{"data_source":{"id":"eedfd721-3bc3-47c4-bff9-bb95d5a66ab6","type":"ColumnDataSource"},"glyph":{"id":"f2b9473c-7563-4e49-b42b-29576fbb9276","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"624e28d8-af4c-42ee-8aef-da7e0e083f51","type":"Line"},"selection_glyph":null},"id":"8cc3e09e-da71-41b2-bc71-ff5b40fc42c3","type":"GlyphRenderer"},{"attributes":{"line_color":{"value":"blue"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"472ab006-d060-41fa-8aed-b66128175ea2","type":"Line"},{"attributes":{},"id":"8117b462-d815-473e-ad7f-db45fd8cc30d","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"965eedc6-27ba-49fc-a6d7-d59f6e063636","type":"BasicTickFormatter"},"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"},"ticker":{"id":"80a5a91f-0337-4afa-b81a-788cdd00e209","type":"BasicTicker"}},"id":"f21a2c9f-1892-4f08-a7fe-744a030be4f6","type":"LinearAxis"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"db7ff109-71b6-459f-ba00-459a74e62feb","type":"ResetTool"},{"attributes":{"callback":null,"column_names":["y","x","index","foo"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"dd4fb44d-333a-46aa-982b-eabc435ffc34","type":"ColumnDataSource"},{"attributes":{"dimension":1,"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"},"ticker":{"id":"c757b087-0b27-47fb-88ad-55f21fdb61bc","type":"BasicTicker"}},"id":"785d7714-8220-4cb7-8629-1eefc1f32eee","type":"Grid"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"03e996df-eb26-40c4-8a48-3b9bb7d32254","type":"PanTool"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"cc7c0ec6-9e43-4c90-b957-47e08580f8aa","type":"ResizeTool"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"4eaa53f6-00b0-425e-a577-688a1385ed17","type":"WheelZoomTool"},{"attributes":{"legends":[["y",[{"id":"8cc3e09e-da71-41b2-bc71-ff5b40fc42c3","type":"GlyphRenderer"}]],["foo",[{"id":"f36ac67e-a09d-41c2-a607-7622c1d1a5ac","type":"GlyphRenderer"}]]],"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"b3aeb45f-c267-4868-835a-e5e1a5617439","type":"Legend"},{"attributes":{"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"},"ticker":{"id":"80a5a91f-0337-4afa-b81a-788cdd00e209","type":"BasicTicker"}},"id":"7f6e1088-a7dc-4548-a066-f4182e583a5c","type":"Grid"},{"attributes":{},"id":"7c17ef47-10f6-41a9-9133-87f92e32aca7","type":"ToolEvents"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"624e28d8-af4c-42ee-8aef-da7e0e083f51","type":"Line"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"6e12749e-a130-44a6-ad29-c51d5b2f6751","type":"Line"},{"attributes":{"callback":null},"id":"e53027cb-78e5-4ffb-b6ec-41d932542a90","type":"DataRange1d"},{"attributes":{"formatter":{"id":"8117b462-d815-473e-ad7f-db45fd8cc30d","type":"BasicTickFormatter"},"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"},"ticker":{"id":"c757b087-0b27-47fb-88ad-55f21fdb61bc","type":"BasicTicker"}},"id":"4bc65242-216b-4dd2-9030-0bfe88e95ff6","type":"LinearAxis"},{"attributes":{"callback":null,"column_names":["y","x","index","foo"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"eedfd721-3bc3-47c4-bff9-bb95d5a66ab6","type":"ColumnDataSource"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"f2b9473c-7563-4e49-b42b-29576fbb9276","type":"Line"},{"attributes":{"overlay":{"id":"8edad728-5a89-4d36-8b6f-439aec38018f","type":"BoxAnnotation"},"plot":{"id":"6c433593-ef3e-4462-b90a-73564098530a","subtype":"Figure","type":"Plot"}},"id":"f0ee3acc-6cbd-40e0-9015-bc6fc45a440f","type":"BoxZoomTool"}],"root_ids":["6c433593-ef3e-4462-b90a-73564098530a"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"956c93d5-85c5-412b-a769-ed799131a654","elementid":"3711bd23-714d-4700-abf6-7417e80153df","modelid":"6c433593-ef3e-4462-b90a-73564098530a"}];
          
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