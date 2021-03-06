/*
 Console.js
 
*/


window.bMa = window.bMa || {}

window.bMa.Console = function(container, map){
    var proto = {
        init:function(container, map){
            this.container = container;
            this.map = map;
            this.projects = {};
            this.items = {};
            
            var that = this;
            var interests = ['load','zoomend', 'moveend'];
            for(var ii = 0; ii < interests.length; ii++)
            {
                map.map.on(interests[ii], function(evt){
                    that.update();
                });
            }
        },
        add:function(project){
            this.projects[project.id] = project;
            var item = $('<div id="console_item_'+project.id+'" />');
            item.addClass('console_item');
            try
            {
                item.html(project.get('partners')[0][1] // FIXME 
                    +'<div class="item-project-name">'
                    +project.get('name')
                    +'</div>');
            }
            catch(e)
            {
                console.log(e.message, e.name);
            }
            this.container.append(item)
            this.items[project.id] = item;
            this.update();
        },
        update:function(){
            for(var id in this.projects)
            {
                var p = this.projects[id];
                var i = this.items[id];
                var lmap = this.map.map;
                var center = p.get('centroid').coordinates;
//                 console.log(center);
                var ctll = new L.LatLng(center[1], center[0]);
                var ctpos = lmap.latLngToContainerPoint(ctll);
                var visible = false;
                if(lmap.getBounds().contains(ctll))
                    visible = true;
                if(visible)
                {
                    i.removeClass('feature-hidden');
                    i.addClass('feature-visible');
                }
                else
                {
                    i.removeClass('feature-visible');
                    i.addClass('feature-hidden');
                }
                var map_offset = $(lmap.getContainer()).offset().top;
                var new_pos = map_offset + ctpos.y - this.container.offset().top;
                i.animate({top:new_pos + 'px'});
            }
        },
        highlight: function(id){
            for(var pid in this.items)
            {
                this.items[pid].removeClass('clicked-feature');
            }
            this.items[id].addClass('clicked-feature');
        },
        dehighlight:function(){
            for(var pid in this.items)
            {
                this.items[pid].removeClass('clicked-feature');
            }
        },
    };

    var ret = Object.create(proto);
    ret.init(container, map);
    return ret;
};