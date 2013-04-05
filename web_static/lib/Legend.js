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
            this.wrapper = $('<div class="project-box"></div>');
            var elems = 'title description address city partnership'.split(' ');
            this.elements = {};
            for(var i=0; i < elems.length; i++)
            {
                var ename = elems[i];
                this.elements[ename] = $('<div class="project-'+ename+'" />');
                this.wrapper.append(this.elements[ename]);
            }
            this.container.append(this.wrapper);
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
            
            this.add_box(this.elements.title, 
                         null, 
                         '<a class="project-link" href="/project/'+project.get('slug')+'">'+project.get('name')+'</a>');
            
            this.add_box(this.elements.description, 
                         null, 
                         project.get('description'));
            
            this.add_box(this.elements.address, 
                         'adresse', 
                         project.get('address'));
            
            this.add_box(this.elements.city,
                        'Commune',
                         project.get('city').zipcode + ' ' + project.get('city').name);
            
            var partnerships = project.get('partnerships');
            var pstring = '';
            for(var i=0; i < partnerships.length; i++)
            {
                partner = partnerships[i].partner;
                ptype = partnerships[i].ptype;
                pstring += '<div class="partneship-item"> <span class="project-partnership-type">'+ptype.name+'</span> '
                + '<span class="project-partnership-type">'+partner.name+'</span> </div>';
            }
            
            this.add_box(this.elements.partnership,
                         'Interventions',
                         pstring);
            
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