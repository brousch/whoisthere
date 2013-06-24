$(document).ready(function() {
    if ($('#message-wrapper').length > 0) {
        setTimeout(function() {
            $('#message-wrapper').fadeOut('slow');
        }, 10000);
    }
});
