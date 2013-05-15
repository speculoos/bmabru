/*
 * 
 * ATW.router.js
 * 
 */


(function(undefined){
    var Router =  Backbone.Router.extend({
        navigate:function(route, options){
            options = _.extend({trigger: true}, options);
            Backbone.Router.prototype.navigate.apply(this, [route, options]);
        },
        routes:{
            'index': 'index',
            'new': 'newform',
            'edit/:id': 'edit',
            'image':'image',
        },
        index:function(){
            this.newform();
        },
        newform:function(){
            app.newForm();
            app.setComponents(['form','post_images','projects']);
        },
        edit:function(id){
            app.editForm(id);
            app.setComponents(['form','post_images','projects']);
        },
        image:function(){
            app.setComponents(['images']);
        },
    });
    
    NEWS.Router = Router;
})();


