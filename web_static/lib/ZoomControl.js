/*
 * ZoomControl.js
 */

window.bMa = window.bMa || {};

window.bMa.ZoomControl = function(map, container){
    var proto = {
        init:function(map, container){
            this.map = map;
            this.container = container || $('<div class="zoom-control-box" />');
            this.zoom_out = $('<div class="zoom-control-out"> − </div>');
            this.zoom_in = $('<div class="zoom-control-in"> + </div>');
            this.zoom_scale_box = $('<div class="zoom-control-scale-box" />');
            this.zoom_scale_cursor = $('<div class="zoom-control-scale-cursor" />');
            this.zoom_scale_scale = this.scale();
            
            this.zoom_scale_box.append(this.zoom_scale_cursor);
            this.zoom_scale_box.append(this.zoom_scale_scale);
            
            this.container.append(this.zoom_out);
            this.container.append(this.zoom_scale_box);
            this.container.append(this.zoom_in);
            
            this.setup_events();
        },
        scale: function(){
            this.scale_container = $('<div class="zoom-control-scale-scale" />');
            var that = this;
            function scale_resize(scale_factor){
                that.scale_container.empty();
                var width = that.scale_container.width();
                var steps = Math.floor(width / scale_factor);
                var step_width = Math.floor(width / steps);
                var dark = false;
                for(var s = 0; s < steps; s++)
                {
                    var sc_class = 'zoom-control-scale-part-light';
                    if(dark)
                    {
                        sc_class = 'zoom-control-scale-part-dark';
                    }
                    var part = $('<div />');
                    part.css('width', step_width+'px');
                    part.addClass(sc_class);
                    that.scale_container.append(part);
                    console.log('Append '+sc_class+' to scale_container');
                    dark = !dark;
                }
            };
            that.scale_container.on('resize',function(evt){
                scale_resize(lmap.getZoom());
            });
            var lmap = this.map.map;
            lmap.on('zoomend', function(evt){
                scale_resize(lmap.getZoom());
            });
            scale_resize(lmap.getZoom());
            return that.scale_container;
            
        },
        scale_cursor: function(){
            
        },
        setup_events:function(){
            var that = this;
            var lmap = this.map.map;
            this.zoom_out.on('click', function(){
                lmap.zoomOut();
            });
            this.zoom_in.on('click', function(){
                lmap.zoomIn();
            });
        },
    };
    
    var ret = Object.create(proto);
    ret.init(map, container);
    return ret;
};