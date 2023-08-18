(function($) {
    $(function() {
        ZeroClipboard.config({
            swfPath: '/media/flash/ZeroClipboard.swf'
        });

        $('.copy-password').each(function () {
            var that = this;
            that.clip = new ZeroClipboard(that);

            that.clip.on('ready', function () {
                that.clip.on('copy', function () {
                    if (that._keep_me_secret === undefined) {
                        var tmpel = $("<div></div>"),
                            password_id = $(that).attr('data-password-id');
                        tmpel.load('/admin/passwords/password/' + password_id + '/ #id_password', function () {
                            that._keep_me_secret = $("#id_password", tmpel).val();
                            $(that).text("Copy Password");
                        });
                    } else {
                        that.clip.setText(that._keep_me_secret);
                        $(that).parents('tr,.form-row').stop(true, true).effect('highlight');
                    }
                });
            });
        });
    });
})(window.django.jQuery);
