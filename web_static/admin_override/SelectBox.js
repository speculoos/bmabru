/**
 * Drop-in replacement of django-admin's SelectBox.js, handles optgroup elements correclty.
 *
 * @author Sardar Yumatov (ja doma gmail com)
 */

var SelectBox = {
    cache: new Object(),
    init: function(id) {
        var cache = [];
        var nogroup = [];
        django.jQuery("#" + id + " > option").each(function() {
            nogroup.push({value: this.value, text: this.text, displayed: 1});
        });
        cache.push({'group': null, 'items': nogroup});

        django.jQuery("#" + id + " optgroup").each(function() {
            var group = [];
            django.jQuery("option", this).each(function() {
                group.push({value: this.value, text: this.text, displayed: 1});
            })
            cache.push({'group': django.jQuery(this).attr('label'), 'items': group});
        });
        SelectBox.cache[id] = cache;
        SelectBox.sort(id, false);
    },
    redisplay: function(id) {
        // Repopulate HTML select box from cache
        var ctr = django.jQuery("#" + id).empty(), ct;
        var cache = SelectBox.cache[id];
        for(var i = 0; i < cache.length; i ++) {
            var gr = cache[i];
            if(gr.items.length == 0) continue; //skip empty groups
            if(gr.group == null) ct = ctr;
            else ct = django.jQuery("<optgroup>").attr('label', gr.group).appendTo(ctr);
            for(var j = 0; j < gr.items.length; j++) {
                var itm = gr.items[j];
                if(itm.displayed) django.jQuery("<option>").attr('value', itm.value).text(itm.text).appendTo(ct);
            }
        }
    },
    filter: function(id, text) {
        // Redisplay the HTML select box, displaying only the choices containing ALL
        // the words in text. (It's an AND search.)
        var tokens = text.toLowerCase().split(/\s+/);
        var cache = SelectBox.cache[id];
        for(var i = 0; i < cache.length; i ++) {
            var gr = cache[i].items;
            for(var k = 0; k < gr.length; k++) {
                gr[k].displayed = 1;
                for(var j = 0; j < tokens.length; j++) {
                    if(gr[k].text.toLowerCase().indexOf(tokens[j]) < 0) {
                        gr[k].displayed = 0;
                        break;
                    }
                }
            }
        }
        SelectBox.redisplay(id);
    },
    delete_from_cache: function(id, value) {
        var cache = SelectBox.cache[id];
        outer:
        for(var i = 0; i < cache.length; i ++) {
            var gr = cache[i].items;
            for(var j = 0; j < gr.length; j++) {
                if(gr[j].value == value) {
                    gr.splice(j, 1);
                    break outer;
                }
            }
        }
    },
    add_to_cache: function(id, option, group) {
        var cache = SelectBox.cache[id];
        if(!group) group = null;
        for(var i = 0; i < cache.length; i++) {
            if(cache[i].group == group) {
                cache[i].items.push({value: option.value, text: option.text, displayed: 1});
                SelectBox.sort(id, group);
                return;
            }
        }
        //new group
        cache.push({'group': group, 'items': [{value: option.value, text: option.text, displayed: 1}]});
    },
    cache_contains: function(id, value) {
        // Check if an item is contained in the cache
        grps = SelectBox.cache[id];
        if(grps) {
            for(var i = 0; i < grps.length; i++) {
                var itms = grps[i].items;
                for(var j = 0; j < itms.length; j++) {
                    if(itms[i].value == value) {
                        return true;
                    }
                }
            }
        }
        return false;
    },
    move: function(from, to) {
        django.jQuery("#" + from + " option:selected").each(function() {
            var group = this.parentNode.tagName.toLowerCase() == 'optgroup'? this.parentNode.getAttribute('label'): null;
            SelectBox.add_to_cache(to, {value: this.value, text: this.text, displayed: 1}, group);
            SelectBox.delete_from_cache(from, this.value);
        });
        SelectBox.redisplay(from);
        SelectBox.redisplay(to);
    },
    move_all: function(from, to) {
        django.jQuery("#" + from + " option").each(function() {
            var group = this.parentNode.tagName.toLowerCase() == 'optgroup'? this.parentNode.getAttribute('label'): null;
            SelectBox.add_to_cache(to, {value: this.value, text: this.text, displayed: 1}, group);
            SelectBox.delete_from_cache(from, this.value);
        });
        SelectBox.redisplay(from);
        SelectBox.redisplay(to);
    },
    sort: function(id, group) {
        var cache = SelectBox.cache[id];
        if(!group && group !== false) group = null;
        for(var i = 0; i < cache.length; i++) {
            if(group === false || cache[i].group == group) {
                cache[i].items.sort(function(a, b) {
                    a = a.text.toLowerCase();
                    b = b.text.toLowerCase();
                    try {
                        if (a > b) return 1;
                        if (a < b) return -1;
                    } catch (e) {
                        // silently fail on IE 'unknown' exception
                    }
                    return 0;
                });
            }
        }
    },
    select_all: function(id) {
        django.jQuery("#" + id + " option").attr('selected', 'selected');
    }
}
