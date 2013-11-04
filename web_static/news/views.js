/*
* 
* NEWS.views.js
* 
*/

(function(undefined){
    'strict';
    var NEWS = window.NEWS;
    var Views = {};
    var Backbone = window.Backbone;
    
    var ConfirmDialog = Backbone.View.extend({
        className:'modal',
        initialize:function(){
            this.$title = $('<div />').addClass('modal-header');
            this.$body = $('<div />').addClass('modal-body');
            this.$controls = $('<div />').addClass('modal-footer');
            
            this.$cancel = $('<button />')
                            .addClass('btn cancel')
                            .text('Cancel')
                            .appendTo(this.$controls);
                            
            this.$confirm = $('<button />')
                            .addClass('btn btn-primary confirm')
                            .text('Confirm')
                            .appendTo(this.$controls);
            
            this.$title.html(this.options.title || 'Confirm');
            this.$body.html(this.options.body || '<p></p>');
        },
        render:function(){
            this.$el.append(this.$title);
            this.$el.append(this.$body);
            this.$el.append(this.$controls);
            this.$el.modal({
                backdrop:false,
                show:true,
            });
            this.$el.on('hidden', this.cancel.bind(this));
            return this;
        },
        events:{
            'click .cancel':'cancel',
            'click .confirm':'confirm',
        },
        cancel:function(){
            this.trigger('cancel');
            this.$el.remove();
        },
        confirm:function(){
            this.trigger('confirm');
            this.$el.remove();
        },
    });
    
    Views.ItemsView = Backbone.View.extend({
        tagName:'ul',
        className:'nav nav-list',
        initialize:function(){
            this.newsItems = new NEWS.Collections.items;
            this.newsItems.on('add', this.renderOne, this);
            this.newsItems.on('reset', this.render, this);
            this.newsItems.on('sort', this.render, this);
            this.newsItems.on('destroy', this.render, this);
            this.items = {};
            
            this._ready = false;
            this.newsItems.on('reset', function(){
                this.render();
            }, this);
            
            this.newsItems.fetch({reset:true});
        },
        renderOne: function(item){
//             console.log('ItemsView.renderOne',item.id, this._ready);
            if(!this._ready)
            {
                var self = this;
                window.setTimeout(function(){
                    self.renderOne(item);
                }, 300);
            }
            if(this.items[item.cid] === undefined)
            {
                item.set({
                    visited:false,
                    current:false,
                }, {silent:true});
                var i = new NEWS.Views.items({model:item});
                this.$el.append(i.render().$el);
                this.items[item.cid] = i;
                var self = this;
                item.on('change:pub_date', function(){
                    self.newsItems.sort();
                });
            }
            return this;
        },
        render: function(){
            Template.render('item-list', this, function(t){
                this.items = {};
                this.$el.html(t({}));
                this._ready = true;
                this.newsItems.each(function(item){
                    this.renderOne(item);
                }, this);
            });
            
            return this;
        },
    });
    
    
    Views.ProjectsView = Backbone.View.extend({
        className:'projects well span4',
        initialize:function(){
            this.projects = new NEWS.Collections.projects;
            //             this.projects.on('add', function(){
            //                 this.render();
            //             }, this);
            this.projects.on('reset', function(){
                this.projects_ready = true;
                this.render();
            }, this);
            //             this.items = {};
            this.projects_ready = false;
            this.projects.fetch({reset:true});
        },
        renderOne: function(item, options){
            options = _.extend({open:false}, options);
            var i = new NEWS.Views.projects({model:item});
            console.log(item.toJSON());
            var el = i.render().el;
            if(options.open)
            {
                i.$el.find('.accordion-body').addClass('in');
            }
            var $root = this.$el.find('.accordion');
            if($root.length > 0)
            {
                $root.append(el);
            }
            return this;
        },
        render: function(){
            this.$el.empty();
            Template.render('projects-list', this, function(t){
                this.$el.html(t({
                    ready:this.projects_ready,
                }));
                if(this.projects_ready)
                {
                    var complete_source = [];
                    for(var i; i < this.projects.length; i++){
                        complete_source.push(this.projects.at(i).get('name'));
                    };
                    this.$el.find('.search-q').typeahead({
                        source:complete_source,
                    });
                }
            }, this);
            return this;
        },
        events:{
            'click .search-submit':'search',
            'click .select': 'select',
        },
        search:function(evt){
            evt.preventDefault();
            this.$el.find('.accordion').empty();
            var re = new RegExp(this.$el.find('.search-q').val(), "i");
            var self = this;
            var items = [];
            this.projects.each(function(item, idx){
                var name = item.get('name');
                if(re.test(name))
                {
                    var res = re.exec(name);
                    items.push({item:item,m:res.length});
                }
            });
            items.sort(function(a, b) {
                return a.m - b.m;
            });
            for(var i=0; i < items.length; i++){
                this.renderOne(items[i].item, {open:(i === 0)});
            }
        },
        select:function(evt){
            var el = $(evt.target);
            var id = el.attr('data-pid');
            window.app.components.form.view.setProject(id);
        },
    });
    
    Views.TitleView = Backbone.View.extend({
        id:'titlebar',
        tagName:'ul',
        className:'breadcrumb',
        initialize:function(){
            this.elements = [{title:'News', route:'index'}];
        },
        setElements:function(elts){
            this.elements = elts;
            this.render();
        },
        render:function(){
            this.$el.empty();
            var dvdr = ' <span class="divider">::';
            for(var i = 0; i < this.elements.length; i++)
            {
                var elt = this.elements[i];
                if(i === (this.elements.length - 1))
                    dvdr = '';
                this.$el.append('<li><span class="link" data-route="'+elt.route+'">'+elt.title+dvdr+'</li>');
            }
            return this;
        },
    });
    
    Views.PostImagesView = Backbone.View.extend({
        className:'images well span4',
        initialize:function(){
            this.images = [];
        },
        render:function(){
            this.$el.empty();
            if(this.images.length > 0)
                this.$el.show();
            else
                this.$el.hide();
            Template.render('images', this, function(t){
                this.$el.html(t({images:this.images}));
            }, this);
            return this;
        },
        setImages:function(images){
            this.images = images;
            this.render();
        },
        events:{
            'click .image-selector':'select',
        },
        select: function(evt){
            var btn = $(evt.target);
            window.app.components.form.view.model.set({image_url:btn.attr('data-image')});
        },
    });
    
    Views.NewsImagesView = Backbone.View.extend({
        className:'news-images-box',
        initialize:function(){
            this.images = new NEWS.Collections.resources;
            this.images.on('add', this.renderOne, this);
            this.images.on('reset', this.render, this);
            this.items = {};
            this.images.fetch();
        },
        renderOne: function(item){
            if(this.items[item.cid] === undefined)
            {
                item.set({
                    visited:false,
                    current:false,
                });
                var i = new NEWS.Views.resources({model:item});
                var el = i.render().el;
                var $root = this.$el.find('.thumbnails');
                if($root.length > 0)
                {
                    $root.append(el);
                    this.items[item.cid] = i;
                }
            }
            return this;
        },
        render: function(){
            this.$el.empty();
            Template.render('resources-list', this, function(t){
                this.$el.html(t({}));
                this.images.each(function(item){
                    this.renderOne(item);
                }, this);
            });
            
            return this;
        },
        events:{
            'click .image-selector':'select',
        },
        select: function(evt){
            var btn = $(evt.target);
            window.app.components.form.view.model.set({image_url:btn.attr('data-image')});
            window.app.restoreComponents();
            },
            activate:function(app){
                app.saveComponents();
            },
        });
    
    Views.PostView = Backbone.View.extend({
        className:'news-form',
        initialize:function(){
            this.resetModel(this.model);
            this._initial = true;
            this.resetChangeState();
        },
        render: function() {
            var $el = this.$el;
            $el.empty();
            var data = this.model.toJSON();
            Template.render(this.className, this, function(t){
                $el.html(t(data));
                $el.find('.datepicker').datepicker({
                    autoclose:true,
                });
            });
            return this;
        },
        fillProjectData:function(){
            var id = this.model.get('project');
            var projects = window.app.components.projects.view.projects;
            var project = projects.get(id);
            if(project)
            {
                this.model.set({
                    project_data: project.toJSON(),
                });
            }
        },
        resetModel:function(model) {
            this.model.set({selected:false});
            this.model = model;
            this.model.set({selected:true});
            this._initial = false;
            if(this.model.get('project') 
                && !this.model.get('project_data'))
            {
                this.fillProjectData();
            }
            this.render();
            this.model.on('change:project', function(){
                this.fillProjectData;
            }, this)
            this.model.on('change', this.render, this);
            this.resetChangeState();
        },
        setProject:function(id){
            this.model.set({ project:id, });
            this.setChangeState();
        },
        events:{
            'click .submit':'save',
            'click .delete':'delete_news',
            'click .parser':'parser',
            'click .reset-project':'resetProject',
            'keyup input, textarea': 'setChangeState',
            'click .image-delete':'removeImage',
        },
        setChangeState:function(evt){
            var body_fr = this.$el.find('[name=body_fr]').val();
            var title_nl = this.$el.find('[name=title_nl]').val();
            var title_fr = this.$el.find('[name=title_fr]').val();
            var body_nl = this.$el.find('[name=body_nl]').val();
            
            this.model.set({
                body_fr:body_fr,
                body_nl:body_nl,
                title_fr:title_fr,
                title_nl:title_nl,
            },{silent:true});
            this._changed = true;
            return true;
        },
        resetChangeState:function(){
            
            this._changed = false;
        },
        resetProject:function(){
            this.model.set({project:null});
            this.setChangeState();
        },
        serialize:function(){
            var ret = {};
            ret.title_fr = this.$el.find('[name=title_fr]').val();
            ret.body_fr = this.$el.find('[name=body_fr]').val();
            ret.title_nl = this.$el.find('[name=title_nl]').val();
            ret.body_nl = this.$el.find('[name=body_nl]').val();
            if(ret.title_fr === '')
                ret.title_fr = 'translation not available';
            if(ret.body_fr === '')
                ret.body_fr = 'translation not available';
            if(ret.title_nl === '')
                ret.title_nl = 'translation not available';
            if(ret.body_nl === '')
                ret.body_nl = 'translation not available';
            ret.title = '@fr @nl';
            ret.body = '@fr @nl';
            
            ret.pub_date = this.$el.find('[name=pub_date]').val();
            
            ret.resource = '';
            ret.project = parseInt(this.$el.find('[name=project]').val());
            return ret;
        },
        save:function(){
            var model = this.model;
            var submit = this.$el.find('.submit');
            var data = this.serialize();
            
            submit.button('loading');
            model.once('sync',function(){
                submit.button('reset');
                window.app.items.newsItems.add(model);
            });
            model.save(data);
            this.resetChangeState();
        },
        delete_news:function(evt){
            var confirm = new ConfirmDialog({
                title:'<h2>Confirm deletion</h2>',
                body:'<p>Are you certain you want to delete <em>'+this.model.get('title')+'</em></p>',
            });
            var self =this;
            confirm.on('confirm', function(){
                window.app.removePost(self.model);
            });
            confirm.render();
        },
        removeImage:function(){
            this.model.set({image_url:''});
            this.setChangeState();
        },
        parser:function(){
            var urlElt = this.$el.find('[name=parse_url]');
            var btn = this.$el.find('.parser');
            btn.button('loading');
            var url = urlElt.val();
            urlElt.val('');
            var self = this;
            $.ajax({
                url:NEWS.Config.PARSER_URL,
                type: "POST",
                data:{url:url},
                dataType:'json'
            }).done(function(data){
                var body = [url];
                if(data.meta.description)
                {
                    body.push(data.meta.description);
                }
                else
                {
                    if(data.content.length > 0)
                        body.push(data.content[0]);
                }
                self.model.set({
                    title_fr:data.meta.title,
                    body_fr:body.join('\n\n'),
                    title_nl:data.meta.title,
                    body_nl:body.join('\n\n'),
                });
                
                window.app.components.post_images.view.setImages(data.images);
                
                btn.button('reset');
            });
        },
        confirmLeave:function(next){
            if(this._initial || !this._changed)
            {   
                next();
                return;
            }
            console.log('confirm', this._initial, this._changed);
            var modal = this.$el.find('#ChangeFormModal');
            var dismiss = modal.find('.news-dismiss');
            var cancel = modal.find('.news-cancel');
            var save = modal.find('.news-save');
            var self = this;
            dismiss.one('click', function(){
                next();
            });
            cancel.one('click', function(){
                modal.modal('hide');
            });
            save.one('click', function(){
                var data = self.serialize();
                self.model.save(data);
                self.resetChangeState();
                next();
            });
            modal.modal({
                backdrop:false,
                keyboard:false,
                show:true,
            });
        },
    });
    
    
    Views.NewImageView = Backbone.View.extend({
        className:'modal new-image-box',
        initialize:function(){
            
        },
        render:function(){
            var $el = this.$el;
            $el.empty();
            Template.render('new-image', this, function(t){
                $el.html(t({}));
            });
            return this;
        },
        events:{
            'click .submit':'submit',
            'click .close-dialog':'close',
        },
        close:function(){
            window.app.unsetComponent('new_image');
            window.app.render();
        },
        submit:function(evt){
            var form = this.$el.find('.upload');
            var media = form.find('input');
            var formdata = new FormData();
            var f = media[0].files[0];
            var f_name = f.name;
            
            formdata.append('image', f);
            var that = this;
            $.ajax({  
                url: NEWS.Collections.resources.prototype.url,  
                type: "POST",  
                data: formdata,  
                processData: false,  
                contentType: false,  
                success: function(res) { 
                    window.app.getComponent('images').images.add(res);
                    window.app.getComponent('form').model.set({
                        image_url:res.url,
                    });
                }  
            });
            this.close();
        },
        
    });
    
    NEWS.Views = NEWS.Views || {};
    _.extend(NEWS.Views, Views);
    
})();