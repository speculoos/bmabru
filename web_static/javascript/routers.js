/*
 * 
 * routers.js
 * 
 */


(function(undefined){
    'strict';
    var bMa = window.bMa;
    var Backbone = window.Backbone;
    
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
        },
        
        index:function(){
            window.app.setComponents('main_map'.split());
        },
    });
    
    bMa.Routers = {
        Main: main,
    };
    
})();