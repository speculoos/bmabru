//test

function InitMap()
{
    var bmabru_json_url = '/api/projects/';
    
    var map = bMa.Map($('#map')[0]);
//     var csl = bMa.Console($('#console'), map);
    var legend = bMa.Legend($('#legend-box'), map);
    var selector = bMa.LayerSelector($('#layer-selector'), map);
    var zoom_control = bMa.ZoomControl(map, $('#zoom-control-box'));
    
    var popup = $('#index_popup_box');
    popup.on('click', function(){
        $(this).hide();
    });
    
    var article = bMa.Article($('#page-box'));
    $('.page-ref').on('click', function(){
        popup.hide();
        var id = $(this).attr('id');
        var id_parts = id.split('_');
        var aid = id_parts.pop();
        legend.hide();
        article.show(aid);
    });
    
    if(window.bma_current_page !== undefined)
    {
        popup.hide();
        article.show(window.bma_current_page);
    }
    
    
    
    for(var key in WMS_CONFIG)
    {
        var wms = WMS_CONFIG[key];
        map.add_layer(key, wms.url, wms.options);
    }
    
    $.ajax({
        method: 'GET',
        url: bmabru_json_url,
        dataType: 'json',
           progress: function(e) {
//                //make sure we can compute the length
//                if(e.lengthComputable) {
//                    //calculate the percentage loaded
//                    var pct = (e.loaded / e.total) * 100;
//                    
//                    //log percentage loaded
//                    console.log(pct);
//                }
//                //this usually happens when Content-Length isn't set
//                else {
//                    console.warn('Content Length not reported!');
//                }
           }
    }).done(function(projects_data){
            var cur_p = undefined;
            for(var idx = 0; idx < projects_data.length; idx++)
            {
                var pdata = projects_data[idx];
                var p = bMa.Project(pdata);
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
                    popup.hide();
                    article.hide();
                    legend.show(this);
                }, p);
                
                p.layer = ovl;
            }
            
            popup.hide();
            if(cur_p !== undefined)
            {
                legend.show(cur_p);
            }
            
            var filter = bMa.Filter($('#filter-box'), map);
    })
.fail(function(xhr, ts, et){
console.log(ts);
});
    
//     var gallery = bMa.Gallery($('#gallery-wrapper'));
}

function Init () {
    InitMap();
}
$(document).ready( Init );
