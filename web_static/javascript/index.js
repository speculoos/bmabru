/*
 * 
 * index.js
 * 
 */


$(document).ready(function(){
    'strict';
    var bMa = window.bMa;
    
    window.app = new bMa.App;
    window.router = new bMa.Routers.Main;
    window.Backbone.history.start({pushState: false});
    
    $('body').on('click', '.route', function(evt){
        var that = $(this);
        that.addClass('visited');
        window.router.navigate(that.attr('data-route'));
    });
    
    app.render();
    
});