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
    
    
    var blogPostTeaser = View.extend({
        className:'bpt',
        initialize:function(options){
            this.data = options.data;
        },
        render:function(){
            T.render(tname('blog-teaser'), this, function(t){
                this.$el.html(t(this.data));
                this.$el.trigger('rendered');
            });
            return this;
        },
    });
    
    var splashscreen = View.extend({
        className:'splashscreen',
        id:'index_popup_box_wrapper',
        initialize:function(){
            this._display = true;
            this.news = bMa.Data.HotNews;
        },
        render:function(){
            if(this._display)
            {
                this.newsItems = [];
                var data = {};
                T.render(tname('splashscreen'), this, function(t){
                    this.$el.html(t(data));
                    this.$container = this.$('.teasers');
                    this.$expander = this.$('.expander');
                    this.$right = this.$('.teasers-box');
                    this.$right.perfectScrollbar({
                        wheelSpeed: 20,
                        minScrollbarLength: 20,
                    })
                    this.mayLoadMore();
//                     this.$right.perfectScrollbar('update');
                    this.$right.on('scroll', this.mayLoadMore.bind(this));
                });
            }
            return this;
        },
        events:{
            'click':'close',
            'click .route':'close',
            'click .close':'close',
            'rendered .bpt':'mayLoadMore',
            'scroll #index_popup_right':'mayLoadMore',
        },
        
        mayLoadMore:function(){
            this.$right.perfectScrollbar('update');
            if(this.$expander.filter(':visible').length > 0)
            {
                var nidx = this.newsItems.length;
                if(nidx >= this.news.length)
                {
                    this.$expander.remove();
                }
                else
                {
                    var ni = new blogPostTeaser({data:this.news[nidx]});
                    this.newsItems.push(ni);
                    ni.render().$el.appendTo(this.$container);
                    this.$right.perfectScrollbar('update');
                }
            }
        },
        
        activate:function(){
            this.mayLoadMore();
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
            'click .section':'setCurrentHandler',
        },
        setCurrentHandler:function(evt){
            var section = $(evt.target);
            this.setCurrent(section.attr('data-cat'));
        },
        setCurrent:function(cat){
            this.$('.section').removeClass('current');
            var section = this.$('[data-cat="'+cat+'"]')
            section.addClass('current');
        },
    });
    
    var siteTools = View.extend({
        className:'site-tools',
        initialize:function(){
            
        },
        render:function(){
            var $el = this.$el;
            var data = {
                next: Backbone.history.location.href,
            };
            T.render(tname('sitetools'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
        activate:function()
        {
            this.render();
        }
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
                var $ab = this.$('.article-box');
                $ab.perfectScrollbar({
                    wheelSpeed: 20,
                    minScrollbarLength: 20,
                })
                $ab.perfectScrollbar('update');
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
            this.rendered = false;
        },
        render:function(){
            this.rendered = false;
            var data = this.model.toJSON();
            T.render(tname('blog-post'), this, function(t){
                this.$el.html(t(data));
                this.rendered = true;
                this.trigger('rendered');
            });
            return this;
        },
    });
    
    var blog = View.extend({
        className:'blog',
        comparator:'pub_date',
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
                this.$el.perfectScrollbar('destroy');
                this.$el.html(t(data));
                bMa.Data.collections.blog.each(this.renderOne.bind(this));
                if(this.currentItem)
                {
                    this.selectItem(this.currentItem);
                }
                this.$el.perfectScrollbar({
                    wheelSpeed: 20,
                    minScrollbarLength: 20,
                })
                this.$el.perfectScrollbar('update');
            });
            return this;
        },
        
        activate:function(){
            if(this.currentItem)
            {
                this.selectItem(this.currentItem);
            }
        },
                           
        selectItem:function(slug){
            this.currentItem = slug;
            for(var k in this.items)
            {
                var ms = this.items[k].model.get('slug');
                if( ms && ms === slug)
                {
                    var item = this.items[k];
                    if(!item.rendered)
                    {
                        item.on('rendered',function(){
                            this.selectItem(slug);
                        }, this);
                        return;
                    }
                    var $el = item.$el;
                    item.model.set({selected:true})
                    var st = this.$el.scrollTop();
                    var pt = $el.position().top;
                    if(pt > st)
                    {
                        this.$el.scrollTop(pt);
                    }
                    this.currentItem = undefined;
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
            var $el = this.$el;
            var data = this.model.toJSON();
            T.render(tname('projectrow'), this, function(t){
                $el.html(t(data));
                $el.trigger('rendered');
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
                this.$tbody = this.$('.table-body');
                _.each(bMa.Data.Projects, function(p){
                    var m = new bMa.Models.Project({id:p.id});
                    this.renderOne(m);
                    m.fetch();
                }, this);
                this.$('#projects_table').stupidtable();
                $el.perfectScrollbar({
                    wheelSpeed: 20,
                    minScrollbarLength: 20,
                })
                $el.perfectScrollbar('update');
            });
            return this;
        },
        activate:function(){
//             this.projects.fetch();
        },
        
        events:{
            'rendered tr':'updateScrollbar',
        },
        
        updateScrollbar:function(){
            this.$el.perfectScrollbar('update');
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
                $el.trigger('resize');
            });
            return this;
        },
    });

    
    var projectViewer = View.extend({
        id:'project-box',
        className:'span4',
        initialize:function(){
            
        },
        
        render: function(){
            this.offset = 0;
            var $el = this.$el;
            $el.empty();
            if(this.project){
                $el.perfectScrollbar('destroy');
                $el.append(this.project.render().el);
                
                $el.perfectScrollbar({
                    wheelSpeed: 20,
                    minScrollbarLength: 20,
                })
                $el.perfectScrollbar('update');
                
            };
            return this;
        },
        
        activate: function(){
            this.$el.scrollTop(this.offset);
        },
        
        deactivate: function(){
            this.offset = this.$el.scrollTop();
        },
        
        events: {
            'resize .project':'updateScrollbar',
        },
        
        updateScrollbar: function(){
            this.$el.perfectScrollbar('update');
        },
        
        setModel:function(model){
            if(this.project
                && this.project.model
                && this.project.model.id
                && (this.project.model.id == model.id) ){
                return;
                }
            this.project = new project({model:model});
            return this.render();
        },
    }); 
    
    var carouselItem = View.extend({
        className: 'item',
        
        initialize:function(){
            
        },
        
        render: function(){
            var $el = this.$el;
            var data = {image:this.model};
            T.render(tname('carousel-item'), this, function(t){
                $el.html(t(data));
            });
            return this;
        },
    });
    
    var carousel = View.extend({
        className:'carousel-box',
        
        initialize:function(){
        },
        
        render:function(){
            this.items = {};
            if(this.model)
            {
                var $el = this.$el;
                var data = {};
                console.log(data);
                T.render(tname('carousel'), this, function(t){
                    $el.html(t(data));
                    var images = this.model.get('image');
                    if(images){
                        _.each(images, function(image){
                            this.renderOne(image);
                        }, this);
                    }
                });
            }
            return this;
        },
        
        setModel:function(model){
            if( this.model
                && this.model.id
                && (this.model.id == model.id) ){
                return;
            }
            if(this.model){
                this.model.off('change:image');
            }
            this.pendingSelectedImage = null;
            this.model = model;
            this.render();
            
            this.model.on('change:image', function(model){
                var images = this.model.get('image');
                if(images){
                    for(var idx = 0; idx < images.length; idx++){
                        if(!(images[idx].id in this.items)){
                            this.renderOne(images[idx]);
                        }
                    }
                }
            }, this);
        },
        
        renderOne: function(image){
            var item = new carouselItem({model:image});
            this.items[image.id] = item.render();
            this.$('.carousel-inner').append(item.el);
            if(this.pendingSelectedImage 
                && this.pendingSelectedImage === image.id){
                _.each(this.items, function(it){
                    it.removeClass('active');
                }, this);
                item.addClass('active');
            }
        },
        
        selectImage:function(image){
            if(image in this.items){
                _.each(this.items, function(item){
                    item.removeClass('active');
                }, this);
                this.items[image].addClass('active');
            }
            this.pendingSelectedImage = image;
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
    
    var contactForm = View.extend({
        className:'contact-form',
        initialize:function(){
            this.errors = undefined;
        },
        render:function(){
            T.render(tname('contact_form'), this, function(t){
                this.$el.html(t({}));
            });
            return this;
        },
        
        events:{
            'click .send-message':'submit',
        },
        
        submit:function(){
            var name = this.$('[name=name]').val();
            var from = this.$('[name=from]').val();
            var message = this.$('[name=message]').val();
            var csrf = this.$('[name=csrfmiddlewaretoken]').val();
            
            var m = new bMa.Models.Message({
                name:name,
                email:from,
                message:message,
            });
            
            m.save();
            window.router.navigate('index');
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
//                 this.map.on('whenReady', this.activate.bind(this));
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
        activate:function(){
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
                this._whenReady(function(){
                    map.fitBounds(p);
                });
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
    
    var backToMap = View.extend({
        className:'back-to-map',
        render:function(){
            T.render(tname('back_to_map'), this, function(t){
                this.$el.html(t({}));
            });
            return this;
        },
    });
    
    var vision = View.extend({
        className:'vision',
        initialize:function(){
            this.collection = bMa.Data.collections.vision;
            this.collection.on('add', this.render, this);
            this.collection.on('reset', this.render, this);
            
            this.current = 0;
        },
        render:function(){
            var data = {images:this.collection.toJSON()};
            console.log(data);
            T.render(tname('vision'), this, function(t){
                this.$el.html(t(data));
            });
            return this;
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
        ContactForm: contactForm,
        BackToMap: backToMap,
        Vision: vision,
    };
    
})();