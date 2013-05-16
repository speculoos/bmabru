/*
 Legend.js
 */

window.bMa = window.bMa || {}

window.bMa.Legend = function(container, map)
{
    var proto = {
        init:function(container, map){
            this.container = container;
            this.map = map;
            this.container.parent().hide();
        },
        add_box:function(elem, label, content)
        {
            elem.empty();
            if(label)
                elem.append('<div class="project-info-label">'+label+'</div>');
            elem.append('<div class="project-info-box">'+content+'</div>');
        },
        show:function(project){
            var pbounds = project.bounds();
            if(pbounds.isValid())
                this.map.map.fitBounds(pbounds);
            
            Template.render('bmabru/project-box', this , function(t){
                this.container.html(t(_.extend({}, project.data) ));
            });
            this.container.parent().show();
        },
        hide:function(){
            this.container.parent().hide();
        },
    };
    
    var ret = Object.create(proto);
    ret.init(container, map);
    return ret;
};