$ = jQuery
$(document).ready =>

    $('html').click (e) ->
        tag_name = $(e.target).prop("tagName")
        $('.sub-menu-show-click').css('display', 'none')
        if tag_name is 'A'
            $(e.target).parent().children('.sub-menu-show-click').css('display', 'block')

    $('.sub-menu-form').parent().find('.nav-ref').click ->
        form_div = $(this).parent().find('.sub-menu-form')
        display = form_div.css('display')
        $('.sub-menu-form').css('display', 'none')
        if display is 'none'
            form_div.css('display', 'block')
