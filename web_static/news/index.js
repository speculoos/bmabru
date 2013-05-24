/*
 * 
 * NEWS.index.js
 * 
 * 
 */

Number.prototype.pad = function(size){
    if(typeof(size) !== "number"){size = 2;}
    var s = String(this);
    while (s.length < size) s = "0" + s;
       return s;
    }

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