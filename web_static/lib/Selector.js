/*
 * Selector.js
 */

window.bMa = window.bMa || {}

window.bMa.Selector = function(container, label){
    
    var proto = {
        ICON_UP: '▵',
        ICON_DOWN: '▿',
        init : function(container, label){
            this.root_label = label;
            this.container = container;
            this.selected = undefined;
            this.container.addClass('selector-root');
            
            this.button = $('<div />').addClass('selector-button');
            
            this.button_text = $('<span />').addClass('selector-button-text');
            this.button_text.text(label);
            
            this.button_icon = $('<span />').addClass('selector-button-text');
            this.button_icon.text(this.ICON_UP);
            this.button_icon.css({float:'right'});
            
            this.button.append(this.button_text);
            this.button.append(this.button_icon);
            
            this.items = $('<div />');
            this.items.addClass('selector-items');
            this.items.hide();
            
            this.container.append(this.items);
            this.container.append(this.button);
            
            var that = this;
            this.button.on('click', function(evt){
                that.toggle_items();
            });
        },
        add_label:function(label){
            var item  = $('<div />');
            item.addClass('selector-item-label');
            item.text(label);
            this.items.append(item);
        },
        add_item : function(label, callbacks, klass){
            var item  = $('<div />');
            item.addClass('selector-item');
            item.text(label);
            if(klass !== undefined)
                item.addClass(klass);
            var that = this;
            item.on('click', function(evt){
                that.toggle_items();
                if(!that.set_current(item, label)) // noop, item already current one
                    return;
                if(callbacks !== undefined)
                {
                    for(var k in callbacks)
                    {
                        if((typeof callbacks[k]) !== 'function')
                        {
                            evt.data = $.extend({}, callbacks[k].data);
                            callbacks[k].callback.call(item, evt);
                        }
                        else
                        {
                            callbacks[k].call(item, evt);
                        }
                    }
                }
                
            });
//             if(callbacks !== undefined)
//             {
//                 for(var k in callbacks)
//                 {
//                     if((typeof callbacks[k]) === 'function')
//                     {
//                         item.on(k, callbacks[k]);
//                     }
//                     else // we assume {callback: fn, data: {}}
//                     {
//                         item.on(k, callbacks[k].data, callbacks[k].callback);
//                     }
//                 }
//             }
            this.items.append(item);
            return item;
        },
        toggle_items:function(){
            var sio = 'selector-items-open';
            if(this.items.hasClass(sio))
            {
                this.items.removeClass(sio);
                this.items.hide(500);
                this.button_icon.text(this.ICON_UP);
            }
            else
            {
                this.items.addClass(sio);
                this.items.show(500);
                this.button_icon.text(this.ICON_DOWN);
            }
        },
        set_current:function(item, label){
            var sk = 'selector-item-selected';
            if(item.hasClass(sk))
            {
                return false;
            }
            this.button_text.text(label);
            if(this.selected !== undefined)
            {
                this.selected.removeClass(sk);
            }
            this.selected = item;
            this.selected.addClass(sk);
            return true;
        },
        get:function(){
            return this.selected;
        }
    };
    
    var ret = Object.create(proto);
    ret.init(container, label);
    return ret;
};