/*
 * 
 * index.js
 * 
 */


$(document).ready(function(){
    'strict';
    var bMa = window.bMa;
    
    $('body').on('click', '.route', function(evt){
        var that = $(this);
        that.addClass('visited');
        window.router.navigate(that.attr('data-route'));
    });
    
    $('body').on('click', '.back', function(evt){
        window.router.back();
    });
    
    
    window.app = new bMa.App;
    app.once('ready', function(){
        window.router = new bMa.Routers.Main;
        window.Backbone.history.start({pushState: false});
        app.render();
    });
    window.app.start();
    
});