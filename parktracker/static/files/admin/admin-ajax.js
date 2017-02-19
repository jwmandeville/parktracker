$(document).ready(function() {
   $('#confirm').click(function() {
        // get form associated with the button
        var form = $(this).parents('form')
        $( "#dialog-confirm" ).dialog({
            resizable: false,
            height:140,
            modal: true,
            buttons: {
                "Yes": function() {
                    $( this ).dialog( "close" );
                    // maybe set an hidden field to keep button value if needed
                    form.submit()
                },

                "No": function() {
                    $( this ).dialog( "close" );
                }
            }
        });
        return false;
    })
});