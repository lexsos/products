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


    Dajaxice.products.get_tree (data) ->
        build_tree_view $('.left-container'), data, (item) ->
            params =
                category_pk: item.category_pk
            callback = (data) ->
                $('.midle-container').html(data.body)
            Dajaxice.products.get_compare_table(callback, params)
