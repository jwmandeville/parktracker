
// $(document).ready(function() {
//     $('.put-rating').each(function() {
//         var id = $(this).children(":first").html();
//         var rating = $('#'+id.toString()+'invrating');
//         rating = Math.round(rating*2)/2;
//         if (rating = 5) {
//             $('#five').attr('five','rated')
//         }
//     });
// });


$(function() {
var username = $('#username').html();
$('.ratingcontainer').each(function() {
        var id = $(this).children(":first").html();
        console.log('checked park' + id.toString());
        var rating = $('#'+id.toString()+'invrating').html();
        console.log('rating:' + rating.toString());
        rating = Math.round(rating*2)/2;
        console.log('new rating:' + rating.toString());
        var start = $(this).children('button:first');
        if (rating === 0) return;
        for (var i = 0; i < rating/0.5; i++) {
            start.addClass('rated');
            start = start.next();
        }
    });

$('.put-rating').hover(function() {
    var id = $(this).children(":first").html();
    var rating = $(this).children(":first").next().html();
    var cont = $('#'+id+'ratingcont');
    start = cont.children('button:first');
    $('#'+id+'ratingcont').children('button').each(function () {
        $(this).addClass('remove');
        //$(this).attr('id', 'remove');
    });
    for (var i = 0; i < rating/0.5; i++) {
        start.addClass('change');
        start = start.next();
    }
}, function() {
    var id = $(this).children(":first").html();
    var rating = $(this).children(":first").next().html();
    var cont = $('#'+id+'ratingcont');
    start = cont.children('button:first');
    $('#'+id+'ratingcont').children('button').each(function () {
        $(this).removeClass('remove');
        //$(this).attr('id', '');
    });
    for (var i = 0; i < rating/0.5; i++) {
        start.removeClass('change');
        start.attr('id', '');
        start = start.next();
    }
});


$('.put-rating').click(function(){
    console.log("fated!");  // sanity check
    var id = $(this).children(":first").html();
    var rating = $(this).children(":first").next().html();
    put_rating(id, rating, username);
});

function put_rating(id, rating, username) {
    console.log("create post is working!"); // sanity check
    console.log(id);
    console.log(rating);
    $.ajax({
        url : "put_rating/", // the endpoint
        type : "PUT", // http method
        data : {rating : rating.toString(), pid : id.toString()}, // data sent with the post request

        // handle a successful response
        success : function(json) {
            console.log(json); // log the returned json to the console
            if (!json.authenticated) {
                window.location.assign("/login/")
            }
            var pname = json.parkname;
            var pid = json.park_id;
            change_rating(pid, json.rating);
            console.log('#' + pid + 'rating'); // another sanity check
        },

        // handle a non-successful response
        error : function() {
            console.log("bad"); // provide a bit more info about the error to the console
        }
    });
};

function change_rating(pid, rating) {
    console.log(pid)
    console.log(rating)
    rating = Math.round(rating*2)/2;
    var start = $('#'+pid+'ratingcont').children('button:first');
    if (rating === 0) return;
    var count = 0;
    for (var i = 0; i < rating/0.5; i++) {
        start.addClass('rated');
        start = start.next();
        count++;
    }
    for (var i = count; i < 10; i++) {
        start.removeClass('rated');
        start = start.next();
    }
}

});