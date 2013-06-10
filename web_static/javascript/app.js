/*
 * 
 * app.js
 * 
 */

(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    var HL = window.HorizontalLayout;
    var VL = window.VerticalLayout;
    

    var app = Backbone.View.extend({
        id:'container',
        initialize:function(){
            
            this.setupLayout();
            
            this.registerComponent('navigation', new bMa.Views.Navigation, 'header', 6);
            this.registerComponent('sitetools', new bMa.Views.SiteTools, 'header', 1);
            
            this.registerComponent('project', new bMa.Views.ProjectViewer, 'viewport', 4);
            this.registerComponent('page', new bMa.Views.PageViewer, 'viewport', 12);
            this.registerComponent('main_map', new bMa.Views.Map, 'viewport', 12-4);
            this.registerComponent('maptools', new bMa.Views.MapTools, 'viewport', 1);
            
            this.trigger('ready');
            this.$el.appendTo('body');
            $(window).on('resize', this.adjustViewport.bind(this));
        },
        setupLayout:function(){
            this.layouts = {
                header:$('<div />'),
                viewport:$('<div />'),
            };
            
            for(var l in this.layouts)
            {
                this.layouts[l].attr('id',l).appendTo(this.el);
            }
            
            
        },
        adjustViewport:function(){
            return;
            var top =  this.layouts.header.$el.outerHeight(true);
            var bottom = this.layouts.footer.$el.outerHeight(true);
            var total = this.$el.height();
            var newHeight = total - (bottom + top);
            console.log(total, newHeight);
            this.layouts.viewport.$el.height(newHeight);
        },
        events:{
            'resize':'adjustViewport',
        },
        registerComponent: function(name, view, parent, size){
            if(this.components === undefined)
            {
                this.components = {};
            }
            this.components[name] = {
                view:view,
                visible:false,
                rendered: false,
                layout: parent,
                size:size,
            }
        },
        send:function(comp, method, args){
            if(!Array.isArray(args))
                args = [args];
            var view = this.getComponent(comp);
            if(view && view.deliver)
                view.deliver(method, args);
                
        },
        getComponent:function(comp){
            if(this.components[comp] === undefined)
                return null;
            return this.components[comp].view;
        },
        render:function(){
            for(var k in this.components){
                var c = this.components[k];
                if(c.visible)
                {
                    this.layouts[c.layout].append(c.view.el);
//                     this.layouts[c.layout].add(c.view, c.size);
//                     this.$el.append(c.view.el);
                    if(!c.rendered)
                    {
                        c.view.render();
                        c.rendered = true;
                    }
                    
                    // at least we have a method which is always called
                    // when a view is made visible
                    if(c.view.refresh)
                    {
                        c.view.refresh();
                    }
                }
            }
//             for(var l in this.layouts)
//             {
//                 this.layouts[l].render();
//             }
//             
//             this.adjustViewport();
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
    });
    
    
    bMa.App = app;
    
})();