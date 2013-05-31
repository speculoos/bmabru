/*
 * 
 * app.js
 * 
 */

(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    
    var app = Backbone.View.extend({
        id:'body',
        initialize:function(){
            this.components = {};
            
            this.registerComponent('main_map', new bMa.Views.Map);
            this.registerComponent('navigation', new bMa.Views.Navigation);
            this.registerComponent('project', new bMa.Views.ProjectViewer);
            this.registerComponent('page', new bMa.Views.PageViewer);
            
            this.trigger('ready');
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
                if(c.visible)
                {
                    this.$el.append(c.view.el);
                    if(!c.rendered)
                    {
                        c.view.render();
                        c.rendered = true;
                    }
                    if(c.view.refresh)
                    {
                        c.view.refresh();
                    }
                    console.log('RENDERED',k);
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
    });
    
    
    bMa.App = app;
    
})();