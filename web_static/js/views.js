/*
 * 
 * views
 * 
 */

window.bMa = window.bMa || {}

window.bMa.PageView = Backbone.View.extend({
    initialize: function() {
        Backbone.View.apply(this, arguments);
        this.listenTo(this.model, 'change', this.render);
    },
    render: function() {
        var data = this.model.toJSON();
        template.render('page', this.$el, function(t){
            this.html(t(data));
        });
        return this;
    },
});



window.bMa.ProjectView = Backbone.View.extend({
    initialize: function() {
        Backbone.View.apply(this, arguments);
        this.listenTo(this.model, 'change', this.render);
    },
    render: function() {
        var m = this.model;
        var dsp = m.get('display');
        if(dsp)
        {
            var options = config.get_dict('/feature/style/show');
        }
        else
        {
            
        }
        this.model.get('feature').setStyle(function(f){ return options;});
        return this;
    },
});

