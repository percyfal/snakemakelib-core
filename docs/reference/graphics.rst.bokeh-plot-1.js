
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
  };var element = document.getElementById("af8f73e9-58d3-4d5b-a098-72f22b2f38a8");
  if (element == null) {
    console.log("Bokeh: ERROR: autoload.js configured with elementid 'af8f73e9-58d3-4d5b-a098-72f22b2f38a8' but no matching script tag was found. ")
    return false;
  }

  var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.11.1.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-compiler-0.11.1.min.js'];

  var inline_js = [
    function(Bokeh) {
      Bokeh.set_log_level("info");
    },
    
    function(Bokeh) {
      Bokeh.$(function() {
          var docs_json = {"68f797fd-d823-4337-9f94-d952a0effaba":{"roots":{"references":[{"attributes":{"callback":null},"id":"2e730fc9-539f-4aa5-9374-776b2a999b3d","type":"DataRange1d"},{"attributes":{"dimension":1,"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"},"ticker":{"id":"e8d8eb3d-1d66-460e-9009-3fd3b1098609","type":"BasicTicker"}},"id":"06565a0c-3673-40fd-aa00-152b7f800a26","type":"Grid"},{"attributes":{"data_source":{"id":"8247ebaf-58ba-46a1-93ae-0d6d799c8693","type":"ColumnDataSource"},"glyph":{"id":"018f1c26-22a1-4519-b257-ef84fec7fd6e","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"f4e3b18a-f5a0-473b-af34-7ad423bc9b46","type":"Line"},"selection_glyph":null},"id":"a0cd80b0-92ff-40c9-8ee3-743b94196faa","type":"GlyphRenderer"},{"attributes":{"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"018f1c26-22a1-4519-b257-ef84fec7fd6e","type":"Line"},{"attributes":{"below":[{"id":"abe577fa-7159-40ab-aef3-6ad19927711d","type":"LinearAxis"}],"left":[{"id":"8b8de558-489a-498b-949d-d2269243e9a6","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"abe577fa-7159-40ab-aef3-6ad19927711d","type":"LinearAxis"},{"id":"6b53dc97-fdd4-4e08-b7a0-fb495fdd81be","type":"Grid"},{"id":"8b8de558-489a-498b-949d-d2269243e9a6","type":"LinearAxis"},{"id":"06565a0c-3673-40fd-aa00-152b7f800a26","type":"Grid"},{"id":"decc3a57-9e62-47ec-b56f-3b26a0ba7feb","type":"BoxAnnotation"},{"id":"28b0d428-5051-4d4b-893c-4de6bb8b29b8","type":"Legend"},{"id":"a0cd80b0-92ff-40c9-8ee3-743b94196faa","type":"GlyphRenderer"},{"id":"92a3bcc9-5e52-4c93-ac55-317df8459360","type":"GlyphRenderer"}],"title":"Line plot","tool_events":{"id":"604b4032-542f-4f78-9d1a-fe01f9a0a88e","type":"ToolEvents"},"tools":[{"id":"25548359-bc15-4931-a30b-70d39370023f","type":"PanTool"},{"id":"93654178-2845-48fd-a448-215ec2041b9d","type":"WheelZoomTool"},{"id":"7b52bb51-9779-4536-bf83-3b90616c0249","type":"BoxZoomTool"},{"id":"1740bba9-4f59-4ddb-a464-f8937b800ef7","type":"PreviewSaveTool"},{"id":"d2928a41-c83b-469a-9ee7-7ffe58721616","type":"ResizeTool"},{"id":"49ce0a63-91d5-4ddf-a542-c121eebadb2b","type":"ResetTool"},{"id":"5f352eab-4762-4872-90ce-e84314b6570f","type":"HelpTool"}],"x_range":{"id":"a2f4a962-8990-4f01-a3b3-6cf4bdb7f303","type":"DataRange1d"},"y_range":{"id":"2e730fc9-539f-4aa5-9374-776b2a999b3d","type":"DataRange1d"}},"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"x"}},"id":"ba9b56f5-8add-4ab2-a085-09f140b1866f","type":"Line"},{"attributes":{"formatter":{"id":"9c1097b7-9325-4afc-8a4b-7f51d7934326","type":"BasicTickFormatter"},"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"},"ticker":{"id":"e8d8eb3d-1d66-460e-9009-3fd3b1098609","type":"BasicTicker"}},"id":"8b8de558-489a-498b-949d-d2269243e9a6","type":"LinearAxis"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"25548359-bc15-4931-a30b-70d39370023f","type":"PanTool"},{"attributes":{"callback":null},"id":"a2f4a962-8990-4f01-a3b3-6cf4bdb7f303","type":"DataRange1d"},{"attributes":{},"id":"48f091c5-2dc2-4b1f-8f7d-c3adb3764750","type":"BasicTickFormatter"},{"attributes":{},"id":"9c1097b7-9325-4afc-8a4b-7f51d7934326","type":"BasicTickFormatter"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"1740bba9-4f59-4ddb-a464-f8937b800ef7","type":"PreviewSaveTool"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"decc3a57-9e62-47ec-b56f-3b26a0ba7feb","type":"BoxAnnotation"},{"attributes":{"legends":[["y",[{"id":"a0cd80b0-92ff-40c9-8ee3-743b94196faa","type":"GlyphRenderer"}]],["x",[{"id":"92a3bcc9-5e52-4c93-ac55-317df8459360","type":"GlyphRenderer"}]]],"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"28b0d428-5051-4d4b-893c-4de6bb8b29b8","type":"Legend"},{"attributes":{},"id":"fa6523f3-5b68-48cc-aaed-e1b956c2bf1b","type":"BasicTicker"},{"attributes":{},"id":"604b4032-542f-4f78-9d1a-fe01f9a0a88e","type":"ToolEvents"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"49ce0a63-91d5-4ddf-a542-c121eebadb2b","type":"ResetTool"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"fa95f38b-db2a-4d3c-8734-514bfc2cdf14","type":"ColumnDataSource"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"93654178-2845-48fd-a448-215ec2041b9d","type":"WheelZoomTool"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"d2928a41-c83b-469a-9ee7-7ffe58721616","type":"ResizeTool"},{"attributes":{"callback":null,"column_names":["y","x","index"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"8247ebaf-58ba-46a1-93ae-0d6d799c8693","type":"ColumnDataSource"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"x"}},"id":"7268f0a5-388c-4478-b687-46d4647c059a","type":"Line"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"f4e3b18a-f5a0-473b-af34-7ad423bc9b46","type":"Line"},{"attributes":{"formatter":{"id":"48f091c5-2dc2-4b1f-8f7d-c3adb3764750","type":"BasicTickFormatter"},"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"},"ticker":{"id":"fa6523f3-5b68-48cc-aaed-e1b956c2bf1b","type":"BasicTicker"}},"id":"abe577fa-7159-40ab-aef3-6ad19927711d","type":"LinearAxis"},{"attributes":{"overlay":{"id":"decc3a57-9e62-47ec-b56f-3b26a0ba7feb","type":"BoxAnnotation"},"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"7b52bb51-9779-4536-bf83-3b90616c0249","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"},"ticker":{"id":"fa6523f3-5b68-48cc-aaed-e1b956c2bf1b","type":"BasicTicker"}},"id":"6b53dc97-fdd4-4e08-b7a0-fb495fdd81be","type":"Grid"},{"attributes":{},"id":"e8d8eb3d-1d66-460e-9009-3fd3b1098609","type":"BasicTicker"},{"attributes":{"plot":{"id":"2cd294a6-0baf-40c3-9254-512f52307944","subtype":"Figure","type":"Plot"}},"id":"5f352eab-4762-4872-90ce-e84314b6570f","type":"HelpTool"},{"attributes":{"data_source":{"id":"fa95f38b-db2a-4d3c-8734-514bfc2cdf14","type":"ColumnDataSource"},"glyph":{"id":"7268f0a5-388c-4478-b687-46d4647c059a","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"ba9b56f5-8add-4ab2-a085-09f140b1866f","type":"Line"},"selection_glyph":null},"id":"92a3bcc9-5e52-4c93-ac55-317df8459360","type":"GlyphRenderer"}],"root_ids":["2cd294a6-0baf-40c3-9254-512f52307944"]},"title":"Bokeh Application","version":"0.11.1"}};
          var render_items = [{"docid":"68f797fd-d823-4337-9f94-d952a0effaba","elementid":"af8f73e9-58d3-4d5b-a098-72f22b2f38a8","modelid":"2cd294a6-0baf-40c3-9254-512f52307944"}];
          
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