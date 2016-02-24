
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
  };var element = document.getElementById("2492ec44-7025-42df-a5ff-157926e03182");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid '2492ec44-7025-42df-a5ff-157926e03182' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"c26679e5-88bb-441e-863c-afc6369a4ec3":{"roots":{"references":[{"attributes":{},"id":"336a4968-ada6-4bd2-a14a-23787e18eb83","type":"BasicTickFormatter"},{"attributes":{"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"a6ff0a4f-ef99-476b-ace1-a45cad2e1b68","type":"WheelZoomTool"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"05f38970-7d27-494b-96a4-59a8c59731ff","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"af1c0dc5-b0b8-4705-a8f4-e77e3ded05bc","type":"ResetTool"},{"attributes":{"callback":null},"id":"b0c9df02-1f99-419c-92ce-2609459abcdd","type":"DataRange1d"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"ac39dd5c-b48b-45f0-a131-aab9ea4249aa","type":"ColumnDataSource"},{"attributes":{"below":[{"id":"9196109c-75ef-4dcd-a15b-97d12f2bd416","type":"LinearAxis"}],"left":[{"id":"a08d3170-d019-4994-a79b-9b5c7424e19a","type":"LinearAxis"}],"plot_height":300,"plot_width":300,"renderers":[{"id":"9196109c-75ef-4dcd-a15b-97d12f2bd416","type":"LinearAxis"},{"id":"8964f369-0551-422c-972a-b071ab556d45","type":"Grid"},{"id":"a08d3170-d019-4994-a79b-9b5c7424e19a","type":"LinearAxis"},{"id":"7c232cf5-80f6-4e33-8a6c-358c1a57ab6b","type":"Grid"},{"id":"21e444e4-c46c-4733-b600-bfb2bf5e68f0","type":"BoxAnnotation"},{"id":"965906ae-d397-41c9-8672-9287e54043bc","type":"GlyphRenderer"},{"id":"0e60330c-7156-4fa3-98bb-750675cd1ccc","type":"GlyphRenderer"}],"title":"My plot","title_text_color":{"value":"olive"},"title_text_font":"times","title_text_font_style":"italic","tool_events":{"id":"f2e5f05a-9ae8-418a-9bfb-d0d5ab2dbbb2","type":"ToolEvents"},"tools":[{"id":"5aa62cf0-6eee-4984-b356-84cffbc76f31","type":"PanTool"},{"id":"a6ff0a4f-ef99-476b-ace1-a45cad2e1b68","type":"WheelZoomTool"},{"id":"f3d88422-a62e-4d78-a3f4-76c222039ffe","type":"BoxZoomTool"},{"id":"27aee46a-cd66-405a-b262-92d26c8d77f9","type":"PreviewSaveTool"},{"id":"65909602-fe75-41fe-b3f8-9e558faf12df","type":"ResizeTool"},{"id":"af1c0dc5-b0b8-4705-a8f4-e77e3ded05bc","type":"ResetTool"},{"id":"27c2630d-7a11-498e-9bc8-f72ed8562588","type":"HelpTool"}],"x_range":{"id":"9886d3f4-872a-4d65-8a85-8d01b2ee2988","type":"DataRange1d"},"y_range":{"id":"b0c9df02-1f99-419c-92ce-2609459abcdd","type":"DataRange1d"}},"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"},{"attributes":{"dimension":1,"grid_line_color":{"value":"black"},"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"},"ticker":{"id":"dc1badc1-ecc8-42f1-8aad-a38546147e93","type":"BasicTicker"}},"id":"7c232cf5-80f6-4e33-8a6c-358c1a57ab6b","type":"Grid"},{"attributes":{},"id":"dc1badc1-ecc8-42f1-8aad-a38546147e93","type":"BasicTicker"},{"attributes":{},"id":"e5f149c0-656d-4170-be36-4d343ef359ec","type":"BasicTicker"},{"attributes":{"data_source":{"id":"05f38970-7d27-494b-96a4-59a8c59731ff","type":"ColumnDataSource"},"glyph":{"id":"177adda6-88d8-400a-b993-8770713e930a","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"ed00bf5a-dad1-4b7b-bb35-0dbf775057c3","type":"Circle"},"selection_glyph":null},"id":"965906ae-d397-41c9-8672-9287e54043bc","type":"GlyphRenderer"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"d3ffbc16-2e59-4822-a1e1-ec999fe56e5c","type":"Circle"},{"attributes":{"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"27aee46a-cd66-405a-b262-92d26c8d77f9","type":"PreviewSaveTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"21e444e4-c46c-4733-b600-bfb2bf5e68f0","type":"BoxAnnotation"},{"attributes":{"fill_color":{"value":"red"},"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"177adda6-88d8-400a-b993-8770713e930a","type":"Circle"},{"attributes":{"data_source":{"id":"ac39dd5c-b48b-45f0-a131-aab9ea4249aa","type":"ColumnDataSource"},"glyph":{"id":"d3ffbc16-2e59-4822-a1e1-ec999fe56e5c","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"4d242275-203b-4707-b576-a06f430baf97","type":"Circle"},"selection_glyph":null},"id":"0e60330c-7156-4fa3-98bb-750675cd1ccc","type":"GlyphRenderer"},{"attributes":{},"id":"f2e5f05a-9ae8-418a-9bfb-d0d5ab2dbbb2","type":"ToolEvents"},{"attributes":{"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"27c2630d-7a11-498e-9bc8-f72ed8562588","type":"HelpTool"},{"attributes":{"callback":null},"id":"9886d3f4-872a-4d65-8a85-8d01b2ee2988","type":"DataRange1d"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"ed00bf5a-dad1-4b7b-bb35-0dbf775057c3","type":"Circle"},{"attributes":{"grid_line_color":{"value":"black"},"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"},"ticker":{"id":"e5f149c0-656d-4170-be36-4d343ef359ec","type":"BasicTicker"}},"id":"8964f369-0551-422c-972a-b071ab556d45","type":"Grid"},{"attributes":{"axis_label":null,"axis_line_color":{"value":null},"formatter":{"id":"336a4968-ada6-4bd2-a14a-23787e18eb83","type":"BasicTickFormatter"},"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"},"ticker":{"id":"dc1badc1-ecc8-42f1-8aad-a38546147e93","type":"BasicTicker"}},"id":"a08d3170-d019-4994-a79b-9b5c7424e19a","type":"LinearAxis"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"4d242275-203b-4707-b576-a06f430baf97","type":"Circle"},{"attributes":{"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"5aa62cf0-6eee-4984-b356-84cffbc76f31","type":"PanTool"},{"attributes":{"overlay":{"id":"21e444e4-c46c-4733-b600-bfb2bf5e68f0","type":"BoxAnnotation"},"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"f3d88422-a62e-4d78-a3f4-76c222039ffe","type":"BoxZoomTool"},{"attributes":{},"id":"c58ab580-00d7-457a-8c27-feb847564e70","type":"BasicTickFormatter"},{"attributes":{"axis_label":"x","formatter":{"id":"c58ab580-00d7-457a-8c27-feb847564e70","type":"BasicTickFormatter"},"major_label_orientation":1.0471975511965976,"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"},"ticker":{"id":"e5f149c0-656d-4170-be36-4d343ef359ec","type":"BasicTicker"}},"id":"9196109c-75ef-4dcd-a15b-97d12f2bd416","type":"LinearAxis"},{"attributes":{"plot":{"id":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b","subtype":"Figure","type":"Plot"}},"id":"65909602-fe75-41fe-b3f8-9e558faf12df","type":"ResizeTool"}],"root_ids":["d4a8fa93-19da-49f6-b905-4fc0683b5b1b"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"c26679e5-88bb-441e-863c-afc6369a4ec3","elementid":"2492ec44-7025-42df-a5ff-157926e03182","modelid":"d4a8fa93-19da-49f6-b905-4fc0683b5b1b"}];
          
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