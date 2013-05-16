/*
 * 
 * bMa.Thumbnailer.js
 * 
 * 
 */


window.bMa = window.bMa || {};

window.bMa.Thumbnailer = function(){
    var proto = {
        init:function(){
            this.$el = $('<div />').addClass('thumbnails-box');
            this.el = this.$el[0];
            this.$root = $('<ul>').addClass('thumbnails').appendTo(this.el);
            this.I = bMa.Image();
            this.setupEvents();
        },
        setImages:function(images){
            this.images = images;
            return this;
        },
        render:function(){
            this.$root.empty();
            var self = this;
            _.each(this.images, function(elt, idx){
                Template.render('bmabru/thumbnail', self ,function(t){
                    var html = t({src:elt});
                    self.$root.append(html);
                });
            });
            return this;
        },
        setupEvents: function(){
            this.$el.on('click','.thumbnail', {T:this}, function(evt){
                var T = evt.data.T;
                $('body').append(T.I.setImages(T.images).el);
            });
        },
        
    };
    
    var ret = Object.create(proto);
    ret.init();
    return ret;
};

