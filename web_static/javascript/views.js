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
    
    var tname = function(name){
        var prefix = 'v2';
        return [prefix,name].join('/');
    };
    
    var navigation = Backbone.View.extend({
        className:'container-fluid',
        initialize:function(){
            this.medias = bMa.Data.Medias;
        },
        render:function(){
            var $el = this.$el;
            $el.empty();
            var data = _.extend({},this.medias);
            T.render(tname('navigation'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
        events:{
//             'click .section':'toggleNav',
        },
        toggleNav:function(evt){
            var section = $(evt.target);
            var list = section.next('ul');
            list.toggle();
        },
    });
    
    var tools = Backbone.View.extend({
        className:'container-fluid',
        initialize:function(){
        },
        render:function(){
            var $el = this.$el;
            $el.empty();
            var data = {};
            T.render(tname('tools'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
    });
    
    var page = Backbone.View.extend({
        className:'page',
        initialize:function(){
            this.model.on('change', this.render, this);
        },
        render: function() {
            var $el = this.$el;
            $el.empty();
            var data = this.model.toJSON();
            T.render(tname('page'), this, function(t){
                var html = t(data);
                $el.html(html);
            });
            return this;
        },
    });
    
    var pageViewer =  Backbone.View.extend({
        id:'page-box',
        initialize:function(){
            
        },
        render:function(){
            var $el = this.$el;
            $el.empty();
            if(this.page){
                $el.append(this.page.render().el);
            };
            return this;
        },
        setModel:function(model){
            this.page = new page({model:model});
            return this.render();
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
            T.render(tname('project'), this, function(t){
                $el.html(t(data));
                if(this.postRender)
                {
                    this.postRender(data);
                }
            });
            return this;
        },
    });
    
    var projectViewer = Backbone.View.extend({
        className:'project-box',
        initialize:function(){
        },
        render:function(){
            var $el = this.$el;
            $el.empty();
            if(this.project){
                $el.append(this.project.render().el);
            };
            return this;
        },
        setModel:function(model){
            this.project = new project({model:model});
            return this.render();
        },
    }); 
    
    var map = Backbone.View.extend({
        id:'map-wrapper',
        initialize:function(){
            
            //             var s = bMa.Scale()
            //             s.addTo(this.map);
            
            this.observers = [];
            this.layers = {};
            this.overlays = {};
        },
        render:function(){
            this.$el.append(this.getMap(true));
            return this;
        },
        insertFeatures:function(){
            var group = L.layerGroup();
            this.map.addLayer(group);
            for(var slug in bMa.Data.Geometries)
            {
                var geo = bMa.Data.Geometries[slug];
                var ovl = new L.GeoJSON(geo, {
                    style:function(f){ 
                        return {
                            stroke:true,
                            color: '#d43b2d',
                            weight:1,
                            opacity:1,
                            fill:true,
                            fillColor: '#d43b2d',
                            fillOpacity:0.75,
                            clickable:true
                        };
                    }
                });
                group.addLayer(ovl);
                
                ovl.on('click', function(evt){
                    window.router.navigate('project/'+slug);
                });
            }
        },
        getMap:function(element){
            if(this.map === undefined)
            {
                this.$map = $('<div>').attr('id', 'map');
                this.map = L.map(this.$map[0],{
                    center: [50.854075572144815, 4.38629150390625],
                    zoom: 13,
                    crs: L.CRS.EPSG900913,
                    zoomControl: false,
                    attributionControl: false
                });
                this.map.on('whenReady', this.refresh.bind(this));
                this.insertFeatures();
                for(var key in window.WMS_CONFIG)
                {
                    var wms = WMS_CONFIG[key];
                    var layer = L.tileLayer.wms(wms.url, wms.options);
                    this.map.addLayer(layer);
                }
            }
            return element ? this.$map : this.map;
        },
        refresh:function(){
            console.log('REFRESH MAP');
            var self = this;
            window.setTimeout(function(){
                self.map.invalidateSize();
                console.log('CENTER MAP');
            }, 1000);
        },
    });
    
    
    bMa.Views = {
        Page: page,
        PageViewer: pageViewer,
        Project: project,
        ProjectViewer: projectViewer,
        Map: map,
        Navigation: navigation,
    };
    
})();