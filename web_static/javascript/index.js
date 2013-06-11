/*
 * 
 * index.js
 * 
 */


/// Included here for convenience
/*!
 * jquery.scrollto.js 0.0.1 - https://github.com/yckart/jquery.scrollto.js
 * Scroll smooth to any element in your DOM.
 *
 * Copyright (c) 2012 Yannick Albert (http://yckart.com)
 * Licensed under the MIT license (http://www.opensource.org/licenses/mit-license.php).
 * 2013/02/17
 **/
(function ($) { $.scrollTo = $.fn.scrollTo = function(x, y, options){ if (!(this instanceof $)) return $.fn.scrollTo.apply($('html, body'), arguments); options = $.extend({}, { gap: { x: 0, y: 0 }, animation: { easing: 'swing', duration: 600, complete: $.noop, step: $.noop } }, options); return this.each(function(){ var elem = $(this); elem.stop().animate({ scrollLeft: !isNaN(Number(x)) ? x : $(x).offset().left + options.gap.x, scrollTop: !isNaN(Number(y)) ? y : $(y).offset().top + options.gap.y }, options.animation); }); }; })(jQuery);



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