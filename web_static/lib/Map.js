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
            
            this.observers = [];
            this.layers = {};
            this.overlays = {};
//             this.layers_control = L.control.layers({}, {}, {position:'bottomright'}).addTo(this.map);
        },
        add_layer:function(name, url, options){
            var layer = L.tileLayer.wms(url, options);
            this.layers[name] = layer;
            this.map.addLayer(layer);
//             this.layers_control.addBaseLayer(layer, name);
            for(var oid in this.observers)
            {
                var o = this.observers[oid];
                o.cb.call(o.ctx, name, layer);
            }
        },
        add_overlay:function(name, overlay){
            if(this.overlays[name] === undefined)
            {
                this.overlays[name] = L.layerGroup();
//                 this.layers_control.addOverlay(this.overlays[name], name);
                this.map.addLayer(this.overlays[name]);
            }
            var group = this.overlays[name];
            group.addLayer(overlay);
        },
        on_layer_add:function(cb, ctx){
            ctx = ctx || this.map;
            this.observers.push({cb:cb,ctx:ctx});
        },
    };
    var ret = Object.create(proto);
    ret.init(container);
    return ret;
};