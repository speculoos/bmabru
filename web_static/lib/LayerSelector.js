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
//             this.update(name);
            var that = this;
            this.selector.add_item(name, {
                click:function(evt){
                    that.select(name);
                }
            });
            
            that.select(name);
        },
//         update:function(name){
//             if(name === undefined)
//             {
//                 for(var lid in this.layers)
//                 {
//                     if(this.layers[lid].selected)
//                     {
//                         name = lid;
//                         break;
//                     }
//                 }
//             }
//             this.container.empty();
//             this.items = {};
//             for(var lid in this.layers)
//             {
//                 var l = this.layers[lid];
//                 var litem = $('<div class="layer-item">'+lid+'</div>');
//                 if(lid === name)
//                 {
//                     litem.addClass('layer-selected');
//                     l.selected = true;
//                 }
//                 else
//                 {
//                     l.selected = false;
//                 }
//                 var that = this;
//                 litem.on('click', function(evt){
//                     var elem = $(this);
//                     if(elem.hasClass('layer-selected'))
//                         return;
//                     that.select(elem.text());
//                 });
//                 this.items[lid] = litem;
//                 this.container.append(litem);
//             }
//         },
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