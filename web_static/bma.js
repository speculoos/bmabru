//test

function InitMap()
{
    var bmabru_json_url = '/projects/';
    
    var map = bMa.Map('map');
//     var csl = bMa.Console($('#console'), map);
    var legend = bMa.Legend($('#content'));
    var selector = bMa.LayerSelector($('#layer-selector'), map);
    var zoom_control = bMa.ZoomControl(map, $('#zoom-control-box'));
    
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
        var cur_p = undefined;
        for(var idx = 0; idx < projects_data.length; idx++)
        {
            var pdata = projects_data[idx];
            var p = bMa.Project(pdata);
            console.log('Add ['+p.id+'] => '+p.get('slug'))
            if(window.bma_current_project !== undefined 
                && bma_current_project === p.id)
            {
                cur_p = p;
            }
            var geo = p.get('geojson');
            var ovl = new L.GeoJSON(geo, {style:function(f){ return ovl_options;}});
            map.add_overlay('bMa', ovl);
            
            ovl.on('click', function(evt){
                legend.show(this);
            }, p);
        }
        
        if(cur_p !== undefined)
        {
            legend.show(cur_p);
        }
    });
}

function Init () {
    InitMap();
}
$(document).ready( Init );