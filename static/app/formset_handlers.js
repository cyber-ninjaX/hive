(function($) { // < start of closure
    $(document).ready(function() {
        $('#id_password').attr('type', 'password'); 

        $('#id_password').click(function() {
            $(this).attr('type', 'text'); 
        });
        $('#id_password').focusout(function() {
            $(this).attr('type', 'password'); 
        });
    });
})(django.jQuery); // passes django.jQuery as parameter to closure block
