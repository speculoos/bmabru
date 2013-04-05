/*
 * Filter.js
 */


window.bMa = window.bMa || {}

window.bMa.Filter = function(container, map){
    
    var proto = {
        init:function(container, map){
            this.container = container;
            this.map = map;
            this.filters = {};
            var that = this;
            
            this.selector = bMa.Selector(container, 'Filtre Projets');
            this.selector.add_item('Tout les projets',{
                click:function(evt){
                    that.reset(true);
                }},
                'filter-reset');

            this.cities = {};
            this.functions = {};
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                var city_data = project.get('city');
                var city = city_data.zipcode + ' ' + city_data.name;
                if(this.cities[city] === undefined)
                {
                    this.cities[city] = {
                        node:city,
                        zip:city_data.zipcode ,
                        projects:[]
                    };
                }
                this.cities[city].projects.push(project);
                
                var fn_a = project.get('functions');
                if(fn_a.length > 0)
                {
                    var fn = fn_a[0].name;
                    if(this.functions[fn] === undefined)
                    {
                        this.functions[fn] = {
                            node:fn,
                            projects:[]
                        };
                    }
                    this.functions[fn].projects.push(project);
                }
                
            }
            
            var cties_a = Object.keys(this.cities);
            cties_a.sort(function(a,b){
                if (a.zip < b.zip)
                    return 1;
                if (a.zip > b.zip)
                    return -1;
                return 0;
            });
            
            this.selector.add_label('Communes');
            for(var k in cties_a)
            {
                console.log(cties_a[k]);
                this.selector.add_item(cties_a[k], {
                    click:{
                        callback:function(evt){
                        that.filter_city(evt.data.city);
                        },
                        data:{
                            city:cties_a[k]
                        }
                    }
                });
            }
            
            this.selector.add_label('Fonctions');
            for(var k in this.functions)
            {
                this.selector.add_item(k, {
                    click:{
                        callback:function(evt){
                            that.filter_function(evt.data.fn);
                        },
                        data:{
                            fn:k
                        }
                    }
                });
            }
            
        },
        reset:function(show){
            var bounds = undefined;
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                if(show)
                    project.show_layer();
                else
                    project.hide_layer();
                if(bounds === undefined)
                {
                    if(project.bounds().isValid())
                        bounds = project.bounds();
                }
                else
                {
                    if(project.bounds().isValid())
                        bounds.extend(project.bounds());
                }
            }
            if(bounds !== undefined)
                this.map.map.fitBounds(bounds);
        },
        filter_city:function(city){
            this.reset(false);
            var ps = this.cities[city].projects;
            var bounds = undefined;
            for(var i=0; i<ps.length; i++)
            {
                ps[i].show_layer();
                if(bounds === undefined)
                {
                    if(ps[i].bounds().isValid())
                        bounds = ps[i].bounds();
                }
                else
                {
                    if(ps[i].bounds().isValid())
                        bounds.extend(ps[i].bounds());
                }
            }
            if(bounds !== undefined)
                this.map.map.fitBounds(bounds);
        },
        filter_function:function(fn){
            this.reset(false);
            var ps = this.functions[fn].projects;
            for(var i=0; i<ps.length; i++)
            {
                ps[i].show_layer();
            }
        },
        
    };
    
    var ret = Object.create(proto);
    ret.init(container, map);
    return ret;
};