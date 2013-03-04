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
            this.wrapper = $('<div class="project-box"></div>');
            var elems = 'title description address city partners'.split(' ');
            this.elements = {};
            for(var i=0; i < elems.length; i++)
            {
                var ename = elems[i];
                this.elements[ename] = $('<div class="project-'+ename+'" />');
                this.wrapper.append(this.elements[ename]);
            }
            this.container.append(this.wrapper);
        },
        show:function(project){
            var proj_name = $('<a class="project-link" href="/project/'+project.get('slug')+'">'+project.get('name')+'</a>');
            this.elements.title.empty();
            this.elements.title.append(proj_name);
            this.elements.description.text(project.get('description'));
            this.elements.address.text(project.get('address', 1));
            this.elements.city.text(project.get('city', 1) + ' ' + project.get('city', 2));
            var partners = project.get('partners');
            var pstring = '';
            var sep = '';
            for(var i=0; i<partners.length; i++)
            {
                pstring += sep + partners[i][1];
                sep = ', ';
            }
            this.elements.partners.text(pstring);
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