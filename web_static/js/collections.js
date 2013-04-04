/*
 * 
 * collections
 * 
 */


window.bMa = window.bMa || {}

window.bMa.PageList = Backbone.Collection.extend({
    url:'/api/pages/',
    model:bMa.Page,
});


window.bMa.ProjectList = Backbone.Collection.extend({
    url:'/api/projects/',
    model:bMa.Project,
});