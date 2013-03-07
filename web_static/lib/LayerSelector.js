/*
 LayerSelector.js
 */

window.bMa = window.bMa || {}

window.bMa.LayerSelector = function(container, map){
    proto = {
        init:function(container, map){
            this.container = container;
            this.map = map;
            this.layers = {};
            this.items = {};
            map.on_layer_add(this.layer_added, this);
            
            this.selector = bMa.Selector(container, 'Layers');
        },
        layer_added:function(name, layer){
            this.layers[name] = {layer:layer, selected:false};
            var that = this;
            this.selector.add_item(name, {
                click:function(evt){
                    that.select(name);
                }
            });
            
            that.select(name);
        },
        select:function(name){
            for(var lid in this.layers)
            {
                var l = this.layers[lid];
                if(l.selected)
                {
                    this.map.map.removeLayer(l.layer);
                }
                l.selected = false;
                if(lid === name)
                {
                    l.selected = true;
                    this.map.map.addLayer(l.layer);
                }
            }
        },
    };
    var ret = Object.create(proto);
    ret.init(container, map);
    return ret;
};