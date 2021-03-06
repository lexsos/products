$ = jQuery
$(document).ready =>

    Array::toDict = (key) ->
        @reduce ((dict, obj) -> dict[ obj[key] ] = obj if obj[key]?; return dict), {}


    class CategoryView
        constructor: (@container) ->

        ajax_function: (callback, params) ->

        after_load: (self) ->

        load_category: (category) ->
            self = @
            params =
               category_pk: category.category_pk
            callback = (data) ->
                self.container.html(data.body)
                self.after_load(self)

            @ajax_function(callback, params)


    class CompareTableView extends CategoryView

        ajax_function: (callback, params) ->
            Dajaxice.products.get_compare_table(callback, params)

        after_load: (self) ->
            $('.compare-table .show-address').click ->
                $('.compare-table .shop-address').toggleClass('hiden')


    class EditTableView extends CategoryView

        ajax_function: (callback, params) ->
            Dajaxice.products.get_edit_table(callback, params)

        after_load: (self) ->
            $('#edit-tables-seve-btn').click ->
                self.on_save(self, $(this))
            $('.edit-table .price').change ->
                self.on_change(self, $(this))

        on_change: (self, element) ->
            element.attr('edited', 'True')

        on_save: (self, element) ->
            cost_list = []
            $('.edit-table .price').each (index) ->
                edit_ctl = $(this)
                if edit_ctl.attr('edited') == 'True'
                    price =
                        price: edit_ctl.val()
                        product_pk: edit_ctl.attr('product_pk')
                        shop_pk: edit_ctl.attr('shop_pk')
                    cost_list.push(price)
                edit_ctl.attr('edited', 'False')
            params =
                cost_list: cost_list
            callback = (data) ->
                alert data.message
            Dajaxice.products.save_price_list(callback, params)


    class LessCompareView extends CategoryView

        ajax_function: (callback, params) ->
            Dajaxice.products.get_less_compare(callback, params)

        after_load: (self) ->
            $('.show-product-detail').click ->
                self.detail_click(self, $(this))

        detail_click: (self, a_element) ->
            tr_id = a_element.attr('tr')
            tr = $(tr_id)
            tr.toggleClass('hiden')
            if not tr.hasClass('hiden')
                td = tr.find('td')
                params =
                    product_pk: a_element.attr('productpk')
                callback = (data) ->
                    td.html(data.body)
                Dajaxice.products.get_less_detail(callback, params)

            detail_count = 0
            $('.less-cmp-table .detail').each (index) ->
                if not $(this).hasClass('hiden')
                    detail_count += 1
            if detail_count
                $('.less-cmp-table .coll-min').addClass('hiden')
                $('.less-cmp-table .coll-max').addClass('hiden')
            else
                $('.less-cmp-table .coll-min').removeClass('hiden')
                $('.less-cmp-table .coll-max').removeClass('hiden')

    view_list = [
        {
            key: 'cmp-table'
            cls: CompareTableView
        },
        {
            key: 'edit-table'
            cls: EditTableView
        },
        {
            key: 'cmp-less'
            cls: LessCompareView
        },
    ]


    class ModeView
        constructor: (@container) ->
            @mode = "cmp-table"
            view_arr = view_list.slice(0)
            for view in view_arr
                view.instans = new view.cls(@container)
            @view_list = view_arr.toDict('key')

        select_mode: (mode) ->
            if mode isnt @mode
                @mode = mode
                @apply()

        select_category: (category) ->
            if category isnt @category
                @category = category
                @apply()

        apply: ->
            if not @mode or not @category
                return
            @view_list[@mode].instans.load_category(@category)


    mode_view = new ModeView($('.midle-container'))


    Dajaxice.products.get_tree (data) ->
        build_tree_view $('.tree-filter'), data, (item) ->
            mode_view.select_category(item)


    $('#view-mode-select').change ->
        mode_view.select_mode($(this).val())


    $(window).resize ->
        $('body').css('padding-top', $('.nav-bar').height())
