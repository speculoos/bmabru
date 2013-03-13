/*
 * Scale.js
 */


window.bMa = window.bMa || {};

window.bMa.Scale = function(options){
    var proto = {
        options: {
            position: 'bottomright',
            maxWidth: 200,
            metric: true,
            imperial: false,
            updateWhenIdle: false
        },
        onAdd: function(map){
            this._map = map;
            var options = this.options;
            this._container = L.DomUtil.create('div','control-scale-box');
            this.scale_container = $(this._container);
            map.on(options.updateWhenIdle ? 'moveend' : 'move', this._update, this);
            map.whenReady(this._update, this);
            
            return this._container;
        },
        onRemove: function (map) {
            map.off(this.options.updateWhenIdle ? 'moveend' : 'move', this._update, this);
        },
        _updateMetric: function(maxMeters){
            var meters = this._getRoundNum(maxMeters);
            var sc_width = this._getScaleWidth(meters / maxMeters);
            var end_label = meters < 1000 ? meters + ' m' : (meters / 1000) + ' km';
            this.scale_container.empty();
            this.scale_container.css('width', sc_width + 'px');
            this.scale_container.append('<div class="control-scale-metrics-box">\
            <div class="control-scale-metrics-start">0</div>\
            <div class="control-scale-metrics-end">'+end_label+'</div>\
            </div');
            var scb = $('<div class="control-scale-scale"></div>');
            var top_row = $('<div class="control-scale-row control-scale-row-top" />');
            var bottom_row = $('<div class="control-scale-row control-scale-row-bottom" />');
            var steps = this.options.steps || 4;
            var step_width = Math.floor(sc_width / steps);
            var dark = false;
            for(var s = 0; s < steps; s++)
            {
                var sc_class = 'control-scale-part-light';
                if(dark)
                {
                    sc_class = 'control-scale-part-dark';
                }
                var part = $('<div />');
                part.css('width', step_width+'px');
                part.addClass('control-scale-part');
                part.addClass(sc_class);
                top_row.append(part);
                dark = !dark;
            }
            dark = true;
            for(var s = 0; s < steps; s++)
            {
                var sc_class = 'control-scale-part-light';
                if(dark)
                {
                    sc_class = 'control-scale-part-dark';
                }
                var part = $('<div />');
                part.css('width', step_width+'px');
                part.addClass('control-scale-part');
                part.addClass(sc_class);
                bottom_row.append(part);
                dark = !dark;
            }
            scb.append(top_row);
            scb.append(bottom_row);
            this.scale_container.append(scb);
        },
    };
    
    var scale = L.Control.Scale.extend(proto);
    var ret = new scale(options);
    return ret;
};