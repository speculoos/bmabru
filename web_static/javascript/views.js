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
                cities: _.uniq(_.pluck(bMa.Data.Projects, 'city')).sort(),
                layers: window.MAP_CONFIG.WMS,
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
            'click .layer-selector':'changeLayer',
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
            this.toggleASelector(t.parents('.selector-root'));
        },
        selectItem:function(evt){
            var t = $(evt.target);
            this.toggleASelector(t.parents('.selector-root'));
        },
        changeLayer:function(evt){
            var layer = $(evt.target).attr('data-layer');
            window.app.send('main_map', 'selectLayer', layer);
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
                this.getMap(true).appendTo(this.$el);
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
                
                var ovl = new L.GeoJSON(geo);
                ovl.setStyle(bMa.Style.featureNormal);
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
                this.$map = $('<div />').css({
                    width:'100%',
                    height:'100%',
                });
                this.map = L.map(this.$map[0],{
                    center: window.MAP_CONFIG.CENTER,
                    zoom: window.MAP_CONFIG.ZOOM,
                    crs: window.MAP_CONFIG.CRS,
                    zoomControl: false,
                    attributionControl: false
                });
//                 this.map.on('whenReady', this.refresh.bind(this));
                this.insertFeatures();
                for(var key in window.MAP_CONFIG.WMS)
                {
                    var wms = window.MAP_CONFIG.WMS[key];
                    var layer = L.tileLayer.wms(wms.url, wms.options);
                    if(wms.visible)
                    {
                        this.map.addLayer(layer);
                        layer.selected = true;
                    }
                    else
                    {
                        layer.selected = false;
                    }
                    this.layers[key] = layer;
                }
                this.map.whenReady(function(){
                    this.trigger('ready');
                }, this);
            }
            return element ? this.$map : this.map;
        },
        refresh:function(){
            var self = this;
            window.setTimeout(function(){
                self.map.invalidateSize();
            }, 200);
        },
        selectLayer:function(name){
            var map = this.getMap();
            for(var lid in this.layers)
            {
                var l = this.layers[lid];
                if(l.selected)
                {
                    map.removeLayer(l);
                }
                l.selected = false;
                if(lid === name)
                {
                    l.selected = true;
                    map.addLayer(l);
                }
            }
        },
        filterCity:function(city){
            console.log('Filer City', city);
            var map = this.getMap();
            var bounds = undefined;
            for(var slug in bMa.Data.Projects)
            {
                var p = bMa.Data.Projects[slug];
                if(p.geometry === undefined)
                    continue;
                this.polys[slug].setStyle(bMa.Style.featureNormal);
                if(p.city === city)
                {
                    this.polys[slug].setStyle(bMa.Style.featureHighlight);
                    if(bounds === undefined)
                    {
                        bounds = this.polys[slug].getBounds();
                    }
                    else
                    {
                        bounds.extend(this.polys[slug].getBounds());
                    }
                    console.log(slug, bounds);
                }
            }
            if(bounds !== undefined)
                map.fitBounds(bounds);
            else{
                map.setView(window.MAP_CONFIG.CENTER, window.MAP_CONFIG.ZOOM);
            }
            this.refresh();
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