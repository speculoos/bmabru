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
//         initialize:function(){
//             this.on('change:functions', this.populateFunctions.bind(this));
//         },
    });
    
    var blogPost = Backbone.Model.extend({
        urlRoot:'/api/items/',
        idAttribute:'id',
    });
    
    var message = Backbone.Model.extend({
        urlRoot:'/api/messages/',
        idAttribute:'id',
    });
    
    var vision = Backbone.Model.extend({
        urlRoot:'/api/subjectiveimages/',
        idAttribute:'id',
    });
    
    
    bMa.Models = {
        Page: page,
        Project : project,
        BlogPost : blogPost,
        Message : message,
        Vision: vision,
    };
    
})();