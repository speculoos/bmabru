/*
 * 
 * models.js
 * 
 */



(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    
    var page = Backbone.Model.extend({
        urlRoot:'/api/pages/',
        idAttribute:'id',
    });
    
    var project = Backbone.Model.extend({
        urlRoot:'/api/projects/',
        idAttribute:'id',
    });
    
    bMa.Models = {
        Page: page,
        Project : project,
    };
    
})();