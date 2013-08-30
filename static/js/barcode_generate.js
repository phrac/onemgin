$(document).ready(function() {
    $('.barcode_generator').submit(function() { // catch the form's submit event
        $('.barcode_generator_submit').button('loading');
        
        var divUpdate = $(this).attr('data-div-update');

        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                if(divUpdate){
                    $(divUpdate).hide().html(response).fadeIn("slow");
                };
                $('button').button('reset');

            },
            error: function(xhr, textStatus, error) {
                $(divUpdate).hide().html('<h3>Oops! '+textStatus+': '+error+'</h3>').fadeIn("slow");
                $('button').button('reset');
                $('.barcode_generator').each(function() {
                        this.reset();
                    });

            }
        });
        return false;
    });
});