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
    
    var View = Backbone.View.extend({
//         constructor: function() {
//             Backbone.View.apply(this, arguments);
//             this.on('message:in', this._deliver.bind(this));
//         },
        deliver:function(targetMethod, args){
            if(_.isFunction(this[targetMethod]))
            {
                this[targetMethod].apply(this, args);
            }
        },
        addClass:function(klass){
            this.$el.addClass(klass);
        },
        removeClass:function(klass){
            this.$el.removeClass(klass);
        },
    });
    
    var tname = function(name){
        var prefix = 'v2';
        return [prefix,name].join('/');
    };
    
    var navigation = View.extend({
        className:'navigation',
        initialize:function(){
            this.medias = bMa.Data.Medias;
        },
        render:function(){
            var $el = this.$el;
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
    
    var siteTools = View.extend({
        className:'site-tools',
        initialize:function(){
            
        },
        render:function(){
            var $el = this.$el;
            var data = {};
            T.render(tname('sitetools'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
    });
    
    var tools = View.extend({
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
    
    var page = View.extend({
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
    
    var pageViewer =  View.extend({
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
    
    
    
    var project =  View.extend({
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

    
    var projectViewer = View.extend({
        id:'project-box',
        className:'span4',
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
    
    var mapTools = View.extend({
        id:'maptools',
        initialize:function(){
            
        },
        render:function(){
            var $el = this.$el;
            $el.empty();
            var data = { 
                cities: _.pluck(bMa.Data.Projects, 'city'),
                layers: window.WMS_CONFIG,
            };
            T.render(tname('maptools'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
        events:{
            'click .zoom-control-out':'zoomOut',
            'click .zoom-control-in':'zoomIn',
            'click .selector-button':'toggleSelector',
            'click .selector-item':'selectItem',
        },
        zoomOut:function(){
            var map = window.app.getComponent('main_map').getMap();
            map.zoomOut();
        },
        zoomIn:function(){
            var map = window.app.getComponent('main_map').getMap();
            map.zoomIn();
        },
        toggleASelector:function(parent){
            var items = parent.find('.selector-items');
            items.toggle();
        },
        toggleSelector:function(evt){
            var t = $(evt.target);
            this.toggleASelector(t.parent());
        },
        selectItem:function(evt){
            var t = $(evt.target);
            
        },
    });
    
    var map = View.extend({
        id:'map',
        initialize:function(){
            
            //             var s = bMa.Scale()
            //             s.addTo(this.map);
            
            this.observers = [];
            this.layers = {};
            this.overlays = {};
            this.map_rendered = false;
            this.polys = {};
        },
        render:function(){
            if(!this.map_rendered)
            {
                this.getMap();
                this.map_rendered = true;
            }
            return this;
        },
        insertFeatures:function(){
            var group = L.layerGroup();
            this.map.addLayer(group);
            for(var slug in bMa.Data.Projects)
            {
                var geo = bMa.Data.Projects[slug].geometry;
                if(geo === undefined)
                    continue;
                
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
                this.polys[slug] = ovl;
                ovl.project_ref = 'project/'+slug;
                ovl.on('click', function(evt){
                    window.router.navigate(this.project_ref);
                });
            }
        },
        getMap:function(element){
            if(this.map === undefined)
            {
                this.map = L.map(this.$el[0],{
                    center: [50.854075572144815, 4.38629150390625],
                    zoom: 13,
                    crs: L.CRS.EPSG900913,
                    zoomControl: false,
                    attributionControl: false
                });
//                 this.map.on('whenReady', this.refresh.bind(this));
                this.insertFeatures();
                for(var key in window.WMS_CONFIG)
                {
                    var wms = WMS_CONFIG[key];
                    var layer = L.tileLayer.wms(wms.url, wms.options);
                    this.map.addLayer(layer);
                    this.layers[key] = layer;
                }
            }
            return element ? this.$el : this.map;
        },
        refresh:function(){
            var self = this;
            window.setTimeout(function(){
                self.map.invalidateSize();
            }, 200);
        },
        selectLayer:function(name){
            for(var lid in this.layers)
            {
                var l = this.layers[lid];
                if(l.selected)
                {
                    this.getMap.removeLayer(l.layer);
                }
                l.selected = false;
                if(lid === name)
                {
                    l.selected = true;
                    this.getMap.addLayer(l.layer);
                }
            }
        },
    });
    
    
    bMa.Views = {
        Page: page,
        PageViewer: pageViewer,
        Project: project,
        ProjectViewer: projectViewer,
        Map: map,
        MapTools: mapTools,
        Navigation: navigation,
        SiteTools: siteTools,
    };
    
})();