/*
 * 
 * bMa.Image.js
 * 
 * 
 */


window.bMa = window.bMa || {};

window.bMa.Image = function(){
    var proto = {
        init:function(){
            this.$el = $('<div />').addClass('image-box');
            this.el = this.$el[0];
            this.setupEvents();
        },
        setImages:function(images){
            this.images = images;
            return this.render();
        },
        render:function(){
            Template.render('bmabru/image', this ,function(t){
                var html = t({images:this.images});
                this.$el.append(html);
            });
            return this;
        },
        setupEvents:function(){
            
        },
    };
    
    var ret = Object.create(proto);
    ret.init();
    return ret;
};