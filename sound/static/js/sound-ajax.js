$(document).ready( function(){

    $('.like').click( function(event){

        var $song_id = $(this).attr('data-songid');
        var $me = $(this)
        var $icon = ' <span class="glyphicon glyphicon-thumbs-up"></span>'

        $.get('/add_like/', {song_id: $song_id}, function(data){

            $me.html(data + $icon);
        });

    });

    $('#add-comment-btn').click( function(event){

        var textarea = $('#id_text');
        var text = textarea.val();
        var songid = $(this).attr('data-songid');
        var author = $(this).attr('data-author');

        var context = {
            song_id: songid,
            author_name: author,
            text_body: text
        }
        $.get('/add_comment/', context, function(data){

            $('#comment-list').html(data);
            textarea.val('');
        });
    });
});