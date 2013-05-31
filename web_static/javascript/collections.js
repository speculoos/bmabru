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
    
    bMa.Collections = {
        Page: page,
        Project : project,
    };
    
    bMa.Data.collections = {
        pages: new page,
        projects: new project,
    };
    
})();

