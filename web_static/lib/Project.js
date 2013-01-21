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
                console.log('ERROR ['+this.id+']:Attempt to access inexistant key => '+key);
        },
    };
    
    var ret = Object.create(proto);
    ret.init(args);
    return ret;
};