/*
 * 
 * NEWS.index.js
 * 
 * 
 */


$(document).ready(function(){
    window.app = new NEWS.App;
    
    window.app.on('ready', function(){
        
        window.router = new NEWS.Router;
        Backbone.history.start({pushState: false});
        
        $('body').on('click', '.link', function(evt){
            var that = $(this);
            that.addClass('visited');
            window.router.navigate(that.attr('data-route'));
        });
    });
});