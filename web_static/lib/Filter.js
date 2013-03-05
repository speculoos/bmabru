/*
 * Filter.js
 */


window.bMa = window.bMa || {}

window.bMa.Filter = function(container){
    
    var proto = {
        init:function(container){
            this.container = container;
            this.filters = {};
            
            this.filterbox = $('<div id="filter-filter" />');
            this.listbox = $('<div id="filter-list" />');
            
            this.container.append(this.filterbox);
            this.container.append(this.listbox);
            
            var that = this;
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
                    this.filterbox.append(n);
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
                        this.filterbox.append(n);
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
            for(var p in bMa.Projects)
            {
                var project = bMa.Projects[p];
                if(show)
                    project.show_layer();
                else
                    project.hide_layer();
            }
        },
        filter_city:function(city){
            this.reset(false);
            var ps = this.cities[city].projects;
            for(var i=0; i<ps.length; i++)
            {
                ps[i].show_layer();
            }
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
    ret.init(container);
    return ret;
};