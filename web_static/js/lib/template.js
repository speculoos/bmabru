/*
 * template.js
 * 
 */


window.template = {} || window.template;


window.template = _.extend(window.template,{
    base_url: '/web_static/js/templates/',
    cache: {},
    render: function(name, el, cb){
        if(cache[name] === undefined)
        {
            var that = this;
            $.get(that.base_url+name+'.html', function(html){
                that.cache[name] = _.template(html);
                cb.apply(el, [that.cache[name]]);
            });
        }
        else
        {
            cb.apply(el, [that.cache[name]]);
        }
    }
});