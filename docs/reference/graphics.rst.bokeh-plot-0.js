document.addEventListener("DOMContentLoaded", function(event) {
    
    (function(global) {
      function now() {
        return new Date();
      }
    
      var force = "";
    
      if (typeof (window._bokeh_onload_callbacks) === "undefined" || force !== "") {
        window._bokeh_onload_callbacks = [];
        window._bokeh_is_loading = undefined;
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
      };var element = document.getElementById("9fbca2a1-5cef-4caa-8f06-6134c1d25d27");
      if (element == null) {
        console.log("Bokeh: ERROR: autoload.js configured with elementid '9fbca2a1-5cef-4caa-8f06-6134c1d25d27' but no matching script tag was found. ")
        return false;
      }
    
      var js_urls = ['https://cdn.pydata.org/bokeh/release/bokeh-0.12.3.min.js', 'https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.3.min.js'];
    
      var inline_js = [
        function(Bokeh) {
          Bokeh.set_log_level("info");
        },
        
        function(Bokeh) {
          Bokeh.$(function() {
              Bokeh.safely(function() {
                  var docs_json = {"1f7bc428-8ce8-415e-a32b-48afb9267c2a":{"roots":{"references":[{"attributes":{"dimension":1,"grid_line_color":{"value":"black"},"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"5e349e27-277c-486d-b9fa-13af84a701e1","type":"BasicTicker"}},"id":"ba5162aa-843c-4381-ac2b-79d886d0e76e","type":"Grid"},{"attributes":{"callback":null},"id":"d042ccfd-582d-458d-903a-23707de5ad06","type":"DataRange1d"},{"attributes":{},"id":"0560911c-dd25-4576-8295-f4e5a3e62f88","type":"BasicTickFormatter"},{"attributes":{"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"}},"id":"88663fba-cff4-4b41-bd25-fb5cfe424a8b","type":"ResetTool"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"d2c67763-f237-4d96-8b0f-3e8f622ce44c","type":"PanTool"},{"id":"305a02dd-ac39-4ae7-b3b4-a77a173b5bb1","type":"WheelZoomTool"},{"id":"e0a29531-1c1e-4fc1-b993-c673e95d059a","type":"BoxZoomTool"},{"id":"e6029bcd-1084-4b12-8b0a-2a653d11219c","type":"SaveTool"},{"id":"88663fba-cff4-4b41-bd25-fb5cfe424a8b","type":"ResetTool"},{"id":"d0f4b895-40e4-448d-81ed-552cb7eea9be","type":"HelpTool"}]},"id":"11e3d92c-2e81-4f94-8d20-00128e82b7dd","type":"Toolbar"},{"attributes":{"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"}},"id":"305a02dd-ac39-4ae7-b3b4-a77a173b5bb1","type":"WheelZoomTool"},{"attributes":{"callback":null,"column_names":["index","x","y"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"96f8edee-9eba-4e60-ae4c-c0c0bdb3e665","type":"ColumnDataSource"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"e4dee79d-e346-4bb0-b048-303e1616b487","type":"Circle"},{"attributes":{},"id":"782fda21-22b9-4503-b76c-dae4b3a8cd14","type":"BasicTicker"},{"attributes":{"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"}},"id":"e6029bcd-1084-4b12-8b0a-2a653d11219c","type":"SaveTool"},{"attributes":{"axis_label":"x","formatter":{"id":"0560911c-dd25-4576-8295-f4e5a3e62f88","type":"BasicTickFormatter"},"major_label_orientation":1.0471975511965976,"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"782fda21-22b9-4503-b76c-dae4b3a8cd14","type":"BasicTicker"}},"id":"31995b0b-2b5d-4161-ac51-7069af3a239e","type":"LinearAxis"},{"attributes":{"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"}},"id":"d2c67763-f237-4d96-8b0f-3e8f622ce44c","type":"PanTool"},{"attributes":{"below":[{"id":"31995b0b-2b5d-4161-ac51-7069af3a239e","type":"LinearAxis"}],"left":[{"id":"a87af0bf-8055-41f1-9668-3ab5bcdd1cde","type":"LinearAxis"}],"plot_height":300,"plot_width":300,"renderers":[{"id":"31995b0b-2b5d-4161-ac51-7069af3a239e","type":"LinearAxis"},{"id":"01aa8006-8f1d-4274-90a3-d7828bcda889","type":"Grid"},{"id":"a87af0bf-8055-41f1-9668-3ab5bcdd1cde","type":"LinearAxis"},{"id":"ba5162aa-843c-4381-ac2b-79d886d0e76e","type":"Grid"},{"id":"4ed7130c-6d2f-468b-8bdc-1fc3d056c177","type":"BoxAnnotation"},{"id":"a049f79c-6164-4e7a-9fba-1d8c51df62da","type":"GlyphRenderer"},{"id":"bc38870d-4463-4d89-8de1-5d9427fb5cc8","type":"GlyphRenderer"}],"title":{"id":"38b8ed3e-b712-461c-84e5-bdb46cddc2af","type":"Title"},"tool_events":{"id":"ee979d9d-2afc-48a2-b52c-84776f2c84f4","type":"ToolEvents"},"toolbar":{"id":"11e3d92c-2e81-4f94-8d20-00128e82b7dd","type":"Toolbar"},"x_range":{"id":"d042ccfd-582d-458d-903a-23707de5ad06","type":"DataRange1d"},"y_range":{"id":"29ba8bd8-45eb-427a-90ac-5c0f63960201","type":"DataRange1d"}},"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"5e349e27-277c-486d-b9fa-13af84a701e1","type":"BasicTicker"},{"attributes":{"data_source":{"id":"96f8edee-9eba-4e60-ae4c-c0c0bdb3e665","type":"ColumnDataSource"},"glyph":{"id":"6f0b896c-c662-4a19-aaaa-98fcfa4eeb9a","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"71ed5123-d7e7-482c-821f-72c6ae62599a","type":"Circle"},"selection_glyph":null},"id":"a049f79c-6164-4e7a-9fba-1d8c51df62da","type":"GlyphRenderer"},{"attributes":{"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"}},"id":"d0f4b895-40e4-448d-81ed-552cb7eea9be","type":"HelpTool"},{"attributes":{"fill_color":{"value":"red"},"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"6f0b896c-c662-4a19-aaaa-98fcfa4eeb9a","type":"Circle"},{"attributes":{"callback":null},"id":"29ba8bd8-45eb-427a-90ac-5c0f63960201","type":"DataRange1d"},{"attributes":{"axis_label":null,"axis_line_color":{"value":null},"formatter":{"id":"c50bf510-4e7c-486b-bc35-3766c93bb685","type":"BasicTickFormatter"},"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"5e349e27-277c-486d-b9fa-13af84a701e1","type":"BasicTicker"}},"id":"a87af0bf-8055-41f1-9668-3ab5bcdd1cde","type":"LinearAxis"},{"attributes":{"data_source":{"id":"ac2f1cf4-1f25-4d51-96b6-78c5916023d3","type":"ColumnDataSource"},"glyph":{"id":"57ae4fa8-0ac1-4689-90a5-f21290bc90db","type":"Circle"},"hover_glyph":null,"nonselection_glyph":{"id":"e4dee79d-e346-4bb0-b048-303e1616b487","type":"Circle"},"selection_glyph":null},"id":"bc38870d-4463-4d89-8de1-5d9427fb5cc8","type":"GlyphRenderer"},{"attributes":{"overlay":{"id":"4ed7130c-6d2f-468b-8bdc-1fc3d056c177","type":"BoxAnnotation"},"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"}},"id":"e0a29531-1c1e-4fc1-b993-c673e95d059a","type":"BoxZoomTool"},{"attributes":{"callback":null,"column_names":["index","x","y"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"ac2f1cf4-1f25-4d51-96b6-78c5916023d3","type":"ColumnDataSource"},{"attributes":{"plot":null,"text":"My plot"},"id":"38b8ed3e-b712-461c-84e5-bdb46cddc2af","type":"Title"},{"attributes":{},"id":"ee979d9d-2afc-48a2-b52c-84776f2c84f4","type":"ToolEvents"},{"attributes":{"fill_color":{"value":"#1f77b4"},"line_color":{"value":"#1f77b4"},"x":{"field":"y"},"y":{"field":"x"}},"id":"57ae4fa8-0ac1-4689-90a5-f21290bc90db","type":"Circle"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"71ed5123-d7e7-482c-821f-72c6ae62599a","type":"Circle"},{"attributes":{},"id":"c50bf510-4e7c-486b-bc35-3766c93bb685","type":"BasicTickFormatter"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"4ed7130c-6d2f-468b-8bdc-1fc3d056c177","type":"BoxAnnotation"},{"attributes":{"grid_line_color":{"value":"black"},"plot":{"id":"951dfe57-0ed0-4347-a42b-1ef0334a21d7","subtype":"Figure","type":"Plot"},"ticker":{"id":"782fda21-22b9-4503-b76c-dae4b3a8cd14","type":"BasicTicker"}},"id":"01aa8006-8f1d-4274-90a3-d7828bcda889","type":"Grid"}],"root_ids":["951dfe57-0ed0-4347-a42b-1ef0334a21d7"]},"title":"Bokeh Application","version":"0.12.3"}};
                  var render_items = [{"docid":"1f7bc428-8ce8-415e-a32b-48afb9267c2a","elementid":"9fbca2a1-5cef-4caa-8f06-6134c1d25d27","modelid":"951dfe57-0ed0-4347-a42b-1ef0334a21d7"}];
                  
                  Bokeh.embed.embed_items(docs_json, render_items);
              });
          });
        },
        function(Bokeh) {
          console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-0.12.3.min.css");
          Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-0.12.3.min.css");
          console.log("Bokeh: injecting CSS: https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.3.min.css");
          Bokeh.embed.inject_css("https://cdn.pydata.org/bokeh/release/bokeh-widgets-0.12.3.min.css");
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
});