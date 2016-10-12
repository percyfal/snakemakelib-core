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
      };var element = document.getElementById("357c3f2c-f6fd-4df8-9b63-40fcaf15f58b");
      if (element == null) {
        console.log("Bokeh: ERROR: autoload.js configured with elementid '357c3f2c-f6fd-4df8-9b63-40fcaf15f58b' but no matching script tag was found. ")
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
                  var docs_json = {"5002b776-5b7c-4084-a531-04ce6af651b5":{"roots":{"references":[{"attributes":{},"id":"5d5b399e-37fb-4d1f-99b5-9646ab7a8e2c","type":"ToolEvents"},{"attributes":{"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"},"ticker":{"id":"c4006f85-6dac-40ad-9aec-79e13255490a","type":"BasicTicker"}},"id":"fb91eb41-4a9f-4e2c-a6af-85de8cf77b4e","type":"Grid"},{"attributes":{"overlay":{"id":"e475662c-12f8-44ff-81dc-3ed0fba128c5","type":"BoxAnnotation"},"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"981d858c-e18a-47fc-a9a8-73d99315ee3e","type":"BoxZoomTool"},{"attributes":{"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"10db4c5b-4c13-452f-b3bd-036bc8251520","type":"SaveTool"},{"attributes":{},"id":"c4006f85-6dac-40ad-9aec-79e13255490a","type":"BasicTicker"},{"attributes":{"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"66fb03e3-56d4-4cc2-968c-f51b15ce2f9f","type":"WheelZoomTool"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"be7727a4-2816-4195-93bb-6516383da431","type":"PanTool"},{"id":"66fb03e3-56d4-4cc2-968c-f51b15ce2f9f","type":"WheelZoomTool"},{"id":"981d858c-e18a-47fc-a9a8-73d99315ee3e","type":"BoxZoomTool"},{"id":"10db4c5b-4c13-452f-b3bd-036bc8251520","type":"SaveTool"},{"id":"eadb146b-678f-4f9c-ba2b-79bb1083c6d1","type":"ResetTool"},{"id":"50cd298e-ba92-4363-81ca-e5c0986eb494","type":"HelpTool"}]},"id":"5006236c-9047-4f2d-8726-b3d5934c5ec1","type":"Toolbar"},{"attributes":{"formatter":{"id":"bdf362a2-1007-4e4d-96ab-72baba0cfc0c","type":"BasicTickFormatter"},"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"},"ticker":{"id":"c4006f85-6dac-40ad-9aec-79e13255490a","type":"BasicTicker"}},"id":"76c7f535-bbcd-4447-a2ef-0f1b5452aef8","type":"LinearAxis"},{"attributes":{"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"eadb146b-678f-4f9c-ba2b-79bb1083c6d1","type":"ResetTool"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"x"}},"id":"a77611e3-a730-434e-bdf5-b1bb7f6e70e5","type":"Line"},{"attributes":{"dimension":1,"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"},"ticker":{"id":"201f097a-26ec-417f-b5aa-6ce7c1a38378","type":"BasicTicker"}},"id":"09861f7f-967b-407b-a04e-d4ef2cde058c","type":"Grid"},{"attributes":{"label":{"field":"x"},"renderers":[{"id":"14be820b-8177-45a2-bdb9-49f73512d8b4","type":"GlyphRenderer"}]},"id":"421189b5-54b6-4d32-9c92-1ad599d6bdcd","type":"LegendItem"},{"attributes":{"data_source":{"id":"d9c49b3d-9f31-494d-9ce9-5859171e1e87","type":"ColumnDataSource"},"glyph":{"id":"648123eb-6675-4e21-a697-737e856b55fa","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"d0353368-e723-4e3c-92b0-b59eafb901c6","type":"Line"},"selection_glyph":null},"id":"4b276736-d1f3-41f4-abd2-7b4e04d121db","type":"GlyphRenderer"},{"attributes":{"items":[{"id":"94ac638d-71e6-4db7-990c-11bb362ec8e4","type":"LegendItem"},{"id":"421189b5-54b6-4d32-9c92-1ad599d6bdcd","type":"LegendItem"}],"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"e57bbcb9-4ebe-405b-be57-b711f4ac49a5","type":"Legend"},{"attributes":{"label":{"field":"y"},"renderers":[{"id":"4b276736-d1f3-41f4-abd2-7b4e04d121db","type":"GlyphRenderer"}]},"id":"94ac638d-71e6-4db7-990c-11bb362ec8e4","type":"LegendItem"},{"attributes":{"callback":null},"id":"d74f1197-1f09-4f4b-9dac-9343456318eb","type":"DataRange1d"},{"attributes":{"data_source":{"id":"3feeec6a-31b6-40c5-acc6-9aa52f958dbf","type":"ColumnDataSource"},"glyph":{"id":"a77611e3-a730-434e-bdf5-b1bb7f6e70e5","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"527e29ca-7fe7-4a6a-8035-a0886a8bf677","type":"Line"},"selection_glyph":null},"id":"14be820b-8177-45a2-bdb9-49f73512d8b4","type":"GlyphRenderer"},{"attributes":{"below":[{"id":"76c7f535-bbcd-4447-a2ef-0f1b5452aef8","type":"LinearAxis"}],"left":[{"id":"d630fd57-0f86-4d3c-998a-4707a56c5871","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"76c7f535-bbcd-4447-a2ef-0f1b5452aef8","type":"LinearAxis"},{"id":"fb91eb41-4a9f-4e2c-a6af-85de8cf77b4e","type":"Grid"},{"id":"d630fd57-0f86-4d3c-998a-4707a56c5871","type":"LinearAxis"},{"id":"09861f7f-967b-407b-a04e-d4ef2cde058c","type":"Grid"},{"id":"e475662c-12f8-44ff-81dc-3ed0fba128c5","type":"BoxAnnotation"},{"id":"e57bbcb9-4ebe-405b-be57-b711f4ac49a5","type":"Legend"},{"id":"4b276736-d1f3-41f4-abd2-7b4e04d121db","type":"GlyphRenderer"},{"id":"14be820b-8177-45a2-bdb9-49f73512d8b4","type":"GlyphRenderer"}],"title":{"id":"51314354-3517-4d49-bd2c-8a4cc575507a","type":"Title"},"tool_events":{"id":"5d5b399e-37fb-4d1f-99b5-9646ab7a8e2c","type":"ToolEvents"},"toolbar":{"id":"5006236c-9047-4f2d-8726-b3d5934c5ec1","type":"Toolbar"},"x_range":{"id":"b9b9e61e-d303-4fb9-ada8-a5899412c339","type":"DataRange1d"},"y_range":{"id":"d74f1197-1f09-4f4b-9dac-9343456318eb","type":"DataRange1d"}},"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"},{"attributes":{},"id":"bdf362a2-1007-4e4d-96ab-72baba0cfc0c","type":"BasicTickFormatter"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"e475662c-12f8-44ff-81dc-3ed0fba128c5","type":"BoxAnnotation"},{"attributes":{},"id":"942669db-4812-4a78-9137-78a31af3499f","type":"BasicTickFormatter"},{"attributes":{"formatter":{"id":"942669db-4812-4a78-9137-78a31af3499f","type":"BasicTickFormatter"},"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"},"ticker":{"id":"201f097a-26ec-417f-b5aa-6ce7c1a38378","type":"BasicTicker"}},"id":"d630fd57-0f86-4d3c-998a-4707a56c5871","type":"LinearAxis"},{"attributes":{"callback":null},"id":"b9b9e61e-d303-4fb9-ada8-a5899412c339","type":"DataRange1d"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"x"}},"id":"527e29ca-7fe7-4a6a-8035-a0886a8bf677","type":"Line"},{"attributes":{"callback":null,"column_names":["index","x","y"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"3feeec6a-31b6-40c5-acc6-9aa52f958dbf","type":"ColumnDataSource"},{"attributes":{"callback":null,"column_names":["index","x","y"],"data":{"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"d9c49b3d-9f31-494d-9ce9-5859171e1e87","type":"ColumnDataSource"},{"attributes":{"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"648123eb-6675-4e21-a697-737e856b55fa","type":"Line"},{"attributes":{},"id":"201f097a-26ec-417f-b5aa-6ce7c1a38378","type":"BasicTicker"},{"attributes":{"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"50cd298e-ba92-4363-81ca-e5c0986eb494","type":"HelpTool"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"d0353368-e723-4e3c-92b0-b59eafb901c6","type":"Line"},{"attributes":{"plot":{"id":"ac89c3d1-b10d-4c22-957f-adaffd0062aa","subtype":"Figure","type":"Plot"}},"id":"be7727a4-2816-4195-93bb-6516383da431","type":"PanTool"},{"attributes":{"plot":null,"text":"Line plot"},"id":"51314354-3517-4d49-bd2c-8a4cc575507a","type":"Title"}],"root_ids":["ac89c3d1-b10d-4c22-957f-adaffd0062aa"]},"title":"Bokeh Application","version":"0.12.3"}};
                  var render_items = [{"docid":"5002b776-5b7c-4084-a531-04ce6af651b5","elementid":"357c3f2c-f6fd-4df8-9b63-40fcaf15f58b","modelid":"ac89c3d1-b10d-4c22-957f-adaffd0062aa"}];
                  
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