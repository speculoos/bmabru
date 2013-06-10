/*
 * 
 * index.js
 * 
 */

for(var f in 'append remove detach appendTo'.split(' ')){
    (function($) {
        var origAppend = $.fn[f];
        
        $.fn[f] = function () {
            return origAppend.apply(this, arguments).trigger(f);
        };
    })(jQuery);
}

$(document).on('resize', '*', function(evt){
    console.log('resize', evt);
});

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