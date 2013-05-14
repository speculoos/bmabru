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
    
    var ItemsView = Backbone.View.extend({
        tagName:'ul',
        className:'nav nav-list',
        initialize:function(){
            this.newsItems = new NEWS.Collections.items;
            this.newsItems.on('add', this.renderOne, this);
            this.newsItems.on('reset', this.render, this);
            this.items = {};
            this.newsItems.fetch();
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
    
    var PostView = Backbone.View.extend({
        className:'news-form',
        initialize:function(){
            this.model.on('change', this.render, this);
            if(!this.model.isNew())
            {
                this.render();
            }
        },
        render: function() {
            var $el = this.$el;
            $el.attr('id', 'news_form_' + this.model.id)
            $el.empty();
            var data = this.model.toJSON();
            Template.render(this.className, this, function(t){
                $el.html(t(data));
            });
            return this;
        },
        resetModel:function(model) {
            this.model = model;
            this.render();
        },
        events:{
            'click .submit':'save',
        },
        serialize:function(){
            var ret = {};
            ret.title = this.$el.find('[name=title]').val();
            ret.body = this.$el.find('[name=body]').val();
            ret.resource = '';
            ret.project = '';
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
        }
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
                
                this.registerComponent('form', new PostView({model:new NEWS.Models.items}));
                
                this.titleBar = new TitleView;
                this.items = new ItemsView;
                this.r0.append(this.titleBar.render().el);
                this.navBox.append(this.items.render().el);
                this.trigger('ready');
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
        },
        editForm:function(id){
            var item = this.items.newsItems.get(id);
            this.components.form.view.resetModel(item);
        },
    });
    NEWS.App = AppView;
})();