/*
 Article.js
 */

window.bMa = window.bMa || {}

window.bMa.Article = function(container)
{
    var proto = {
        init:function(container){
            this.container = container;
            this.container.parent().hide();
            this.catname = $('<div class="catname-box"></div>');
            this.menu = $('<div class="menu-box"></div>');
            this.content = $('<div class="article-box"></div>');
            this.container.append(this.catname);
            this.container.append(this.menu);
            this.container.append(this.content);
            
            this.articles_cache = {};
            
            this.media_url = undefined;
            var that = this;
            bMa.Config().server('MEDIA_URL', function(data){
                that.media_url = data.MEDIA_URL;
            });
        },
        make_menu:function(cat, citem){
            var medias = window.bma_medias[cat];
            var items = medias;
            this.menu.empty();
            this.catname.empty();
            this.catname.append('<div class="menu-title">'+cat+'</div>');
            var that = this;
            for(var ik in items)
            {
                var item = $('<div class="menu_item" id="menu_item_'+items[ik]+'"></div>');
                item.append('<span><span>'+items[ik]+'</span></span>');
                if(citem === ik)
                {
                    item.addClass('menu_item_current');
                }
                this.menu.append(item);
                item.on('click', {aid:ik}, function(evt){
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
            this.content.append('<div class="article-title"><a href="/media/page/'+article.slug+'">'
                                +article.title
                                +'</a></div>');
            this.content.append('<div class="article-body">'
                                +article.body
                                +'</div>');
            var image = $('<div class="article-image" />');
            if(article.image && this.media_url !== undefined)
            {
                image.append('<image src="'+this.media_url+article.image+'" width="'+article.width+'" height="'+article.height+'" />');
            }
            this.content.append(image);
            this.container.parent().show();
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
            this.container.parent().hide();
        },
    };
    
    var ret = Object.create(proto);
    ret.init(container);
    return ret;
};