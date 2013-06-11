/*
 * backbone_generic.js
 * 
 */

(function(namespace, undefined){
    window[namespace] = window[namespace] || {};
    var ns = window[namespace] ;
    ns.Modeler = function(callback, object){
        ns.Models = ns.Models || {};
        ns.Collections = ns.Collections || {};
        ns.Views = ns.Views || {};
        $.getJSON(ns.Config.API_URL, function(data){
            _.each(data, function(mdata, model)
            {
                var api_url = data[model];
                ns.Models[model] = Backbone.Model.extend({
                    urlRoot: api_url,
                    idAttribute: 'id',
                    initialize: function() { 
                        if(this.deps)
                        {
                            for(var d = 0; d < this.deps.length; d++)
                            {
                                var dep = this.deps[d];
                                if(dep.set)
                                    continue;
                                
                                this.on('change', function(cmodel, coptions){
                                    if(ns.Models[dep.model] && ns.Collections[dep.model])
                                    {
                                        if(this.get(dep.attr)
                                            && ns.Collections[dep.model].get(this.get(dep.attr)))
                                        {
                                            var depModel = ns.Collections[dep.model].get(this.get(dep.attr));
                                            depModel.on('change',function(){
                                                this.trigger('change:'+dep.attr);
                                            }, this);
                                            dep.set = true;
                                        }
                                    }
                                }, this);
                            }
                        }
                    },
                });
                
                ns.Collections[model] = Backbone.Collection.extend({
                    url: api_url,
                    model: ns.Models[model],
                });
                
                ns.Views[model] = Backbone.View.extend({
                    className: model,
                    initialize: function() {
                        this.model.on('change', this.render, this);
                    },
                    render: function() {
                        var $el = this.$el;
                        var data = this.model.toJSON();
                        Template.render(model, this, function(t){
                            $el.html(t(data));
                            if(this.postRender)
                            {
                                this.postRender(data);
                            }
                        });
                        return this;
                    },
                });
            });
            
            if(callback && (typeof callback === 'function'))
            {
                var obj = object || window;
                callback.apply(obj, []);
            }
            
        });
    }
})('NEWS');
