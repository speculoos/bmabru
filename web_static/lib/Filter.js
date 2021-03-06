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
                    that.resetBounds();
                }},
                'filter-reset');

            this.cities = {};
            this.functions = {};
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                var city_data = project.get('city');
                if(!city_data)
                    continue;
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
            
            $('body').on('click', '.filter-city', function(evt){
                event.preventDefault();
                that.filter_city($(this).attr('data-filter'));
            });
            $('body').on('click', '.filter-function', function(evt){
                event.preventDefault();
                that.filter_function($(this).attr('data-filter'));
            });
            
        },
        resetVisibity:function(show){
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                if(show)
                    project.show_layer();
                else
                    project.hide_layer();
            }
        },
        resetBounds:function(){
            var bounds = undefined;
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
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
            this.resetVisibity(false);
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
            else
                this.resetBounds();
        },
        filter_function:function(fn){
            this.resetVisibity(false);
            this.resetBounds();
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