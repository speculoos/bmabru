/*
 * Selector.js
 */

window.bMa = window.bMa || {}

window.bMa.Selector = function(container, label){
    
    var proto = {
        init : function(container, label){
            this.root_label = label;
            this.container = container;
            this.selected = undefined;
            this.container.addClass('selector-root');
            
            this.button = $('<div />');
            this.button.addClass('selector-button');
            this.button.text(label);
            
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
            }
            else
            {
                this.items.addClass(sio);
                this.items.show(500);
            }
        },
        set_current:function(item, label){
            var sk = 'selector-item-selected';
            if(item.hasClass(sk))
            {
                return false;
            }
            this.button.text(label);
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