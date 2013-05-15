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
            '': 'newform',
            'new': 'newform',
            'edit/:id': 'edit',
        },
        newform:function(){
            app.newForm();
            app.setComponents(['form','post_images', 'images']);
        },
        edit:function(id){
            app.editForm(id);
            app.setComponents(['form','post_images','images']);
        },
    });
    
    NEWS.Router = Router;
})();


