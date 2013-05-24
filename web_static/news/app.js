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
        postRender:function(data){
            if(data.selected)
            {
                this.$el.addClass('selected');
            }
            else
            {
                this.$el.removeClass('selected');
            }
        },
    };
    
    var ResourceProto = {
        tagName:'li',
        className:'span3',
    };
    
    var ProjectModelProto = {
        deps : [{attr:'project',model:'projects'}],
    };
    
    var ProjectProto = {
        className:'accordion-group',
    };
    
    
    var ItemCollectionProto = {
        comparator:function(a,b){
            var da = new Date(a.get('pub_date')).getTime();
            var db = new Date(b.get('pub_date')).getTime();
            return db - da;
        },
    };
    
    var AppView =  Backbone.View.extend({
        className:'container-fluid',
        id:'app',
        initialize:function(){
            $('body').append(this.el);
            this.r0 = $('<div>').addClass('row-fluid title-box').appendTo(this.el);
            this.r1 = $('<div>').addClass('row-fluid main-box').appendTo(this.el);
            this.navBox = $('<div>').addClass('span3 navbox').appendTo(this.r1);
            this.workSpace = $('<div>').addClass('span9  workSpace').appendTo(this.r1);
            
            this._compStack = [];
            
            NEWS.Modeler(function(){
                _.extend(NEWS.Views.items.prototype, ItemProto);
                _.extend(NEWS.Views.resources.prototype, ResourceProto);
                _.extend(NEWS.Views.projects.prototype, ProjectProto);
                _.extend(NEWS.Collections.items.prototype, ItemCollectionProto);
                
                this.registerComponent('form', new NEWS.Views.PostView({model:new NEWS.Models.items}));
                this.registerComponent('post_images', new NEWS.Views.PostImagesView);
                this.registerComponent('projects', new NEWS.Views.ProjectsView);
                this.registerComponent('images', new NEWS.Views.NewsImagesView);
                this.registerComponent('new_image', new NEWS.Views.NewImageView);
                
                this.titleBar = new NEWS.Views.TitleView;
                this.items = new NEWS.Views.ItemsView;
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
        getComponent:function(comp){
            if(this.components[comp] === undefined)
                return null;
            return this.components[comp].view;
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
            for(var i=0; i<comps.length; i++)
            {
                var c = comps[i];
                if(this.components[c].view.activate)
                    this.components[c].view.activate(this);
            }
            
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
            this.current_comps = comps;
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
            if(this.components[comp].view.activate)
                this.components[comp].view.activate();
            this.components[comp].visible = true;
        },
        saveComponents:function(){
            var state = {};
            for(var k in this.components){
                var c = this.components[k];
                state[k] = c.visible;
            }
            this._compStack.push(state);
        },
        restoreComponents:function(){
            if(this._compStack.length === 0)
                return;
            var state = this._compStack.pop();
            for(var k in state)
            {
                this.components[k].visible = state[k];
            }
            this.render();
        },
        newForm:function(){
            var item = new NEWS.Models.items;
            var self = this;
            this.components.form.view.confirmLeave(function(){
                self.components.form.view.resetModel(item);
                self.components.post_images.view.setImages([]);
            });
        },
        editForm:function(id){
            var item = this.items.newsItems.get(id);
            var self = this;
            this.components.form.view.confirmLeave(function(){
                self.components.form.view.resetModel(item);
                self.components.post_images.view.setImages([]);
            });
        },
        removePost:function(model){
            model.destroy();
            window.router.navigate('index');
        },
    });
    NEWS.App = AppView;
})();