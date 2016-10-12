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
      };var element = document.getElementById("348d65ef-c653-425e-9c9a-921b1fbd742a");
      if (element == null) {
        console.log("Bokeh: ERROR: autoload.js configured with elementid '348d65ef-c653-425e-9c9a-921b1fbd742a' but no matching script tag was found. ")
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
                  var docs_json = {"a9c32d1d-f23e-4de4-ae7d-b9b1f65a304f":{"roots":{"references":[{"attributes":{"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"6ed84777-0a5f-4d3e-bf60-b858c6110755","type":"PanTool"},{"attributes":{"below":[{"id":"8243d156-0bd0-4e3a-bb66-b6ec40ef6001","type":"LinearAxis"}],"left":[{"id":"c8cbcfde-385d-456c-9ba6-3fc2f3274f8d","type":"LinearAxis"}],"plot_height":400,"plot_width":400,"renderers":[{"id":"8243d156-0bd0-4e3a-bb66-b6ec40ef6001","type":"LinearAxis"},{"id":"31ab76bb-bb8d-48c0-a6f3-7e51f5d8c937","type":"Grid"},{"id":"c8cbcfde-385d-456c-9ba6-3fc2f3274f8d","type":"LinearAxis"},{"id":"47590510-df47-453d-9b04-7e4a2b52f87b","type":"Grid"},{"id":"111ce224-9a2f-48ce-af2a-05af240ca475","type":"BoxAnnotation"},{"id":"54eeeeea-affb-4c7f-a2a5-8820503a7a0d","type":"Legend"},{"id":"dbaa2aa7-1d89-4eec-a0ba-64a9fe430f16","type":"GlyphRenderer"},{"id":"ae002b3a-24b8-4018-acf7-6612df6d94e7","type":"GlyphRenderer"}],"title":{"id":"b3041a16-58cd-47b4-a97a-099cfe2e8b75","type":"Title"},"tool_events":{"id":"aab283df-db28-4c6b-93d3-276ad0ce32af","type":"ToolEvents"},"toolbar":{"id":"824c7c68-6e51-4d79-9a19-9f2efd7c1319","type":"Toolbar"},"x_range":{"id":"eeac9d00-7caf-4a46-bd3f-528a1c81f9d3","type":"DataRange1d"},"y_range":{"id":"219136f0-0a8b-428e-90bd-c59deb174ec0","type":"DataRange1d"}},"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"},{"attributes":{"data_source":{"id":"b2eec34d-3934-49e4-b063-116ba7f8367c","type":"ColumnDataSource"},"glyph":{"id":"fc8190fd-7555-46b4-93d5-8525ce25d2ce","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"26f755bf-8fb6-4ef8-a640-89f9bf66360f","type":"Line"},"selection_glyph":null},"id":"dbaa2aa7-1d89-4eec-a0ba-64a9fe430f16","type":"GlyphRenderer"},{"attributes":{"formatter":{"id":"cfb24dfa-eb32-4d23-b3f1-9c4418251e44","type":"BasicTickFormatter"},"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"},"ticker":{"id":"62617dbf-6403-429f-9f35-7624046562a5","type":"BasicTicker"}},"id":"c8cbcfde-385d-456c-9ba6-3fc2f3274f8d","type":"LinearAxis"},{"attributes":{"overlay":{"id":"111ce224-9a2f-48ce-af2a-05af240ca475","type":"BoxAnnotation"},"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"d3921f73-7e0a-4253-a9a6-16dfb59ca66a","type":"BoxZoomTool"},{"attributes":{"line_color":{"value":"red"},"x":{"field":"x"},"y":{"field":"y"}},"id":"fc8190fd-7555-46b4-93d5-8525ce25d2ce","type":"Line"},{"attributes":{"bottom_units":"screen","fill_alpha":{"value":0.5},"fill_color":{"value":"lightgrey"},"left_units":"screen","level":"overlay","line_alpha":{"value":1.0},"line_color":{"value":"black"},"line_dash":[4,4],"line_width":{"value":2},"plot":null,"render_mode":"css","right_units":"screen","top_units":"screen"},"id":"111ce224-9a2f-48ce-af2a-05af240ca475","type":"BoxAnnotation"},{"attributes":{"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"},"ticker":{"id":"1523aa38-2563-471c-ba68-fb99e78d9d5a","type":"BasicTicker"}},"id":"31ab76bb-bb8d-48c0-a6f3-7e51f5d8c937","type":"Grid"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"0d3b6cd6-798d-4ec3-ad10-6463112d9e53","type":"Line"},{"attributes":{},"id":"cfb24dfa-eb32-4d23-b3f1-9c4418251e44","type":"BasicTickFormatter"},{"attributes":{"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"6ab96d89-a1dc-4765-940c-a8d1228dc3d2","type":"WheelZoomTool"},{"attributes":{"data_source":{"id":"ffa7dbbc-53f4-497a-977b-5220bf231f2e","type":"ColumnDataSource"},"glyph":{"id":"3c410111-828c-478c-b376-cc2dcafdfbe4","type":"Line"},"hover_glyph":null,"nonselection_glyph":{"id":"0d3b6cd6-798d-4ec3-ad10-6463112d9e53","type":"Line"},"selection_glyph":null},"id":"ae002b3a-24b8-4018-acf7-6612df6d94e7","type":"GlyphRenderer"},{"attributes":{"plot":null,"text":"Line plot"},"id":"b3041a16-58cd-47b4-a97a-099cfe2e8b75","type":"Title"},{"attributes":{"callback":null},"id":"219136f0-0a8b-428e-90bd-c59deb174ec0","type":"DataRange1d"},{"attributes":{},"id":"62617dbf-6403-429f-9f35-7624046562a5","type":"BasicTicker"},{"attributes":{"formatter":{"id":"d351e06e-e2b6-4977-8906-2528d26b8cd6","type":"BasicTickFormatter"},"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"},"ticker":{"id":"1523aa38-2563-471c-ba68-fb99e78d9d5a","type":"BasicTicker"}},"id":"8243d156-0bd0-4e3a-bb66-b6ec40ef6001","type":"LinearAxis"},{"attributes":{"label":{"field":"y"},"renderers":[{"id":"dbaa2aa7-1d89-4eec-a0ba-64a9fe430f16","type":"GlyphRenderer"}]},"id":"b7fcc7dd-612b-4676-8ce5-abb9a23af407","type":"LegendItem"},{"attributes":{"dimension":1,"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"},"ticker":{"id":"62617dbf-6403-429f-9f35-7624046562a5","type":"BasicTicker"}},"id":"47590510-df47-453d-9b04-7e4a2b52f87b","type":"Grid"},{"attributes":{},"id":"aab283df-db28-4c6b-93d3-276ad0ce32af","type":"ToolEvents"},{"attributes":{},"id":"1523aa38-2563-471c-ba68-fb99e78d9d5a","type":"BasicTicker"},{"attributes":{"label":{"field":"foo"},"renderers":[{"id":"ae002b3a-24b8-4018-acf7-6612df6d94e7","type":"GlyphRenderer"}]},"id":"52f6580b-b009-4768-9f7c-d97a630b1e8b","type":"LegendItem"},{"attributes":{"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"e7e04fc2-ca76-4f0b-a583-0ba08a500e6e","type":"SaveTool"},{"attributes":{},"id":"d351e06e-e2b6-4977-8906-2528d26b8cd6","type":"BasicTickFormatter"},{"attributes":{"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"x":{"field":"x"},"y":{"field":"y"}},"id":"26f755bf-8fb6-4ef8-a640-89f9bf66360f","type":"Line"},{"attributes":{"line_color":{"value":"blue"},"x":{"field":"x"},"y":{"field":"foo"}},"id":"3c410111-828c-478c-b376-cc2dcafdfbe4","type":"Line"},{"attributes":{"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"6c16c019-8027-4df4-a9be-1d6035d1cbed","type":"HelpTool"},{"attributes":{"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"7eaeed08-fa9a-4c6b-87ed-fa68cc0f215f","type":"ResetTool"},{"attributes":{"callback":null},"id":"eeac9d00-7caf-4a46-bd3f-528a1c81f9d3","type":"DataRange1d"},{"attributes":{"active_drag":"auto","active_scroll":"auto","active_tap":"auto","tools":[{"id":"6ed84777-0a5f-4d3e-bf60-b858c6110755","type":"PanTool"},{"id":"6ab96d89-a1dc-4765-940c-a8d1228dc3d2","type":"WheelZoomTool"},{"id":"d3921f73-7e0a-4253-a9a6-16dfb59ca66a","type":"BoxZoomTool"},{"id":"e7e04fc2-ca76-4f0b-a583-0ba08a500e6e","type":"SaveTool"},{"id":"7eaeed08-fa9a-4c6b-87ed-fa68cc0f215f","type":"ResetTool"},{"id":"6c16c019-8027-4df4-a9be-1d6035d1cbed","type":"HelpTool"}]},"id":"824c7c68-6e51-4d79-9a19-9f2efd7c1319","type":"Toolbar"},{"attributes":{"items":[{"id":"b7fcc7dd-612b-4676-8ce5-abb9a23af407","type":"LegendItem"},{"id":"52f6580b-b009-4768-9f7c-d97a630b1e8b","type":"LegendItem"}],"plot":{"id":"b6bf1830-0bba-4508-b4ae-2ea120016cf8","subtype":"Figure","type":"Plot"}},"id":"54eeeeea-affb-4c7f-a2a5-8820503a7a0d","type":"Legend"},{"attributes":{"callback":null,"column_names":["index","x","y","foo"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"ffa7dbbc-53f4-497a-977b-5220bf231f2e","type":"ColumnDataSource"},{"attributes":{"callback":null,"column_names":["index","x","y","foo"],"data":{"foo":[4,2,12],"index":[0,1,2],"x":[1,2,3],"y":[2,5,9]}},"id":"b2eec34d-3934-49e4-b063-116ba7f8367c","type":"ColumnDataSource"}],"root_ids":["b6bf1830-0bba-4508-b4ae-2ea120016cf8"]},"title":"Bokeh Application","version":"0.12.3"}};
                  var render_items = [{"docid":"a9c32d1d-f23e-4de4-ae7d-b9b1f65a304f","elementid":"348d65ef-c653-425e-9c9a-921b1fbd742a","modelid":"b6bf1830-0bba-4508-b4ae-2ea120016cf8"}];
                  
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