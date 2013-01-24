/*
 Project.js
 
 */


window.bMa = window.bMa || {}

window.bMa.Project = function(args){
    var proto = {
        init:function(args){
            this.data = args.fields;
            this.id = args.pk;
        },
        get:function(key){
            if(this.data[key] !== undefined)
                return this.data[key]
            else
            { 
                throw new this.NoKeyException(key);
            }
        },
        NoKeyException:function(key) {
            this.message = 'Project ['+this.id+'] has no key: '+key;
            this.name = "NoKeyException";
        },
    };
    
    var ret = Object.create(proto);
    ret.init(args);
    return ret;
};