/*
 * Config.js
 * 
 */

window.bMa = window.bMa || {};

window.bMa.Config = function(){
    
    var config = {
        feature_style_show : {
            stroke:true,
            color: '#d43b2d',
            weight:1,
            opacity:1,
            fill:true,
            fillColor: '#d43b2d',
            fillOpacity:0.5,
            clickable:true
        },
        feature_style_hide : {
            stroke:true,
            color: '#d43b2d',
            weight:1,
            opacity:1,
            fill:true,
            fillColor: '#d43b2d',
            fillOpacity:0.2,
            clickable:false
        }
    };
    
    
    var proto= {
        init:function(){
            this.config = config;
        },
        get_dict:function(path){
            var pa = path.split('/');
            if(pa[0].length === 0)
                pa.shift();
            var name = pa.join('_');
            return this.config[name];
        },
        get:function(path){
            var pa = path.split('/');
            if(pa[0].length === 0)
                pa.shift();
            var key = pa.pop();
            var name = pa.join('_');
            if(this.config[name] === undefined)
            {
                return undefined;
            }
            return this.config[name][key];
        },
        server: function(key, callback){
            $.getJSON('/config/'+key, callback);
        },
    };
    
    var ret = Object.create(proto);
    ret.init();
    return ret;
};