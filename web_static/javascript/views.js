/*
 * 
 * views.js
 * 
 */



(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    var T = window.Template;
    
    
    var page = Backbone.View.extend({
        className:'page',
        initialize:function(){
            this.model.on('change', this.render, this);
        },
        render: function() {
            var $el = this.$el;
            $el.empty();
            var data = this.model.toJSON();
            T.render(model, this, function(t){
                $el.html(t(data));
                if(this.postRender)
                {
                    this.postRender(data);
                }
            });
            return this;
        },
    });
    
    var project_geometry = Backbone.View.extend({
        initialize:function(){
            this.model.on('change', this.render, this);
            this.map = this.options.map;
        },
        render:function(){
            
        },
    });
    
    var project =  Backbone.View.extend({
        className:'project',
        initialize:function(){
            this.model.on('change', this.render, this);
            
        },
        render: function() {
            var $el = this.$el;
            $el.empty();
            var data = this.model.toJSON();
            T.render(model, this, function(t){
                $el.html(t(data));
                if(this.postRender)
                {
                    this.postRender(data);
                }
            });
            return this;
        },
    });
    
    var map = Backbone.View.extend({
        className:'map',
        initialize:function(){
            this.map = L.map(this.el,{
                center: [50.854075572144815, 4.38629150390625],
                zoom: 13,
                crs: L.CRS.EPSG900913,
                zoomControl: false,
                attributionControl: false
            });
            //             var s = bMa.Scale()
            //             s.addTo(this.map);
            
            this.observers = [];
            this.layers = {};
            this.overlays = {};
        },
        render:function(){
  
            return this;
        },
    });
    
    
    bMa.Views = {
        Page: page,
        Project: project,
        Geometry: project_geometry,
        Map: map,
    };
    
})();