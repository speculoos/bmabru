/*
 Project.js
 
 */


window.bMa = window.bMa || {};
window.bMa.Projects = window.bMa.Projects || {};

window.bMa.Project = function(args){
    var config = bMa.Config();
    var proto = {
        init:function(args){
            this.data = args;
            this.id = args.id;
            window.bMa.Projects[this.id] = this;
        },
        get:function(key, idx){
            if(this.data[key] !== undefined)
            {
                if(idx === undefined)
                    return this.data[key]
                else
                    return this.data[key][idx]
            }
            else
            { 
                return 'Data not available';
                throw new this.NoKeyException(key);
            }
        },
        NoKeyException:function(key) {
            this.message = 'Project ['+this.id+'] has no key: '+key;
            this.name = "NoKeyException";
        },
        hide_layer:function(){
            if(this.layer !== undefined)
            {
                var options = config.get_dict('/feature/style/hide');
                this.layer.setStyle(function(f){ return options;});
            }
        },
        show_layer:function(){
            if(this.layer !== undefined)
            {
                var options = config.get_dict('/feature/style/show');
                this.layer.setStyle(function(f){ return options;});
            }
        },
        bounds:function(){
            if(this.layer === undefined || this.data.geojson.coordinates.length === 0)
            {
                var llb = new L.LatLngBounds();
                return llb;
            }
            return this.layer.getBounds();
        }
    };
    
    var ret = Object.create(proto);
    ret.init(args);
    return ret;
};