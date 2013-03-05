/*
 Article.js
 */

window.bMa = window.bMa || {}

window.bMa.Article = function(container)
{
    var proto = {
        init:function(container){
            this.container = container;
            this.container.hide();
            this.menu = $('<div class="menu-box"></div>');
            this.content = $('<div class="article-box"></div>');
            this.container.append(this.menu);
            this.container.append(this.content);
            
            this.articles_cache = {};
        },
        make_menu:function(cat, citem){
            var medias = window.bma_medias[cat];
            var items = medias[cat];
            this.menu.empty();
            var that = this;
            for(var ik in items)
            {
                var item = $('<div class="menu_item" id="menu_item_'+items[ik]+'">'+ik+'</div>');
                if(citem === items[ik])
                {
                    item.addClass('menu_item_current');
                }
                this.menu.append(item);
                item.on('click', {aid:items[ik]}, function(evt){
                    that.show(evt.data.aid);
                });
            }
        },
        find_cat:function(aid){
            var medias = window.bma_medias
            for(var mk in medias)
            {
                for(var ik in medias[mk])
                {
                    if(ik === aid)
                    {
                        return mk;
                    }
                }
            }
            return null;
        },
        show_complete:function(article){
            this.content.empty();
            this.content.append('<div class="article-title">'
                                +article.title
                                +'</div>');
            this.content.append('<div class="article-body">'
                                +article.body
                                +'</div>');
            this.container.show();
        },
        show:function(article_id){
            var cat = this.find_cat(article_id);
            this.make_menu(cat, article_id);
            if(this.articles_cache[article_id] === undefined)
            {
                var that = this;
                $.getJSON('/media/json/'+article_id, function(data){
                    that.show_complete(data[0].fields);
                    that.articles_cache[article_id] = data[0].fields;
                });
            }
            else
            {
                this.show_complete(this.articles_cache[article_id]);
            }
        },
        hide:function(){
            this.container.hide();
        },
    };
    
    var ret = Object.create(proto);
    ret.init(container);
    return ret;
};