$ = jQuery
$(document).ready =>


    Dajaxice.products.get_tree (data) ->
        $('#tree').treeview
            data: data
        $('#edit_tree').treeview
            data: data


    $('#tree').on 'nodeSelected', (event, node) ->
        params =
            category_pk: node.category_pk
        callback = (data) ->
            $('#compare_div').html(data.body)
        Dajaxice.products.get_compare_table(callback, params)


    $('#edit_tree').on 'nodeSelected', (event, node) ->
        params =
            category_pk: node.category_pk
        callback = (data) ->
            $('#edit_div').html(data.body)
            $('.price_edit').change ->
                $(this).attr('edited', 'True')
        Dajaxice.products.get_edit_table(callback, params)


    $('#save_btn').click ->
        $('.price_edit').each (index) ->
            edit_ctl = $(this)
            if edit_ctl.attr('edited') == 'True'
                edit_ctl.attr('edited', 'False')
                params =
                    price: edit_ctl.val()
                    product_pk: edit_ctl.attr('product_pk')
                    shop_pk: edit_ctl.attr('shop_pk')
                callback = (data) ->
                    data
                Dajaxice.products.set_price(callback, params)

        alert('All saved')


    make_tree_node = (level, node_data) ->
        li_html = '<li>'
        for i in [0..level]
            do (i) ->
                li_html += '<span class="ident"></span>'
        if node_data.nodes
            if level > 0
                li_html += '<span class="collapsed"></span>'
            else
                li_html += '<span class="expanded"></span>'
        li_html += '<span class="node-text">'
        li_html += node_data.text
        li_html += '</span>'
        li_html += '</li>'
        li_element = $(li_html)
        node_data.element = li_element
        if level > 0
            node_data.collapsed = true
        if level > 1
            li_element.addClass('hiden')
        li_element.data('node_data', node_data)
        li_element


    add_tree_nodes = (level, nodes_list, tree_list) ->
        nodes_list.forEach (node_data, i) ->
            make_tree_node(level, node_data).appendTo(tree_list)
            if node_data.nodes
                add_tree_nodes(level+1, node_data.nodes, tree_list)


    collapse_tree = (node_data) ->
        node_data.nodes.forEach (item_data, i) ->
            item_data.element.addClass('hiden')
            item_data.element.find('.expanded, .collapsed').addClass('collapsed').removeClass('expanded')
            item_data.collapsed = true
            if item_data.nodes
                collapse_tree(item_data)


    build_tree = (element, nodes_list, on_select) ->
        element.html('<ul class="tree-view"></ul>')
        tree_list = element.find('ul')
        tree_list.data('nodes', nodes_list) 
        add_tree_nodes(0, nodes_list, tree_list)
        
        tree_list.find('li').click ->
            node_data = $(this).data('node_data')
            if not node_data.selected
                tree_list.find('li').each (i) ->
                    item_data = $(this).data('node_data')
                    item_data.selected = false
                    $(this).data('node_data', item_data)

                tree_list.find('li').removeClass('selected')
                $(this).addClass('selected')
                node_data.selected = true
                on_select(node_data)

        tree_list.find('.expanded, .collapsed').click (e) ->
            e.stopPropagation()
            node_data = $(this).parent().data('node_data')
            if node_data.collapsed
                node_data.element.find('.expanded, .collapsed').addClass('expanded').removeClass('collapsed')
                node_data.nodes.forEach (item_data, i) ->
                    item_data.element.removeClass('hiden')
            else
                collapse_tree(node_data)
                node_data.element.find('.expanded, .collapsed').addClass('collapsed').removeClass('expanded')

            node_data.collapsed = !node_data.collapsed

    Dajaxice.products.get_tree (data) ->
        build_tree $('.left-container'), data, (item) ->
            $('.midle-container').html item.text + ' ' + item.category_pk
