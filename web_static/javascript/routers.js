/*
 * 
 * routers.js
 * 
 */


(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    
    var findMedia = function(slug)
    {
        var medias = bMa.Data.Medias;
        for(var cat in medias)
        {
            for(var p in medias[cat])
            {
                var page = medias[cat][p];
                if(page.slug === slug)
                {
                    return page;
                }
            }
        }
    }
    
    var main = Backbone.Router.extend({
        navigate:function(route, options){
            options = _.extend({trigger: true}, options);
            Backbone.Router.prototype.navigate.apply(this, [route, options]);
        },
        
        routes:{
            '': 'index',
            'index': 'index',
            'page/:slug' :'page',
            'project/:slug':'project',
            'city/:city':'city',
            'function/:func':'func',
            'projects':'projects',
        },
        
        index:function(){
            window.app.send('main_map', 'removeClass', 'partial');
            window.app.setComponents('navigation sitetools main_map maptools'.split(' '));
        },
        page:function(slug){
            if(bMa.Data.collections.pages.findWhere({slug:slug}))
            {
                window.app.getComponent('page')
                .setModel(bMa.Data.collections.pages.findWhere({slug:slug}));
                window.app.setComponents('navigation sitetools page'.split(' '));
            }
            else if(findMedia(slug))
            {
                var page = new bMa.Models.Page({id:findMedia(slug).id});
                bMa.Data.collections.pages.add(page);
                page.fetch();
                window.app.getComponent('page').setModel(page);
                window.app.setComponents('navigation sitetools page'.split(' '));
            }
            else
            {
                this.navigate('index');
            }
        },
        project:function(slug){
            window.app.send('main_map', 'addClass', 'partial');
            if(bMa.Data.collections.projects.findWhere({slug:slug}))
            {
                window.app.getComponent('project')
                    .setModel(bMa.Data.collections.projects.findWhere({slug:slug}));
                window.app.setComponents('navigation sitetools main_map maptools project'.split(' '));
            }
            else if(bMa.Data.Projects[slug])
            {
                var project = new bMa.Models.Project({id:bMa.Data.Projects[slug].id});
                bMa.Data.collections.projects.add(project);
                project.fetch();
                window.app.getComponent('project').setModel(project);
                window.app.setComponents('navigation sitetools main_map maptools project'.split(' '));
            }
            else
            {
                this.navigate('index');
            }
        },
        city:function(city){
            window.app.send('main_map', 'removeClass', 'partial');
            window.app.setComponents('navigation sitetools main_map maptools'.split(' '));
            window.app.send('main_map', 'filterCity', city);
        },
        func:function(func){
            window.app.send('main_map', 'removeClass', 'partial');
            window.app.setComponents('navigation sitetools main_map maptools'.split(' '));
            window.app.send('main_map', 'filterFunction', func);
        },
        projects:function(){
            
        },
    });
    
    bMa.Routers = {
        Main: main,
    };
    
})();