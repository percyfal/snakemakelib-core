var colorbrewer = {Paired: {
    3	: [ "#A6CEE3","#1F78B4","#B2DF8A"],
    4	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C"],
    5	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99"],
    6	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C"],
    7	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F"],
    8	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00"] ,
    9	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6"],
    10	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6","#6A3D9A"],
    11	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6","#6A3D9A","#FFFF99"],
    12	: [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6","#6A3D9A","#FFFF99", "#B15928"]}};

var pca_callback;
pca_callback = function(source, cb_obj, item) {
    var data = source.get('data');
    var active = cb_obj.get('active');
    // If radio button group need index
    // var label = cb_obj.get('label')[active]
    var label = cb_obj.get('label');
    var colormap = {};
    // Comment out if(!active) if radiobuttongroup
    if (!active) {
	if (typeof(data[label][0]) != "string") {
	    var minsize = Math.log(Math.min.apply(null, data[label]))/Math.LN2;
	    var maxsize = Math.log(Math.max.apply(null, data[label]))/Math.LN2;
	    for (i = 0; i < data[item].length; i++) {
		data['size'][i] = 10 + (Math.log(data[label][i])/Math.LN2 - minsize) / (maxsize - minsize) * 20;
	    }
	} else {
	    var j = 0;
	    // Simple categorical grouping
	    for (i = 0; i < data[item].length; i++) {
		if (data[label][i] in colormap) {
		} else {
		    colormap[data[label][i]] = j;
		    j++;
		}
	    }
	    var nfac = Object.keys(colormap).length;
	    if (nfac > 12) {
		nfac = 12;
	    } 
	    if (nfac < 3) {
		nfac = 3;
	    }
	    var colors = colorbrewer['Paired'][nfac];
	    for (i = 0; i < data[label].length; i++) {
		data['color'][i] = colors[colormap[data[label][i]]]
	    }
	}
    } else {
	if (typeof(data[label][i] != "string")) {
	    for (i = 0; i < data[item].length; i++) {
		data['size'][i] = 10;
	    }
	}
    }
    source.trigger('change');
};

var pca_component;
pca_component = function(source, cb_obj, component) {
    var myRe = /^([0-9]+)/;
    var data = source.get('data');
    var value = myRe.exec(String(cb_obj.get('value')))[1]
    var pcacomp = data[component]
    for (i = 0; i < pcacomp.length; i++) {
        pcacomp[i] = data[value-1][i]
    }
    source.trigger('change');
};
