//test

function InitMap()
{
    var bmabru_json_url = '/projects/';
    
    var map = bMa.Map('map');
//     var csl = bMa.Console($('#console'), map);
    var legend = bMa.Legend($('#legend-box'));
    var selector = bMa.LayerSelector($('#layer-selector'), map);
    var zoom_control = bMa.ZoomControl(map, $('#zoom-control-box'));
    
    var article = bMa.Article($('#page-box'));
    $('.page-ref').on('click', function(){
        var id = $(this).attr('id');
        var id_parts = id.split('_');
        var aid = id_parts.pop();
        legend.hide();
        article.show(aid);
    });
    
    var filter = bMa.Filter($('#filter-box'));
    
    
    for(var key in WMS_CONFIG)
    {
        var wms = WMS_CONFIG[key];
        map.add_layer(key, wms.url, wms.options);
    }
    
    
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
            var ovl = new L.GeoJSON(geo, {
                style:function(f){ 
                    return bMa.Config().get_dict('/feature/style/show');
                }
            });
            map.add_overlay('bMa', ovl);
            
            ovl.on('click', function(evt){
                article.hide();
                legend.show(this);
            }, p);
            
            p.layer = ovl;
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