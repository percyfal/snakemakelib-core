# Copyright (C) 2015 by Per Unneberg
# From RColorBrewer: lapply(3:12, function(x) {brewer.pal(x, "Paired")})
Paired3	= [ "#A6CEE3","#1F78B4","#B2DF8A"]
Paired4	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C"]
Paired5	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99"]
Paired6	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C"]
Paired7	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F"]
Paired8	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00"] 
Paired9	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6"]
Paired10	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6","#6A3D9A"]
Paired11	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6","#6A3D9A","#FFFF99"]
Paired12	= [ "#A6CEE3","#1F78B4","#B2DF8A","#33A02C","#FB9A99","#E31A1C","#FDBF6F","#FF7F00","#CAB2D6","#6A3D9A","#FFFF99", "#B15928"]

Set2_3	= [ "#66C2A5","#FC8D62","#8DA0CB"]
Set2_4	= [ "#66C2A5","#FC8D62","#8DA0CB","#E78AC3"]
Set2_5	= [ "#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854"]
Set2_6	= [ "#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854","#FFD92F"]
Set2_7	= [ "#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854","#FFD92F","#E5C494"]
Set2_8	= [ "#66C2A5","#FC8D62","#8DA0CB","#E78AC3","#A6D854","#FFD92F","#E5C494","#B3B3B3"]

Dark2_3	= [ "#1B9E77","#D95F02","#7570B3"]
Dark2_4	= [ "#1B9E77","#D95F02","#7570B3","#E7298A"]
Dark2_5	= [ "#1B9E77","#D95F02","#7570B3","#E7298A","#66A61E"]
Dark2_6	= [ "#1B9E77","#D95F02","#7570B3","#E7298A","#66A61E","#E6AB02"]
Dark2_7	= [ "#1B9E77","#D95F02","#7570B3","#E7298A","#66A61E","#E6AB02","#A6761D"]
Dark2_8	= [ "#1B9E77","#D95F02","#7570B3","#E7298A","#66A61E","#E6AB02","#A6761D","#666666"]


__palettes__ = [ "Paired3", "Paired4", "Paired5", "Paired6",
                 "Paired7", "Paired8", "Paired9", "Paired10", "Paired11",
                 "Paired12", "Set2_3", "Set2_4", "Set2_5", "Set2_6", "Set2_7",
                 "Set2_8", "Dark2_3", "Dark2_4", "Dark2_5", "Dark2_6", "Dark2_7",
                 "Dark2_8" ]

brewer = {
    "Paired"    : { 3: Paired3, 4: Paired4, 5: Paired5, 6: Paired6, 7: Paired7, 8: Paired8, 9: Paired9, 10: Paired10, 11: Paired11, 12: Paired12},
    "Set2"      : { 3: Set2_3, 4: Set2_4, 5: Set2_5, 6: Set2_6, 7: Set2_7, 8: Set2_8},
    "Dark2"      : { 3: Dark2_3, 4: Dark2_4, 5: Dark2_5, 6: Dark2_6, 7: Dark2_7, 8: Dark2_8},
    }
