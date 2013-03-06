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
            
            this.filterbox = $('<div id="filter-filter" />');
            this.filterbox_city = $('<div />');
            var all_city = $('<div id="filter-all-city">Toutes les communes</div>');
            all_city.on('click',function(){that.reset(true)});
            this.filterbox_city.append(all_city);
            this.filterbox_functions = $('<div />');
            var all_functions = $('<div id="filter-all-city">Toutes les fonctions</div>');
            all_functions.on('click',function(){that.reset(true)});
            this.filterbox_functions.append(all_functions);
            this.filterbox.append(this.filterbox_city);
            this.filterbox.append(this.filterbox_functions);
            
            this.listbox = $('<div id="filter-list" />');
            
            this.container.append(this.filterbox);
            this.container.append(this.listbox);
            
            this.cities = {};
            this.functions = {};
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                var city = project.get('city').slice(1);
                if(this.cities[city] === undefined)
                {
                    var n = $('<div class="filter-item filter-item-function">'+city+'</div>');
                    n.on('click',{city:city},function(evt){that.filter_city(evt.data.city)});
                    this.filterbox_city.append(n);
                    this.cities[city] = {
                        node:n,
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
                        var n = $('<div class="filter-item filter-item-function">'+fn+'</div>');
                        n.on('click',{fn:fn},function(evt){that.filter_function(evt.data.fn)});
                        this.filterbox_functions.append(n);
                        this.functions[fn] = {
                            node:n,
                            projects:[]
                        };
                    }
                    this.functions[fn].projects.push(project);
                }
                
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