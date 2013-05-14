/*
 * backbone_generic.js
 * 
 */

(function(namespace, undefined){
    window[namespace] = window[namespace] || {};
    var ns = window[namespace] ;
    ns.Modeler = function(callback, object){
        ns.Models = {};
        ns.Collections = {};
        ns.Views = {};
        $.getJSON(ns.Config.API_URL, function(data){
            _.each(data, function(mdata, model)
            {
                var api_url = data[model];
                console.log(model, ns.Config.API_URL, api_url);
                ns.Models[model] = Backbone.Model.extend({
                    urlRoot: api_url,
                    idAttribute: 'id',
                    initialize: function() { },
                });
                
                ns.Collections[model] = Backbone.Collection.extend({
                    url: api_url,
                    model: ns.Models[model],
                });
                
                ns.Views[model] = Backbone.View.extend({
                    className: model,
                    initialize: function() {
                        this.model.on('change', this.render, this);
                        if(!this.model.isNew())
                        {
                            this.render();
                        }
                    },
                    render: function() {
                        var $el = this.$el;
                        $el.attr('id', model + '_' + this.model.id)
                        $el.empty();
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