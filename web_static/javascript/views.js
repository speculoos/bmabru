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
    
    var splashscreen = View.extend({
        className:'splashscreen',
        id:'index_popup_box',
        initialize:function(){
            this._display = true;
        },
        render:function(){
            if(this._display)
            {
                var data = _.extend({}, {news: bMa.Data.HotNews});
                T.render(tname('splashscreen'), this, function(t){
                    this.$el.html(t(data));
                });
            }
            return this;
        },
        events:{
            'click .route':'close',
            'click .close':'close',
        },
        close:function(){
            this._display = false;
            this.$el.hide();
        },
    });
    
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
        setCurrentCat:function(slug){
            var theCat = undefined;
            for(var catname in bMa.Data.Medias)
            {
                var cat = bMa.Data.Medias[catname];
                for(var pid in cat)
                {
                    var pslug = cat[pid].slug;
                    if(slug === pslug)
                    {
                        theCat = catname;
                    }
                }
            }
            this.$el.find('.section').removeClass('current');
            if(theCat)
                this.$el.find('[data-cat="'+theCat+'"]').addClass('current');
        }
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
            _.extend(data, {pages:this.lookupCategory()});
            T.render(tname('page'), this, function(t){
                var html = t(data);
                $el.html(html);
            });
            return this;
        },
        lookupCategory:function(){
            var spid = ''+this.model.id
            for(var catname in bMa.Data.Medias)
            {
                var cat = bMa.Data.Medias[catname];
                for(var pid in cat)
                {
                    if(pid === spid)
                    {
                        return _.clone(cat);
                    }
                }
            }
            return {};
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
    
    var blogPost = View.extend({
        className:'post',
        initialize:function(){
            this.model.on('change', this.render.bind(this));
        },
        render:function(){
            var data = this.model.toJSON();
            T.render(tname('blog-post'), this, function(t){
                this.$el.html(t(data));
            });
            return this;
        },
    });
    
    var blog = View.extend({
        className:'blog',
        initialize:function(){
            bMa.Data.collections.blog.on('add', this.renderOne.bind(this));
            bMa.Data.collections.blog.on('reset', this.render.bind(this));
        },
        renderOne:function(item){
            if(this.items && !this.items[item.cid])
            {
                this.items[item.cid] = new blogPost({model:item});
                this.$el.append(this.items[item.cid].render().el);
            }
        },
        render:function(){
            var data = {};
            T.render(tname('blog'), this, function(t){
                this.items = {};
                this.$el.html(t(data));
                bMa.Data.collections.blog.each(this.renderOne.bind(this));
            });
            return this;
        },
        selectItem:function(slug){
            for(var k in this.items)
            {
                var ms = this.items[k].model.get('slug');
                console.log('selectItem',ms,slug);
                if( ms && ms === slug)
                {
                    this.items[k].model.set({selected:true})
                    return;
                }
            }
            bMa.Data.collections.blog.once('add',function(){
                this.selectItem(slug);
            }, this);
        },
    });
    
    var projectListRow = View.extend({
        tagName:'tr',
        initialize:function(){
            this.model.on('change', this.render.bind(this));
        },
        render:function(){
            
            console.log('RENDER ROW', this.cid);
            var $el = this.$el;
            var data = this.model.toJSON();
            T.render(tname('projectrow'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
    });
    
    var projectList = View.extend({
        id:'projects_table_wrapper',
        initialize:function(){
//             this.projects = bMa.Data.collections.projects;
//             this.projects.on('add', this.renderOne.bind(this));
        },
        renderOne:function(item){
            if(this.items)
            {
                if(this.items[item.cid] === undefined)
                {
                    this.items[item.cid] = new projectListRow({model:item});
                    this.items[item.cid].render().$el.appendTo(this.$tbody);
                }
            }
        },
        render:function(){
            var $el = this.$el;
            this.items = {};
            var data = {};
            T.render(tname('projectlist'), this, function(t){
                $el.html(t(data));
                this.$tbody = this.$el.find('.table-body');
                _.each(bMa.Data.Projects, function(p){
                    var m = new bMa.Models.Project({id:p.id});
                    this.renderOne(m);
                    m.fetch();
                }, this);
            });
            return this;
        },
        refresh:function(){
//             this.projects.fetch();
        },
    });
    
    
    var project =  View.extend({
        className:'project',
        initialize:function(){
            this.model.on('change', this.render, this);
            
        },
        render: function() {
            var $el = this.$el;
            var data = this.model.toJSON();
            T.render(tname('project'), this, function(t){
                $el.html(t(data));
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
    
    var carousel = View.extend({
        className:'carousel-box',
        initialize:function(){
        },
        render:function(){
            if(this.model)
            {
                var $el = this.$el;
                var data = {images:this.model.toJSON().image};
                console.log(data);
                T.render(tname('carousel'), this, function(t){
                    $el.html(t(data));
                });
            }
            return this;
        },
        setModel:function(model){
            this.model = model;
            this.model.on('change:image', this.render.bind(this));
//             this.render();
        },
        selectImage:function(image){
            // TODO
        },
        events:{
            'click .close':'close',
        },
        close:function(){
            window.router.navigate('project/'+this.model.get('slug'));
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
            this._refreshing = true;
            var self = this;
            window.setTimeout(function(){
                self.map.invalidateSize();
                _.each(self.layers, function(l){
                    l._update();
                });
                self._refreshing = false;
                self.trigger('refreshed');
            }, 200);
            
        },
        _whenReady:function(c){
            if(!this._refreshing)
                c.apply(this, []);
            else
            {
                this.once('refreshed', c.bind(this));
            }
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
        showProject:function(slug){
            var map = this.getMap();
            var p = this.polys[slug];
            if(p)
            {
                this._whenReady(function(){map.fitBounds(p);});
            }
        },
        filterCity:function(city){
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
            this._whenReady(function(){
                if(bounds !== undefined)
                    map.fitBounds(bounds);
                else{
                    map.setView(window.MAP_CONFIG.CENTER, window.MAP_CONFIG.ZOOM);
                }
            });
        },
    });
    
    
    bMa.Views = {
        Page: page,
        PageViewer: pageViewer,
        Project: project,
        ProjectList: projectList,
        ProjectViewer: projectViewer,
        Map: map,
        MapTools: mapTools,
        Navigation: navigation,
        SiteTools: siteTools,
        Splash: splashscreen,
        Blog: blog,
        Carousel: carousel,
    };
    
})();