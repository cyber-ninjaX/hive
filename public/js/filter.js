(function($) {
    var RETURN = 13;

    $(function() {
        var $tbody = $('#result_list').children('tbody');

        function fix_striping() {
            $tbody.children('.row1:visible, .row2:visible').removeClass('row1 row2').each(function(idx) {
                this.setAttribute('class', 'row' + (idx % 2 + 1));
            });
        }

        // Clear button
        var $clear = $('#clear-searchbar');
        var $search = $('#searchbar');
        $clear.click(function(evt) {
            evt.stopPropagation();
            $search.val('').change().focus();
            return false;
        });
        // Done here (instead of a static style="display:none;"), as the
        // search box can be populated on load
        $clear.toggle(!!$search.val());

        $search.keydown(function(evt) {
            if (evt.keyCode == RETURN) {
                evt.preventDefault();
                return false;
            }
        });

        var row_cache = [];
        var $rows = $tbody.children('tr');
        $rows.each(function() {
            var $this = $(this);
            var $tds = $this.children('td');
            // 'name', 'username', 'password', 'url', 'host', 'notes'
            var search_text = $this.find('th').text() + '\n\n' +            // Name
                              $tds.eq(1).children('input').val() + '\n\n' + // Username
                              $tds.eq(2).find('.actual').val() + '\n\n' +   // Password
                              $tds.eq(3).find('a').attr('href') + '\n\n' +  // URL
                              $tds.eq(5).text() + '\n\n' +                  // Host
                              $tds.eq(6).text();                            // Notes
            row_cache.push([search_text.toLowerCase(), $this]);
        });

        // Add highlight class
        var style = document.createElement('style');
        style.type = 'text/css';
        style.innerHTML = '.highlight { background-color: yellow; outline: 1px solid invert; }';
        document.getElementsByTagName('head')[0].appendChild(style);

        $search.bind('keyup keypress blur change', function() {
            var $this = $(this);
            // Show/hide clear button
            $clear.toggle(!!$this.val());

            if (!$this.val().trim()) {
                $rows.show().unhighlight();
                fix_striping();
                return;
            }

            var i;
            var terms = $this.val().toLowerCase().split(/\s+/);
            var highlight_terms = [];
            // Don't highlight short search terms. It slows things down and isn't too useful
            for (i=0; i<terms.length; i++) {
                if (terms[i].length > 2)
                    highlight_terms.push(terms[i]);
            }

            for (i=0; i<row_cache.length; i++) {
                var _row = row_cache[i];
                var search_text = _row[0];
                var $row = _row[1];

                var found = true;
                for (var j=0; j<terms.length; j++) {
                    var term = terms[j];
                    if (search_text.indexOf(term) == -1) {
                        found = false;
                        break;
                    }
                }

                if (found) {
                    $row.show();
                    $row.unhighlight();
                    if (highlight_terms.length > 0)
                        $row.highlight(highlight_terms);
                } else {
                    $row.hide();
                }
            }

            fix_striping();
        });
    });
})(window.django.jQuery);
