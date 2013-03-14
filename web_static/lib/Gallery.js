/*
 * Gallery.js
 */



window.bMa = window.bMa || {}

window.bMa.Gallery = function(container)
{
    var proto = {
        init:function(container){
            this.container = container;
            this.container_stored_width = this.container.css('width');
            this.wrapper = $('<div class="gallery-container" />');
            this.image = $('<div class="gallery-image" />');
            this.back = $('<div class="gallery-control gallery-back">&lt;</div>');
            this.next = $('<div class="gallery-control gallery-next">&gt;</div>');
            this.note = $('<div class="gallery-note" />');
            
            this.container.append(this.wrapper);
            this.wrapper.append(this.image);
            this.wrapper.append(this.back);
            this.wrapper.append(this.next);
            this.wrapper.hide();
            
            this.ready = false;
            this.items = undefined;
            this.current = -1;
            var that = this;
            $.getJSON('/media/json/subjective_images/',function(data){
                that.items = data;
                that.ready = true;
                for(var i=0; i < that.items.length; i++)
                {
                    var item = that.items[i];
                    var image = $('<img src="'+item.url+'" />');
                    item.image = image;
                }
            });
            
            
            this.back.on('click',function(evt){
                that.show_previous();
                
            });
            this.next.on('click',this.show_next);
            
            this.container.on('click', function(){
                if(that.wrapper.is(':visible'))
                {
                    that.hide();
                }
                else
                {
                    that.show();
                }
            });
            
        },
        show:function(){
            this.container.css('width','100%');
            this.wrapper.show(1000);
            if(this.current < 0)
                this.show_next();
        },
        hide:function(){
            this.container.css('width',this.container_stored_width);
            this.wrapper.hide(1000);
        },
        show_next:function(){
            this.current += 1;
            if(this.current > this.items.length)
                this.current = 0;
            this.show_complete();
        },
        show_previous:function(){
            this.current -= 1;
            if(this.current < 0)
                this.current = this.items.length - 1;
            this.show_complete();
        },
        show_complete:function(){
            this.image.empty();
            var item = this.items[this.current];
            this.image.append(item.image);
            this.note.html(item.note);
        },
    };
    
    var ret = Object.create(proto);
    ret.init(container);
    return ret;
};