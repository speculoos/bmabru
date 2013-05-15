/*
 * 
 * NEWS.index.js
 * 
 * 
 */


$(document).ready(function(){
    $('body').on('click', '.link', function(evt){
        var that = $(this);
        that.addClass('visited');
        window.router.navigate(that.attr('data-route'));
    });
    
    window.app = new NEWS.App;
    
    window.app.on('ready', function(){
        
        window.router = new NEWS.Router;
        var route = Backbone.history.start({pushState: false});
        if(!route)
        {
            window.router.navigate('index');
        }
        
    });
});