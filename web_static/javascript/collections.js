/*
 * 
 * collections.js
 * 
 */

(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    
    var page = Backbone.Collection.extend({
        url:'/api/media/pages/',
        model: bMa.Models.Page,
    });
    
    var project = Backbone.Collection.extend({
        url:'/api/bmabru/projects/',
        model: bMa.Models.Project,
    });
    
    var blog = Backbone.Collection.extend({
        url:'/api/news/items/',
        model: bMa.Models.BlogPost,
        comparator:function(a,b){
            var da = new Date(a.get('pub_date')).getTime();
            var db = new Date(b.get('pub_date')).getTime();
            var ret = db - da;
            return ret;
        },
    });
    
    var vision = Backbone.Collection.extend({
        url:'/api/media/subjectiveimages/',
        model: bMa.Models.Vision,
        comparator:'order',
    });
    
    
    bMa.Collections = {
        Page: page,
        Project : project,
        Blog : blog,
        Vision : vision,
    };
    
    bMa.Data.collections = {
        pages: new page,
        projects: new project,
        blog: new blog,
        vision : new vision,
    };
    
})();

