(function($){
    ListFilterCollapsePrototype = {
        bindToggle: function(){
            var that = this;
            this.$filterEl.click(function(){
                that.$plusMinus.html(that.hidden ? '(&minus;)' : '(&plus;)');
                that.$filterList.slideToggle();
                that.hidden = !that.hidden;
            });
        },
        init: function(filterEl) {
            this.$filterEl = $(filterEl).css('cursor', 'pointer');
            this.$filterList = this.$filterEl.next('ul').hide();
            this.hidden = true;

            var plusminus = document.createElement('span');
            plusminus.innerText = '(+)';
            plusminus.style.paddingRight = '4px';
            plusminus.style.display = 'inline-block';
            this.$filterEl.prepend(plusminus);
            this.$plusMinus = $(plusminus);

            this.bindToggle();
        }
    };
    function ListFilterCollapse(filterEl) {
        this.init(filterEl);
    }
    ListFilterCollapse.prototype = ListFilterCollapsePrototype;

    $(document).ready(function(){
        $('#changelist-filter').children('h3').each(function(){
            var collapser = new ListFilterCollapse(this);
        });
    });
})(django.jQuery);
