
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
  };var element = document.getElementById("b8276027-9fa0-4821-9f51-fb71a57fa946");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid 'b8276027-9fa0-4821-9f51-fb71a57fa946' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"3d73f29a-b32f-4d27-925f-6fda2142a874":{"roots":{"references":[{"attributes":{"grid_line_color":{"value":"black"},"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"64c54c5a-b3c0-496a-a81a-c1fe34378995","type":"BasicTicker"}},"id":"8c03a7fc-0c55-4faf-9039-364c110a0d21","type":"Grid"},{"attributes":{"dimension":1,"grid_line_color":{"value":"black"},"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"dfa37113-102e-478a-bf42-54d70fe72367","type":"BasicTicker"}},"id":"b9252ae8-7ca6-4afa-8607-2e10b238bb1c","type":"Grid"},{"attributes":{},"id":"7c3450c3-1f14-40a5-9c2d-9c630e190533","type":"BasicTickFormatter"},{"attributes":{"fill_color":{"value":"red"},"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"e1b36507-983a-427e-ada6-378b6630615f","type":"Circle"},{"attributes":{"overlay":{"id":"e9a7c914-aeb6-42ac-b7c4-6315878e32af","type":"BoxAnnotation"},"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"153e321e-ffe8-44a9-b475-8709f64d67ed","type":"BoxZoomTool"},{"attributes":{"axis_label":"x","formatter":{"id":"c32f4889-7120-44ac-8c44-c8e4a06e7780","type":"BasicTickFormatter"},"major_label_orientation":1.0471975511965976,"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"64c54c5a-b3c0-496a-a81a-c1fe34378995","type":"BasicTicker"}},"id":"6dcc7ea6-440a-4dcf-8045-fa42eaed563e","type":"LinearAxis"},{"attributes":{},"id":"64c54c5a-b3c0-496a-a81a-c1fe34378995","type":"BasicTicker"},{"attributes":{"data_source":{"id":"6594ffc8-b963-47ef-b20b-4e3cda3762d6","type":"ColumnDataSource"},"glyph":{"id":"4980937f-0cda-456a-9981-c18c3ce82db6","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"61a09144-55d7-4835-9c8f-dfad4a6ee077","type":"Circle"},"selection_glyph":null},"id":"9df37742-1afe-49e7-bc6d-5547506c5195","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"793c4aa1-8216-4e9a-9efc-96f2a7b801de","type":"ResizeTool"},{"attributes":{"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"b103d11d-2c3d-4ff2-bd9f-5d1244216f32","type":"WheelZoomTool"},{"attributes":{"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"8844cf9f-8576-46d0-ba41-efb305d29945","type":"PreviewSaveTool"},{"attributes":{"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"16734baa-cfd7-4052-9d5b-d80d72967936","type":"PanTool"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"6594ffc8-b963-47ef-b20b-4e3cda3762d6","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"af8a1824-5a97-41ce-bff2-0ffd32dd7d03","type":"ResetTool"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"93667df9-5ebb-4dbb-aa70-773c38847ef4","type":"Circle"},{"attributes":{"callback":null},"id":"52e618a8-f2c9-4412-9c82-149c656dba5e","type":"DataRange1d"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"61a09144-55d7-4835-9c8f-dfad4a6ee077","type":"Circle"},{"attributes":{},"id":"dfa37113-102e-478a-bf42-54d70fe72367","type":"BasicTicker"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"4980937f-0cda-456a-9981-c18c3ce82db6","type":"Circle"},{"attributes":{},"id":"c32f4889-7120-44ac-8c44-c8e4a06e7780","type":"BasicTickFormatter"},{"attributes":{"axis_label":null,"axis_line_color":{"value":null},"formatter":{"id":"7c3450c3-1f14-40a5-9c2d-9c630e190533","type":"BasicTickFormatter"},"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"dfa37113-102e-478a-bf42-54d70fe72367","type":"BasicTicker"}},"id":"5cc7f17f-0f43-4443-bb22-295168212dbe","type":"LinearAxis"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"6aea9867-65c9-437d-97b8-d84979b77281","type":"ColumnDataSource"},{"attributes":{"below":[{"id":"6dcc7ea6-440a-4dcf-8045-fa42eaed563e","type":"LinearAxis"}],"left":[{"id":"5cc7f17f-0f43-4443-bb22-295168212dbe","type":"LinearAxis"}],"plot_height":300,"plot_width":300,"renderers":[{"id":"6dcc7ea6-440a-4dcf-8045-fa42eaed563e","type":"LinearAxis"},{"id":"8c03a7fc-0c55-4faf-9039-364c110a0d21","type":"Grid"},{"id":"5cc7f17f-0f43-4443-bb22-295168212dbe","type":"LinearAxis"},{"id":"b9252ae8-7ca6-4afa-8607-2e10b238bb1c","type":"Grid"},{"id":"e9a7c914-aeb6-42ac-b7c4-6315878e32af","type":"BoxAnnotation"},{"id":"d33517d5-69dc-4b05-ac34-560fd39a3faf","type":"GlyphRenderer"},{"id":"9df37742-1afe-49e7-bc6d-5547506c5195","type":"GlyphRenderer"}],"title":"My plot","title_text_color":{"value":"olive"},"title_text_font":"times","title_text_font_style":"italic","tool_events":{"id":"184bdcb2-04d3-4c90-947c-65399749cade","type":"ToolEvents"},"tools":[{"id":"16734baa-cfd7-4052-9d5b-d80d72967936","type":"PanTool"},{"id":"b103d11d-2c3d-4ff2-bd9f-5d1244216f32","type":"WheelZoomTool"},{"id":"153e321e-ffe8-44a9-b475-8709f64d67ed","type":"BoxZoomTool"},{"id":"8844cf9f-8576-46d0-ba41-efb305d29945","type":"PreviewSaveTool"},{"id":"793c4aa1-8216-4e9a-9efc-96f2a7b801de","type":"ResizeTool"},{"id":"af8a1824-5a97-41ce-bff2-0ffd32dd7d03","type":"ResetTool"},{"id":"c17b63ae-88f1-4466-9a1d-821267ab2c8e","type":"HelpTool"}],"x_range":{"id":"28781bdc-83fc-4dd8-baa2-246a82b57104","type":"DataRange1d"},"y_range":{"id":"52e618a8-f2c9-4412-9c82-149c656dba5e","type":"DataRange1d"}},"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"e9a7c914-aeb6-42ac-b7c4-6315878e32af","type":"BoxAnnotation"},{"attributes":{"data_source":{"id":"6aea9867-65c9-437d-97b8-d84979b77281","type":"ColumnDataSource"},"glyph":{"id":"e1b36507-983a-427e-ada6-378b6630615f","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"93667df9-5ebb-4dbb-aa70-773c38847ef4","type":"Circle"},"selection_glyph":null},"id":"d33517d5-69dc-4b05-ac34-560fd39a3faf","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"923e1a2b-7967-46ed-9c30-37f24c9914d7","subtype":"Figure","type":"Plot"}},"id":"c17b63ae-88f1-4466-9a1d-821267ab2c8e","type":"HelpTool"},{"attributes":{"callback":null},"id":"28781bdc-83fc-4dd8-baa2-246a82b57104","type":"DataRange1d"},{"attributes":{},"id":"184bdcb2-04d3-4c90-947c-65399749cade","type":"ToolEvents"}],"root_ids":["923e1a2b-7967-46ed-9c30-37f24c9914d7"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"3d73f29a-b32f-4d27-925f-6fda2142a874","elementid":"b8276027-9fa0-4821-9f51-fb71a57fa946","modelid":"923e1a2b-7967-46ed-9c30-37f24c9914d7"}];
          
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