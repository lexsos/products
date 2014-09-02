$ = jQuery
$(document).ready =>

    ajax_tree_url = '/ajax/tree/'
    ajax_edit_tree_url = '/ajax/edit_tree/'

    getTree = (url) ->
        req =
            type: "GET"
            url: url
            async: false
        json_data = $.ajax(req).responseText
        data_obj = $.parseJSON(json_data)
        data_obj

    $('#tree').treeview
        data: getTree(ajax_tree_url)
    $('#tree').on 'nodeSelected', (event, node) ->
        $('#compare_div').load(node.url)


    $('#edit_tree').treeview
        data: getTree(ajax_edit_tree_url)
    $('#edit_tree').on 'nodeSelected', (event, node) ->
        $('#edit_div').load node.url, ->
            $('.price_edit').change ->
                $(this).attr('edited', 'True')


    $('#save_btn').click ->
        $('.price_edit').each (index) ->
            edit_ctl = $(this)
            if edit_ctl.attr('edited') == 'True'
                edit_ctl.attr('edited', 'False')
        alert('All saved')
