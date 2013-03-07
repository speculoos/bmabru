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
            
            this.selector = bMa.Selector(container, 'Projects Filter');
            this.selector.add_item('All Projects',{
                click:function(evt){
                    that.reset(true);
                }},
                'filter-reset');

            this.cities = {};
            this.functions = {};
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                var city = project.get('city').slice(1);
                if(this.cities[city] === undefined)
                {
                    this.cities[city] = {
                        node:city,
                        projects:[]
                    };
                }
                this.cities[city].projects.push(project);
                
                var fn_a = project.get('functions');
                if(fn_a.length > 0)
                {
                    var fn = fn_a[0][1];
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
            this.selector.add_label('Cities');
            for(var k in this.cities)
            {
                this.selector.add_item(k, {
                    click:{
                        callback:function(evt){
                        that.filter_city(evt.data.city);
                        },
                        data:{
                            city:k
                        }
                    }
                });
            }
            
            this.selector.add_label('Functions');
            for(var k in this.functions)
            {
                this.selector.add_item(k, {
                    click:{
                        callback:function(evt){
                            that.filter_city(evt.data.fn);
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