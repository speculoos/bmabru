//test

function InitMap()
{
    var WMS_URL = 'http://bmawms.specgis.be/service';
    var WMS_LAYER = 'bMa';
    var PG_URL = 'http://specgis.be:8001/';
    var MAP_TITLE = 'Map Title';
    var bmabru_json_url = 'http://bma.local/projects/';
    
    var map = bMa.Map('map');
    map.add_layer('bMa/OSM', WMS_URL, {
        layers: 'bMa',
        format: 'image/png',
        transparent: true,
        attribution: "OpenStreetMap styled by Speculoos"
    });
    var csl = bMa.Console($('#console'), map);
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
            var pid = p.id;
            ovl.on('click', function(evt){
                csl.highlight(pid);
            });
        }
    });
    

//     var feature_options = {
//         stroke:true,
//         color: '#d43b2d',
//         weight:1,
//         opacity:1,
//         fill:true,
//         fillColor: '#d43b2d',
//         fillOpacity:0.5,
//         clickable:true
//     };
//     BG.install_features('map', {
//         click:function(evt){
//             var ctnt = $('#content');
//             ctnt.html(projects[this.pid].content);
//             ctnt.show();
//         },
//         mouseover:function(evt){
//             $('.console_item').removeClass('clicked-feature');
//             $('#console_item_'+this.pid).addClass('clicked-feature');
//         },
//         mouseout:function(evt){
//             $('.console_item').removeClass('clicked-feature');
//         }
//     },feature_options);
}

function Init () {
    InitMap();
}
$(document).ready( Init );