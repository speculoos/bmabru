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
        url:'/api/pages/',
        model: bMa.Models.Page,
    });
    
    var project = Backbone.Collection.extend({
        url:'/api/projects/',
        model: bMa.Models.Project,
    });
    
    var blog = Backbone.Collection.extend({
        url:'/api/items/',
        model: bMa.Models.BlogPost,
        comparator:function(a,b){
            var da = new Date(a.get('pub_date')).getTime();
            var db = new Date(b.get('pub_date')).getTime();
            var ret = db - da;
            return ret;
        },
    });
    
    bMa.Collections = {
        Page: page,
        Project : project,
        Blog : blog,
    };
    
    bMa.Data.collections = {
        pages: new page,
        projects: new project,
        blog: new blog,
    };
    
})();

