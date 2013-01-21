/*
 Map.js
*/

window.bMa = window.bMa || {}

window.bMa.Map = function(container){
    proto = {
        init:function(container){
            this.map = L.map(container,{
                center: [50.854075572144815, 4.38629150390625],
                zoom: 12,
                crs: L.CRS.EPSG900913,
            });
            
            this.layers = {};
            this.overlays = {};
            this.layers_control = L.control.layers({}, {}, {position:'bottomright'}).addTo(this.map);
        },
        add_layer:function(name, url, options){
            var layer = L.tileLayer.wms(url, options);
            this.layers[name] = layer;
            this.map.addLayer(layer);
            this.layers_control.addBaseLayer(layer, name);
        },
        add_overlay:function(name, overlay){
            if(this.overlays[name] === undefined)
            {
                this.overlays[name] = L.layerGroup();
                this.layers_control.addOverlay(this.overlays[name], name);
                this.map.addLayer(this.overlays[name]);
            }
            var group = this.overlays[name];
            group.addLayer(overlay);
        },
    };
    var ret = Object.create(proto);
    ret.init(container);
    return ret;
};