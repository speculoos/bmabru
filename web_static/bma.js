//test

function InitMap()
{
    var bmabru_json_url = '/projects/';
    
    var map = bMa.Map('map');
    var csl = bMa.Console($('#console'), map);
    var legend = bMa.Legend($('#content'));
    var selector = bMa.LayerSelector($('#layer-selector'), map);
    
    for(var key in WMS_CONFIG)
    {
        var wms = WMS_CONFIG[key];
        map.add_layer(key, wms.url, wms.options);
    }
    
    
    var ovl_options = {
        stroke:true,
        color: '#d43b2d',
        weight:1,
        opacity:1,
        fill:true,
        fillColor: '#d43b2d',
        fillOpacity:0.5,
        clickable:true
    };
    $.getJSON(bmabru_json_url, function( projects_data ){
        for(var idx = 0; idx < projects_data.length; idx++)
        {
            var pdata = projects_data[idx];
            var p = bMa.Project(pdata);
            var geo = p.get('geojson');
            var ovl = new L.GeoJSON(geo, {style:function(f){ return ovl_options;}});
            map.add_overlay('bMa', ovl);
            csl.add(p);
            ovl.on('mouseover', function(evt){
                csl.highlight(this.id);
            }, p);
            ovl.on('mouseout', function(evt){
                csl.dehighlight();
            });
            
            ovl.on('click', function(evt){
                legend.show(this);
            }, p);
        }
    });
}

function Init () {
    InitMap();
}
$(document).ready( Init );