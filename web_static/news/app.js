/*
 * 
 * NEWS.app.js
 * 
 */

(function(undefined){
    'strict';
    var NEWS = window.NEWS;
    var Backbone = window.Backbone;
    
    var ItemProto = {
        tagName: "li",
    };
    
    var ResourceProto = {
        tagName:'li',
        className:'span2',
    };
    
    var ProjectModelProto = {
        deps : [{attr:'project',model:'projects'}],
    };
    
    var ProjectProto = {
        className:'accordion-group',
    };
    
    var ItemsView = Backbone.View.extend({
        tagName:'ul',
        className:'nav nav-list',
        initialize:function(){
            this.newsItems = new NEWS.Collections.items;
            this.newsItems.on('add', this.renderOne, this);
            this.newsItems.on('reset', this.render, this);
            this.items = {};
            
            this._ready = false;
            this.newsItems.on('reset', function(){
                if(!this._ready)
                {
                    this._ready = true;
                    this.trigger('ready');
                }
            }, this);
            
            this.newsItems.fetch({reset:true});
        },
        renderOne: function(item){
            if(this.items[item.cid] === undefined)
            {
                item.set({
                    visited:false,
                    current:false,
                });
                var i = new NEWS.Views.items({model:item});
                var el = i.render().el;
                this.$el.append(el);
                this.items[item.cid] = i;
            }
            return this;
        },
        render: function(){
            this.$el.empty();
            Template.render('item-list', this, function(t){
                this.$el.html(t({}));
                this.newsItems.each(function(item){
                    this.renderOne(item);
                }, this);
            });
            
            return this;
        },
    });
    
    
    var ProjectsView = Backbone.View.extend({
        className:'projects well span3',
        initialize:function(){
            this.projects = new NEWS.Collections.projects;
//             this.projects.on('add', function(){
//                 this.render();
//             }, this);
            this.projects.on('reset', function(){
                this.projects_ready = true;
                this.render();
            }, this);
//             this.items = {};
            this.projects_ready = false;
            this.projects.fetch({reset:true});
        },
        renderOne: function(item, options){
            options = _.extend({open:false}, options);
            var i = new NEWS.Views.projects({model:item});
            console.log(item.toJSON());
            var el = i.render().el;
            if(options.open)
            {
                i.$el.find('.accordion-body').addClass('in');
            }
            var $root = this.$el.find('.accordion');
            if($root.length > 0)
            {
                $root.append(el);
            }
            return this;
        },
        render: function(){
            this.$el.empty();
            Template.render('projects-list', this, function(t){
                this.$el.html(t({
                    ready:this.projects_ready,
                }));
                }, this);
            return this;
        },
        events:{
            'click .search-submit':'search',
            'click .select': 'select',
        },
        search:function(evt){
            evt.preventDefault();
            this.$el.find('.accordion').empty();
            var re = new RegExp(this.$el.find('.search-q').val(), "i");
            var self = this;
            var items = [];
            this.projects.each(function(item, idx){
                var name = item.get('name');
                if(re.test(name))
                {
                    var res = re.exec(name);
                    items.push({item:item,m:res.length});
                }
            });
            items.sort(function(a, b) {
                return a.m - b.m;
            });
            for(var i=0; i < items.length; i++){
                 this.renderOne(items[i].item, {open:(i === 0)});
            }
        },
        select:function(evt){
            var el = $(evt.target);
            var id = el.attr('data-pid');
            window.app.components.form.view.setProject(id);
        },
    });
    
    var TitleView = Backbone.View.extend({
        id:'titlebar',
        tagName:'ul',
        className:'breadcrumb',
        initialize:function(){
            this.elements = ['News'];
        },
        setElements:function(elts){
            this.elements = elts;
            this.render();
        },
        render:function(){
            this.$el.empty();
            var dvdr = ' <span class="divider">::';
            for(var i = 0; i < this.elements.length; i++)
            {
                if(i === (this.elements.length - 1))
                    dvdr = '';
                this.$el.append('<li>'+this.elements[i]+dvdr+'</li>');
            }
            return this;
        },
    });
    
    var PostImagesView = Backbone.View.extend({
        className:'images well span3',
        initialize:function(){
            this.images = [];
        },
        render:function(){
            this.$el.empty();
            if(this.images.length > 0)
                this.$el.show();
            else
                this.$el.hide();
            Template.render('images', this, function(t){
                this.$el.html(t({images:this.images}));
                }, this);
            
            return this;
        },
        setImages:function(images){
            this.images = images;
            this.render();
        },
        events:{
            'click .image-selector':'select',
        },
        select: function(evt){
            var btn = $(evt.target);
            window.app.components.form.view.model.set({image_url:btn.attr('data-image')});
        },
    });
    
    var NewsImagesView = Backbone.View.extend({
        className:'row-fluid news-images-box',
        initialize:function(){
            this.images = new NEWS.Collections.resources;
            this.images.on('add', this.renderOne, this);
            this.images.on('reset', this.render, this);
            this.items = {};
            this.images.fetch();
        },
        renderOne: function(item){
            if(this.items[item.cid] === undefined)
            {
                item.set({
                    visited:false,
                    current:false,
                });
                var i = new NEWS.Views.resources({model:item});
                var el = i.render().el;
                var $root = this.$el.find('.thumbnails');
                if($root.length > 0)
                {
                    $root.append(el);
                    this.items[item.cid] = i;
                }
            }
            return this;
        },
        render: function(){
            this.$el.empty();
            Template.render('resources-list', this, function(t){
                this.$el.html(t({}));
                this.images.each(function(item){
                    this.renderOne(item);
                }, this);
            });
            
            return this;
        },
    });
    
    var PostView = Backbone.View.extend({
        className:'news-form',
        comparator:'pub_date',
        initialize:function(){
            this.resetModel(this.model);
        },
        render: function() {
            var $el = this.$el;
            $el.empty();
            var data = this.model.toJSON();
            Template.render(this.className, this, function(t){
                $el.html(t(data));
            });
            return this;
        },
        fillProjectData:function(){
            var id = this.model.get('project');
            var projects = window.app.components.projects.view.projects;
            var project = projects.get(id);
            if(project)
            {
                this.model.set({
                    project_data: project.toJSON(),
                });
            }
        },
        resetModel:function(model) {
            this.model = model;
            if(this.model.get('project') 
                && !this.model.get('project_data'))
            {
                this.fillProjectData();
            }
            this.render();
            this.model.on('change:project', function(){
                this.fillProjectData;
            }, this)
            this.model.on('change', this.render, this);
        },
        setProject:function(id){
            this.model.set({ project:id, });
        },
        events:{
            'click .submit':'save',
            'click .parser':'parser',
            'click .reset-project':'resetProject',
        },
        resetProject:function(){
            this.model.set({project:null});
        },
        serialize:function(){
            var ret = {};
            ret.title_fr = this.$el.find('[name=title_fr]').val();
            ret.body_fr = this.$el.find('[name=body_fr]').val();
            ret.title_nl = this.$el.find('[name=title_nl]').val();
            ret.body_nl = this.$el.find('[name=body_nl]').val();
            if(ret.title_fr === '')
                ret.title_fr = 'translation not available';
            if(ret.body_fr === '')
                ret.body_fr = 'translation not available';
            if(ret.title_nl === '')
                ret.title_nl = 'translation not available';
            if(ret.body_nl === '')
                ret.body_nl = 'translation not available';
            ret.title = '@fr @nl';
            ret.body = '@fr @nl';
            
            ret.resource = '';
            ret.project = parseInt(this.$el.find('[name=project]').val());
            return ret;
        },
        save:function(){
            var model = this.model;
            var submit = this.$el.find('.submit');
            var data = this.serialize();
            
            submit.button('loading');
            model.once('sync',function(){
                submit.button('reset');
                window.app.items.newsItems.add(model);
            });
            model.save(data);
        },
        parser:function(){
            var urlElt = this.$el.find('[name=parse_url]');
            var btn = this.$el.find('.parser');
            btn.button('loading');
            var url = urlElt.val();
            urlElt.val('');
            var self = this;
            $.ajax({
                url:NEWS.Config.PARSER_URL,
                type: "POST",
                data:{url:url},
                dataType:'json'
            }).done(function(data){
                console.log(data);
                self.$el.find('[name=title]').val(data.meta.title);
                var body = [url];
                if(data.meta.description)
                {
                    body.push(data.meta.description);
                }
                else
                {
                    if(data.content.length > 0)
                        body.push(data.content[0]);
                }
                self.$el.find('[name=body]').val(body.join('\n\n'));
                
                window.app.components.images.view.setImages(data.images);
                
                btn.button('reset');
            });
        },
    });
    
    var AppView =  Backbone.View.extend({
        className:'container-fluid',
        id:'app',
        initialize:function(){
            $('body').append(this.el);
            this.r0 = $('<div>').addClass('row-fluid title-box').appendTo(this.el);
            this.r1 = $('<div>').addClass('row-fluid main-box').appendTo(this.el);
            this.navBox = $('<div>').addClass('span3 navbox').appendTo(this.r1);
            this.workSpace = $('<div>').addClass('span9  workSpace').appendTo(this.r1);
            
            
            NEWS.Modeler(function(){
                _.extend(NEWS.Views.items.prototype, ItemProto);
                _.extend(NEWS.Views.resources.prototype, ResourceProto);
                _.extend(NEWS.Views.projects.prototype, ProjectProto);
                
                this.registerComponent('form', new PostView({model:new NEWS.Models.items}));
                this.registerComponent('post_images', new PostImagesView);
                this.registerComponent('projects', new ProjectsView);
                this.registerComponent('images', new NewsImagesView);
                
                this.titleBar = new TitleView;
                this.items = new ItemsView;
                this.items.on('ready', function(){
                    this.trigger('ready');
                },this);
                
                this.r0.append(this.titleBar.render().el);
                this.navBox.append(this.items.render().el);
//                 this.workSpace
                
            }, this);
        },
        registerComponent: function(name, view){
            if(this.components === undefined)
            {
                this.components = {};
            }
            this.components[name] = {
                view:view,
                visible:false,
                rendered: false,
            }
        },
        render:function(){
            for(var k in this.components){
                var c = this.components[k];
                console.log(k, c.visible, c.rendered);
                if(c.visible)
                {
                    this.workSpace.append(c.view.el);
                    if(!c.rendered)
                    {
                        c.view.render();
                        c.rendered = true;
                    }
                }
                else
                {
                    c.view.$el.detach();
                }
            }
        },
        resetViews:function(comps){
            for(var i=0; i<comps.length; i++)
            {
                var c = comps[i];
                try{
                    this.components[c].rendered = false;
                }
                catch(e){
                    //                     console.log('Could not reset: '+c);
                }
            }
            this.render();
        },
        setComponents:function(comps){
            console.log(comps);
            this.current_comps = comps;
            for(var k in this.components){
                var c = this.components[k];
                c.visible = false;
                c.view.$el.detach();
            }
            for(var i=0; i<comps.length; i++)
            {
                var c = comps[i];
                try{
                    this.components[c].visible = true;
                }
                catch(e){
                    //                     console.log('Could not activate: '+c);
                }
            }
            this.render();
        },
        unsetComponent:function(comp){
            if(this.components[comp] === undefined)
                return;
            this.components[comp].visible = false;
        },
        setComponent:function(comp){
            if(this.components[comp] === undefined)
                return;
            this.components[comp].visible = true;
        },
        newForm:function(){
            var item = new NEWS.Models.items;
            this.components.form.view.resetModel(item);
//             this.components.post_images.view.setImages([]);
        },
        editForm:function(id){
            var item = this.items.newsItems.get(id);
            this.components.form.view.resetModel(item);
//             this.components.post_images.view.setImages([]);
        },
    });
    NEWS.App = AppView;
})();