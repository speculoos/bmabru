/*
 Legend.js
 */

window.bMa = window.bMa || {}

window.bMa.Legend = function(container)
{
    var proto = {
        init:function(container){
            this.container = container;
            this.container.hide();
            this.wrapper = $('<div class="short-description"></div>');
            this.title = $('<div class="description-title"></div>');
            this.content = $('<div class="description-wrapper"></div>');
            this.container.append(this.wrapper);
            this.wrapper.append(this.title);
            this.wrapper.append(this.content);
        },
        show:function(project){
            this.title.text(project.get('name'));
            this.content.text(project.get('description'));
            this.container.show();
        },
        hide:function(){
            this.container.hide();
        },
    };
    
    var ret = Object.create(proto);
    ret.init(container);
    return ret;
};